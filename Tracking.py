import polygon
from pymongo import MongoClient

# Create a REST client
client = polygon.RESTClient(
    api_key="0b_OzOzhi4hrhdQIBgjeNF1VOr2OYCUc")

class Tracking:
    def __init__(self):
        # Connect to MongoDB
        self.client = MongoClient("mongodb+srv://Arafat:negrusa2@bank.ggwz1.mongodb.net/bank?retryWrites=true&w=majority")
        self.db = self.client.bank
        self.collection = self.db.transactions

    def get_transactions(self):
            # Fetch data from MongoDB
            return list(self.collection.find())
    def close(self):
            # Close the MongoDB client
            self.client.close()

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
