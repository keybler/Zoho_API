# This works. Getting the auth token was pain in the ass. I'm not sure if it will expire. I also need to get my creds out of this script.

import http.client
import json

conn = http.client.HTTPSConnection("www.zohoapis.com")
headers = {'Authorization': "Zoho-oauthtoken 1000.abc123"}

conn.request("GET", "/inventory/v1/items?organization_id=abc123", headers=headers)

res = conn.getresponse()
data = res.read()

# Decode and parse the JSON data
items_data = json.loads(data.decode("utf-8"))

# Check if the 'items' key is in the response
if 'items' in items_data:
    for item in items_data['items']:
        # Extract and print relevant information for each item
        print(f"Item Name: {item.get('name', 'N/A')}")
        print(f"SKU: {item.get('sku', 'N/A')}")
        print(f"Price: {item.get('rate', 'N/A')}")
        print(f"Stock: {item.get('stock', 'N/A')}")
        print(f"purchase_rate: {item.get('purchase_rate', 'N/A')}")
        print("-" * 40)  # Separator for readability
else:
    print("No items found or invalid response.")
bility
else:
    print("No items found or invalid response.")
