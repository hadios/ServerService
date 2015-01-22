from pymongo import MongoClient

def ListAllItemInDatabase (database):
	posts = database.post;
	
	for post in posts.find():
		print(post);

client = MongoClient();
db = client.test_database;

print(db);

# Add sample document
sampleItem = { "itemName" 	: "Ace Combat Assault Horizon Legacy",
			   "Edition"	: "Standard",
			   "Region" 	: "NTSC(US)",
			   "Price" 		: "$39.00" };
			   
posts = db.post;
post_id = posts.insert(sampleItem);
print(post_id);

ListAllItemInDatabase(db);