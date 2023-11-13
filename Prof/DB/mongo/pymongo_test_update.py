from pymongo_get_database import get_database
from dateutil import parser


# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()
collection_name = dbname["user_1_items"]
 
item_details = collection_name.find()
count = 0
for item in item_details:
   # This does not give a very readable output
   print(item)
   item["update_count"] +=1
   collection_name.update_one( {"_id" : item[ "_id"]}, {'$inc': {'update_count': count}})
   count += 1

collection_name.update_many({'update_count': {"$gt" : 10}}, {'$inc': {'update_count': 100}})


