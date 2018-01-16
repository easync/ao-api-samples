# Installation:
 - Install [Python 2.7](https://www.python.org/download/releases/2.7/)
 - Install [python requests module](http://docs.python-requests.org/en/master/user/install/)
 - Get API token at https://app.easync.io/api
 - Open `place_an_order.py` in editor and replace string `00000000-0000-0000-0000-000000000000` with your API token
 - Open `retrieve_an_order.py` in editor and replace string `00000000-0000-0000-0000-000000000000` with your API token

# Usage: 
### Place an order
- `python place_an_order.py`
- Copy `request_id` value from response and paste it in `retrieve_an_order.py`

### Retrieve an order
- wait for about 3-5 minutes while order in process
- `python retrieve_an_order.py`