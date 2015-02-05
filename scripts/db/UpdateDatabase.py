from pymongo import MongoClient

PRODUCTFILE_NAME = 'productlist.csv'
FILE_FORMAT = {
				'itemNo' 			: 0,
				'itemName' 			: 1,
				'edition' 			: 2,
				'region'			: 3,
				'priceSingapore'	: 4,
				'priceMalaysia'		: 5 };

DATABASE_NAME 	= 'test_database';
COLLECTION_NAME = 'productlist';				

def ListAllItemInDatabase (database, collectionName):
	posts = database[collectionName];
	
	for post in posts.find():
		print(post);
		
def UpdateAndAddProductInfoFromList(collectionToAddTo, filename):
	# Open file and read line by line
	with open(PRODUCTFILE_NAME) as file:
		line = file.readline;
		
		skip = True;
		for currentLine in file:
			if (skip):
				skip = False;
				continue;
			
			#print(currentLine);
			elements = currentLine.split(',');
		
			# Create the product information
			# Add sample document
			sampleItem = { "itemName" 		: elements[FILE_FORMAT['itemName']],
						   "Edition"		: elements[FILE_FORMAT['edition']],
						   "Region" 		: elements[FILE_FORMAT['region']],
						   "Price($SG)" 	: elements[FILE_FORMAT['priceSingapore']],
						   "Price($MY)" 	: elements[FILE_FORMAT['priceMalaysia']] };
		
			#print(sampleItem);
		
			# Check if item is already in database
			findResult = collectionToAddTo.find_one({"itemName": sampleItem['itemName']});
			
			if (findResult != None):
				# If it is, update the price
				collectionToAddTo.update({"itemName": sampleItem['itemName']}, 
										 {"$set": 
											{"Price($SG)": sampleItem['Price($SG)'], 
											 "Price($MY)": sampleItem['Price($MY)']}
										 });
			else:
				# Else, insert the data
				collectionToAddTo.insert(sampleItem);
	
def Main ():
	# Connect to default mongo client
	client = MongoClient();
	
	# Get database
	db = client[DATABASE_NAME];
	
	# Create new collection
	productCollection = db[COLLECTION_NAME];
	productCollection.remove();
	
	UpdateAndAddProductInfoFromList(productCollection, PRODUCTFILE_NAME);
	#ListAllItemInDatabase(db, COLLECTION_NAME);
	print("Total items: " + str(productCollection.count()));
	
#------------------------------------------------------------------------------
Main();