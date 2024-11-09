from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
import openai

app = Flask(__name__)

# Load TinyLlama model and tokenizer
model_name = "TinyLlama-1.1B"  # replace with the actual model name if needed
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to handle queries with TinyLlama
def query_tinyllama(query):
    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Financial API integration (Example with Yahoo Finance)
def get_stock_price(stock_symbol):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={stock_symbol}"
    response = requests.get(url)
    data = response.json()
    price = data['quoteResponse']['result'][0]['regularMarketPrice']
    return price

# Your finance bot's functionality
def finance_bot(query):
    if "stock" in query.lower():
        # Extract stock symbol from the query
        stock_symbol = query.split(" ")[-1].upper()
        stock_price = get_stock_price(stock_symbol)
        return f"The current price of {stock_symbol} is ${stock_price}"

    elif "inflation" in query.lower():
        return query_tinyllama("Explain how inflation affects my savings.")

    elif "interest rate" in query.lower():
        return query_tinyllama("What are the current interest rates for savings accounts?")

    else:
        # For general queries, use TinyLlama to generate a response
        return query_tinyllama(query)

# Endpoint to handle user messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    if "stock" in user_message.lower():
        # Extract stock symbol (just a simple example)
        stock_symbol = user_message.split(" ")[-1].upper()
        stock_price = get_stock_price(stock_symbol)
        return jsonify({'response': f"The current price of {stock_symbol} is ${stock_price}"})
    else:
        # Otherwise, use TinyLlama to generate a response
        response = query_tinyllama(user_message)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

# Example use case
user_query = "What is the current stock price of Tesla?"
response = finance_bot(user_query)
print(response)