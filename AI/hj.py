import base64
import json
import os
from requests import post,get

client_id = "837b17147958429d8dc0f90dfd5413d2"
client_secret_id = "9b4b0dad41a84ce0bf6ad30340dd2388"
tokeaa = "BQDMywd3VN4qLOB-JlNMTm2DNVVDFLY7KseCoi3cf4WWeZFlMKrc6A_U7EFBlpfu8YndfPKV2ElIxPa78_ChEopXKxF-jTLtuE3tSMROp_eFhUnkpDE"

def get_token():
    auth_string = client_id +":"+client_secret_id
    auth_byte = auth_string.encode("utf-8")
    auth_ff = str(base64.b64encode(auth_byte),'utf-8')
    url = "https://accounts.spotify.com/api/token"
    headers= {
        'Authorization': 'Basic ' + auth_ff,
        "Content_type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url+query
    result = get(query_url,headers=headers)
    json_result = json.loads(result.content)
    return json_result["artists"]['items'][0]

token = get_token()
result = search_for_artist(token , "Taylor+swift")
print(result["name"] +"\n" + result["id"])
