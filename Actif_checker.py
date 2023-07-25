import requests
import os

API = 0

ID_CLAN     = "208QLOJJV"
FILE_DATA   = "./data.txt"
FILE_API    = "./api.txt"
#API
try:
    myapi_file = open(FILE_API)
    API = myapi_file.read()
    myapi_file.close()
except FileNotFoundError:
    print("Le fichier api.txt n'existe pas.")
if not API:
    API = input("Entre ton API (https://developer.clashofclans.com/): ")

#Récuperation des données
session = requests.Session()
session.headers.update({'Authorization': 'Bearer ' + API})
response = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/capitalraidseasons?limit=1")
data = response.json()

#Traitement
try:
    content_file = []
    list_items = ""
    if (os.path.exists(FILE_DATA)):
        with open(FILE_DATA, "r") as fichier:
            content_file = fichier.read()
        content_file.split('\n')
        # print(content_file[:-1])
    # PROMOTION
    for items in data['items'][0]['members']:
        actual = items['name']
        for past in content_file.split('\n'):
            print(past)
            print(actual)
            if acutal == past:
                print(actual + " a besoin d'une promotion")
                continue
    with open(FILE_DATA, "w") as fichier:
        for items in data['items'][0]['members']:
            fichier.write(items['name'] + '\n')

    # ensemble = list(set(list_items) | set(content_file))
    # Écrire le contenu dans le fichier
        # members_war_1 = items['members']
    # members_war_2 = data['items'][1]
        # for member in items['name']:
    # member_names__war_2 = [member['name'] for member in members_war_2]
        # print(member)
    # print(members_war_2)
except:
    print("Echec de la récuperation des données")