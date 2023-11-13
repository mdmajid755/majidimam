from pymongo_get_database import get_database

# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()

# Retrieve a collection named "user_1_items" from database
collection_name = dbname["user_1_items"]
 
item_details = collection_name.find()
for item in item_details:
   # This does not give a very readable output
   print(item)
