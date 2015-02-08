from pymongo import MongoClient

PRODUCTFILE_NAME = ['3ds.csv', 'vita.csv', 'xboxone.csv'];
FILE_FORMAT = {
				'itemNo' 			: 0,
				'itemName' 			: 1,
				'edition' 			: 2,
				'region'			: 3,
				'priceSingapore'	: 4,
				'priceMalaysia'		: 5,
				'type'				: 6};

DATABASE_NAME 	= 'test_database';
COLLECTION_NAME = 'products';				

def ListAllItemInDatabase (database, collectionName):
	posts = database[collectionName];
	
	for post in posts.find():
		print(post);
		
def UpdateAndAddProductInfoFromList(collectionToAddTo, filename):
	# Open file and read line by line
	with open(filename) as file:
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
			sampleItem = { 
						   "Sn"			: elements[FILE_FORMAT['itemNo']],
						   "Name" 		: elements[FILE_FORMAT['itemName']],
						   "Edition"	: elements[FILE_FORMAT['edition']],
						   "Region" 	: elements[FILE_FORMAT['region']],
						   "PriceSG" 	: elements[FILE_FORMAT['priceSingapore']].translate(None, '$'),
						   "PriceMY" 	: elements[FILE_FORMAT['priceMalaysia']].translate(None, 'RM'),
						   "Type" 		: elements[FILE_FORMAT['type']].translate(None, '\n')};
		
			#print(sampleItem);
		
			# Check if item is already in database
			findResult = collectionToAddTo.find_one({"Name": sampleItem['Name'], "Type": sampleItem['Type'], "Edition": sampleItem['Edition'], "Region": sampleItem['Region'], });
			
			if (findResult != None):
				print(findResult);
				print(sampleItem);
				# If it is, update the price
				collectionToAddTo.update({"Name": sampleItem['Name']}, 
										 {"$set": 
											{"PriceSG": sampleItem['PriceSG'], 
											 "PriceMY": sampleItem['PriceMY']}
										 });
				#print(sampleItem['Name'] + ", " + sampleItem['Type'] + " Overwrite!");
			else:
				# Else, insert the data
				collectionToAddTo.insert(sampleItem);
	
def Main ():
	# Connect to default mongo client
	client = MongoClient();
	
	# Get database
	db = client[DATABASE_NAME];
	print(db);
	
	# Create new collection
	productCollection = db[COLLECTION_NAME];
	productCollection.remove();
	
	for item in PRODUCTFILE_NAME:
		UpdateAndAddProductInfoFromList(productCollection, item);
		
	#ListAllItemInDatabase(db, COLLECTION_NAME);
	print("Total items: " + str(productCollection.count()));
	
#------------------------------------------------------------------------------
Main();