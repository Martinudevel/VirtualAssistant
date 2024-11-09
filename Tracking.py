import polygon
from pymongo import MongoClient

# Create a REST client
client = polygon.RESTClient(
    api_key="0b_OzOzhi4hrhdQIBgjeNF1VOr2OYCUc")



# Create a tracking database
response = client.get_aggs(
    ticker="AAPL",
    multiplier=1,
    timespan="day",
    from_="2023-01-09",
    to="2023-01-09"
)
print(response)


# Connect to MongoDB
mongo_client = MongoClient("mongodb+srv://Arafat:negrusa2@bank.ggwz1.mongodb.net/bank?retryWrites=true&w=majority")

# Select the database
db = mongo_client.bank

# Select the collection
collection = db.transactions

# Fetch data from MongoDB
data = collection.find()

# Process the data as needed
for record in data:
    print(record)

# Close the MongoDB client
mongo_client.close()
