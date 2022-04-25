import pymongo

client = pymongo.MongoClient(host="localhost")
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

db = client['test']
# 相当于数据库表
collection = db.students

# result = collection.insert_many([student, student2])
# print(result)

# 查找年龄大于20的
# one = collection.find_one({'age': {'$gt': 20}})
# print(one)

# results = collection.find({'name': {'$regex': '^M.*'}})
# print(results)

# 这个用不了，可能跟版本有关系
# count = collection.find().count()
# print(count)

# 排序
# r = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([x['name'] for x in r])

r2 = collection.delete_many({'name': 'Jordan'})


# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html 操作api
r = collection.find().sort('name', pymongo.ASCENDING)
print([x['name'] for x in r])