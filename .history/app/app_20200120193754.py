import pymongo

url = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(url)
db = client['demo']
collection = database['students']

students = collection.find({})

print(students)



