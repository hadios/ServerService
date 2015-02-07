// BASE SETUP
// ==================================================================================

// call the packages we need
var express		= require('express');
var app			= express();
var bodyParser	= require('body-parser');
var cors		= require('cors');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

var port = process.env.PORT || 8080;

// Setup mongoose
var mongoose	= require('mongoose');
mongoose.connect('mongodb://localhost:27017/test_database');

//var Bear		= require('./app/models/bear');
var Product	= require('./app/models/product');

// ROUTES FOR API
// ==================================================================================
var router = express.Router();

router.use(function(req, res, next) {
	// Logging
	console.log('Something is happening.');
	next();
});

// Test route for GET
router.get('/', function(req, res) {
	res.json({ message: 'Hooray! Welcome to our api!' });
});

// For routes that ends in /products
// ==================================================================================
router.route('/products')

	// POST 
	.post(function(req, res) {
		var product = new Product();
		product.name = req.body.name;
		product.edition = req.body.name;
		
		product.save(
			function(err) {
				if (err) {
					res.send(err);
				}
				
				res.json({ message: 'Product created!' });
			}
		);
	})
	
	// GET
	.get(function(req, res) {
		Product.find(function(err, products) {
			if (err) {
				res.send(err);
			}
			
			res.json(products);
		});
	});
	
// For routes that ends in /products
// ==================================================================================
router.route('/products/:product_id')

	.get(function(req, res) {
		
		Product.findOne({ 'itemNo': req.params.product_id }, function(err, product) {
			if (err) {
				res.send(err);
			}
			
			res.json(product);
		});
	})
	
	.put(function(req, res) {
		Product.findById({ 'itemNo': req.params.product_id }, function(err, product) {
			if (err) {
				res.send(err);
			}
			
			if (req.body.name != null) {
				product.name = req.body.name;
			}
			
			if (req.body.priceSg != null) {
				product.priceSg = req.body.priceSg;
			}
			
			product.save(function(err) {
				if (err) {
					res.send(err);
				}
				res.json({ message: 'Product updated!' });
			});
		});
	})
	
	.delete(function(req, res) {
		Product.remove({ 'itemNo': req.params.product_id }, function(err, product) {
			if (err) {
				res.send(err);
			}
			res.json({ message: 'Successfully deleted' });
		});
	});
	

// REGISTER ROUTES
app.use('/api', router);

// START THE SERVER
// ==================================================================================
app.listen(port);
console.log('Magic happens on port ' + port);