import json
import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
# ottawa_wards_response.json()
body = json.loads(ottawa_wards_response.content)
# print(body) 

# Iterate through your new dictionary and display the name of each ward in the collection.

i=0
while i < len(body['objects']):
    print(body['objects'][i]['name'])
    i+=1


# Return to the main page of the API documentation. Pick another URL ("endpoint") from this API and use the same steps as above to make a request to that endpoint and convert the response into a Python dictionary.

ottawa_representatives = requests.get('https://represent.opennorth.ca/representatives')
head = json.loads(ottawa_representatives.content)
# print(head)

i=0
while i < len(head['objects']):
    print(head['objects'][i]['name'])
    i+=1

