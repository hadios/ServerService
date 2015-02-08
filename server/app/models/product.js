var mongoose	= require('mongoose');
var Schema		= mongoose.Schema;

var ProductSchema	= new Schema({
	id:			Number,
	name: 		String,
	edition: 	String,
	region: 	String,
	priceSg: 	Number,
	priceMy:	Number,
	type:		String
});

module.exports = mongoose.model('Product', ProductSchema);