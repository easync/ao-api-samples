import requests

API_TOKEN = '00000000-0000-0000-0000-000000000000'; #SEE https://app.easync.io/api for details

REQUEST_ID = '66e94c40-facb-11e7-b69b-2f40a5f75e83'; #CREATE REQUEST WITH place_an_order.js FIRST

print requests.get("https://core.easync.io/api/v1/orders/"+REQUEST_ID, auth=(API_TOKEN, '')).content;

