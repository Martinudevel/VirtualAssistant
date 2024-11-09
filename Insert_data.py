from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient("mongodb+srv://Arafat:negrusa2@bank.ggwz1.mongodb.net/bank?retryWrites=true&w=majority")

# Select the database
db = client.bank

# Select the collection
collection = db.transactions

# Define the data to be inserted
data = [
    {"source": "John Doe", "destination": "Smith", "money": 50},
    {"source": "Jane Smith", "destination": "Doe", "money": 100},
    {"source": "Bob Johnson", "destination": "Bob Johnson", "money": 2000}
]

# Insert data into the collection
collection.insert_many(data)

# Close the connection
client.close()