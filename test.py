import pymongo

client = pymongo.MongoClient("mongodb+srv://Rakku_99:mongoDB2022@cluster0.n3owz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "rakesh",
    "email": "rakeshranjan4294@gmail.com",
    "surname": "ranjan"
}
db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d )