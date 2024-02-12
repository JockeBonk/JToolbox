import requests

response = requests.get('https://randomuser.me/api')

#print(response.status_code)
#print(response.json())

title = response.json()['results'][0]['name']['title']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
age = response.json()['results'][0]['dob']['age']
gender = response.json()['results'][0]['gender']

print(f"{title}. {first_name} {last_name}")
print(gender)
print(f"{age} y/o")
