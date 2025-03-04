// BASE SETUP
// ==================================================================================

// call the packages we need
var express		= require('express');
var app			= express();
var bodyParser	= require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;

// Setup mongoose
var mongoose	= require('mongoose');
mongoose.connect('mongodb://localhost:27017/');

var Bear		= require('./app/models/bear');

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

// For routes that ends in /bears
// ==================================================================================
router.route('/bears')

	// POST 
	.post(function(req, res) {
		var bear = new Bear();
		bear.name = req.body.name;
		
		bear.save(
			function(err) {
				if (err) {
					res.send(err);
				}
				
				res.json({ message: 'Bear created!' });
			}
		);
	})
	
	// GET
	.get(function(req, res) {
		Bear.find(function(err, bears) {
			if (err) {
				res.send(err);
			}
			
			res.json(bears);
		});
	});
	
// For routes that ends in /bears
// ==================================================================================
router.route('/bears/:bear_id')

	.get(function(req, res) {
		Bear.findById(req.params.bear_id, function(err, bear) {
			if (err) {
				res.send(err);
			}
			
			res.json(bear);
		});
	})
	
	.put(function(req, res) {
		Bear.findById(req.params.bear_id, function(err, bear) {
			if (err) {
				res.send(err);
			}
			
			bear.name = req.body.name;
			bear.save(function(err) {
				if (err) {
					res.send(err);
				}
				res.json({ message: 'Bear updated!' });
			});
		});
	})
	
	.delete(function(req, res) {
		Bear.remove({ _id: req.params.bear_id }, function(err, bear) {
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