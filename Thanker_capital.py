import requests

API = 0

ID_CLAN = "%23208QLOJJV"

#API
try:
    myapi_file = open("./api.txt")
    API = myapi_file.read()
    myapi_file.close()
except FileNotFoundError:
    print("Le fichier api.txt n'existe pas.")
if not API:
    API = input("Entre ton API (https://developer.clashofclans.com/): ")

#Récuperation des données
session = requests.Session()
session.headers.update({'Authorization': 'Bearer ' + API})
response = session.get("https://api.clashofclans.com/v1/clans/" + ID_CLAN + "/capitalraidseasons?limit=1")
data = response.json()

#Traitement
try:
    members = data['items'][0]['members']
    member_names = [member['name'] for member in members]
    str = "Merci à "
    for name in member_names:
        str += name + ", "
    str += "d'avoir participés au raid de ce weekend !"
    print(str)
except:
    print("Echec de la récuperation des données")