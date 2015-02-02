from pymongo import MongoClient

PRODUCTFILE_NAME = 'productlist.csv'
FILE_FORMAT = {
				'itemNo' 			: 0,
				'itemName' 			: 1,
				'edition' 			: 2,
				'region'			: 3,
				'priceSingapore'	: 4,
				'priceMalaysia'		: 5 };		

def ListAllItemInDatabase (database):
	posts = database.post;
	
	for post in posts.find():
		print(post);
		
def Main ():
	# Connect to default mongo client
	client = MongoClient();
	db = client.test_database;

	# Print out existing information in database
	print(db);

	# Open up collection
	posts = db.productlist;
	
	# Open file and read line by line
	with open(PRODUCTFILE_NAME) as file:
		line = file.readline;
		
		skip = True;
		for currentLine in file:
			if (skip):
				skip = False;
				continue;
			
			print(currentLine);
			elements = currentLine.split(',');
		
			# Check if item is already in database
				# If it is, update the price
				
				# Else, insert the data
		
		
	'''
	# Add sample document
	sampleItem = { "itemName" 	: "Ace Combat Assault Horizon Legacy",
				   "Edition"	: "Standard",
				   "Region" 	: "NTSC(US)",
				   "Price" 		: "$39.00" };
				   
	
	post_id = posts.insert(sampleItem);
	print(post_id);
	'''

	ListAllItemInDatabase(db);
	
	
#------------------------------------------------------------------------------
Main();