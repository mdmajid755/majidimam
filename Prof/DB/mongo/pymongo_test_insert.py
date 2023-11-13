from pymongo_get_database import get_database
from dateutil import parser


# Get the database using the method we defined in pymongo_test_insert file
db = get_database()
collection_name = db["user_1_items"]

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance",
  "update_count" : 0
}
collection_name.insert_one(item_1)

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs",
  "update_count" : 0
}

expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)

item_3 = {
  "item_name" : "Bread",
  "quantity" : 2,
  "ingredients" : "all-purpose flour",
  "expiry_date" : expiry,
  "update_count" : 0,
  "extra_field_not_in_other_documents": True
}

collection_name.insert_many([item_2,item_3])



 