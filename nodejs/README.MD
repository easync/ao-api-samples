# Installation:
 - Install [Nodejs](https://nodejs.org/en/download/)
 - Install sample scripts project dependencies with running `npm i` in project folder `nodejs`
 - Get API token at https://app.easync.io/api
 - Open `place_an_order.js` in editor and replace string `00000000-0000-0000-0000-000000000000` with your API token
 - Open `retrieve_an_order.js` in editor and replace string `00000000-0000-0000-0000-000000000000` with your API token

# Usage: 
### Place an order
- `node place_an_order.js`
- Copy `request_id` value from response and paste it in `retrieve_an_order.js`

### Retrieve an order
- wait for about 3-5 minutes while order in process
- `node retrieve_an_order.js`