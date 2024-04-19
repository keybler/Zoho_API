#this works to get auth_code

import requests
import json

def generate_auth_url(client_id, redirect_uri):
    scope = "ZohoInventory.FullAccess.all"
    auth_url = (f"https://accounts.zoho.com/oauth/v2/auth?scope={scope}&client_id={client_id}"
                f"&response_type=code&access_type=offline&redirect_uri={redirect_uri}")
    return auth_url

client_id = "1000.abc123"
redirect_uri = "https://www.abc123.com"

auth_url = generate_auth_url(client_id, redirect_uri)
print("Visit this URL to authorize:", auth_url)

#print(code)

uth_url)

#print(code)

