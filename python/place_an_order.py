import requests
import json

true = True
false = False

API_TOKEN = '00000000-0000-0000-0000-000000000000'; #SEE https://app.easync.io/api for details

RETAILER = 'amazon';

PRODUCT_ID = 'B01K7C0CSA';

MAX_PRICE = 15000;

RETAILER_CREDENTIALS = {
	"email": 'user@gmail.com',
	"password": '123456'
}

BILLING_ADDRESS = {
    "first_name": "William",
    "last_name": "Rogers",
    "address_line1": "84 Massachusetts Ave",
    "address_line2": "",
    "zip_code": "02139",
    "city": "Cambridge",
    "state": "MA",
    "country": "US",
    "phone_number": "5551234567"
}

SHIPPING_ADDRESS = {
    "first_name": "Tim",
    "last_name": "Beaver",
    "address_line1": "77 Massachusetts Avenue",
    "address_line2": "",
    "zip_code": "02139",
    "city": "Cambridge",
    "state": "MA",
    "country": "US",
    "phone_number": "5551230101"
};

PAYMENT_METHOD = {
    "expiration_month": 7,
    "expiration_year": 9999,
    "name_on_card": "Patrick Williams",
    "number": "0000000000000000",
    "security_code": "333",
    "use_gift": true
};

ORDER = {
  "retailer": RETAILER,
  "retailer_credentials": RETAILER_CREDENTIALS,	
  "products": [
    {
      "product_id": PRODUCT_ID,
      "quantity": 1,
      "seller_selection_criteria": {
        "condition_in": [
          "New"
        ],
        "handling_days_max": 5,
        "max_item_price": MAX_PRICE,
        "prime": true
      }
    }
  ],
  "shipping_address": SHIPPING_ADDRESS,
  "shipping_method": "free",
  "billing_address": BILLING_ADDRESS,
  "payment_method": PAYMENT_METHOD,
  "is_gift": true,
  "gift_message": "Thank you so much!",
  "max_price": MAX_PRICE,
}


print requests.post("https://core.easync.io/api/v1/orders", auth=(API_TOKEN, ''), json=ORDER).content;