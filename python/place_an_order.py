import requests
import json

true = True
false = False

API_TOKEN = '00000000-0000-0000-0000-000000000000'; #SEE https://app.easync.io/api for details

RETAILER = 'amazon';

PRODUCT_ID = 'B01K7C0CSA'; # Amazon US
# PRODUCT_ID = 'B01BRC1ZYE'; # Amazon DE
# PRODUCT_ID = 'B00V6C5Z0Q'; # Amazon UK
# PRODUCT_ID = 'B010S9M3L6'; # Amazon ES
# PRODUCT_ID = 'B019HC54WU'; # Amazon FR
# PRODUCT_ID = 'B019HC54WU'; # Amazon CA
# PRODUCT_ID = 'B007PNGRPC'; # Amazon IT

MAX_PRICE = 15000;

RETAILER_CREDENTIALS = {
	"email": 'user@gmail.com',
	"password": '123456'
}

BILLING_ADDRESS = {
    "first_name": "John",
    "last_name": "Smith",
    "address_line1": "14 Bus St.",
    "address_line2": "",
    "zip_code": "123456",
    "city": "Atlanta",
    "state": "GA",
    "country": "US",
    "phone_number": "1234567890"
}

SHIPPING_ADDRESS = {
    "first_name": "Eric",
    "last_name": "Walter",
    "address_line1": "18 Ellie St.",
    "address_line2": "",
    "zip_code": "070065",
    "city": "Sacramento",
    "state": "CA",
    "country": "US",
    "phone_number": "1234567890"
};

PAYMENT_METHOD = {
    "expiration_month": 9,
    "expiration_year": 9999,
    "name_on_card": "Jack Sparrow",
    "number": "0000000000000000",
    "security_code": "555",
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