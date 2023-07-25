import requests
import os

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
try:

    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer ' + API})
    data = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/capitalraidseasons?limit=1").json()
    all_members_name = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/members").json()
except:
    print("Echec de la récuperation des données")

#Traitement
try:
    if (os.path.exists(FILE_DATA)):
        with open(FILE_DATA, "r") as fichier:
            old_war_members = fichier.read().split('\n')


    # PROMOTION
    print("\n\t*****PROMOTION*****")
    for items in data['items'][0]['members']:
        for past in old_war_members:
            if items['name'] == past:
                print(items['name'] + "      \tà besoin d'une promotion.")
                continue


    # ECRITURE DES ACTIFS DE LA SEMAINE DANS LE FICHIER
    with open(FILE_DATA, "w") as fichier:
        for items in data['items'][0]['members']:
            fichier.write(items['name'] + '\n')
            old_war_members.append(items['name'])


    #RETROGRADATION
    print("\n\t*****RETROGRADATION*****")
    retrogradation_list = []
    for member in all_members_name['items']:
        member = member['name']
        retrogradation_list.append(member)
        for actif in old_war_members:
            if not actif:
                continue
            if member == actif:
                retrogradation_list.remove(member)
                break
    for member in retrogradation_list:
        print(member)
except:
    print("Echec du traitement des données")