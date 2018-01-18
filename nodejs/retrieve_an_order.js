const API_TOKEN = '00000000-0000-0000-0000-000000000000'; //SEE https://app.easync.io/api for details

const REQUEST_ID = 'c78b4ac0-fac7-11e7-af7a-a3722abb32e3'; //CREATE REQUEST WITH place_an_order.js FIRST

require('request')({
		url: 'https://core.easync.io/api/v1/orders/'+REQUEST_ID,
		method: 'GET',
		headers: {
			'Authorization': "Basic " + new Buffer(API_TOKEN + ":").toString("base64"),
		},
	},
	(error, response, body) => {
		console.log(body);
	}
);

