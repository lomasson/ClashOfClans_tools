import requests
import datetime
import os

ID_CLAN     = "208QLOJJV"
FILE_DATA   = "./data.txt"
FILE_API    = "./api.txt"
# me #JJ2YGY08
API         = ""
try:
    myapi_file = open(FILE_API)
    API = myapi_file.read()
    myapi_file.close()
except FileNotFoundError:
    print("Le fichier api.txt n'existe pas.")

if not API:
    API = input("Entre ton API (https://developer.clashofclans.com/): ")


try:
#Récuperation des données
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer ' + API})
    data = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/capitalraidseasons?limit=1").json()['items'][0]
    all_members_name = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/members").json()['items']

#Traitement
    old_war_members = []
    if (os.path.exists(FILE_DATA)):
        with open(FILE_DATA, "r") as fichier:
            old_war_members = fichier.read().split('\n')

    # DATE
    end_time = datetime.datetime.strptime(data['endTime'], "%Y%m%dT%H%M%S.%fZ")
    formatted_end_time = end_time.strftime("%d/%m/%Y")

    # PROMOTION
    print("\n\t*****PROMOTION*****")
    for member_info in all_members_name:
        # Check if the member is not a CoLeader or admin
        if member_info['role'] not in ['coLeader', 'admin']:
            member_name = member_info['name']
            if member_name in old_war_members:
                print(f"{member_name}")

    # ECRITURE DES ACTIFS DE LA SEMAINE DANS LE FICHIER
    with open(FILE_DATA, "w") as file:
        file.write(formatted_end_time + '\n')
        for items in data['members']:
            file.write(items['name'] + '\n')
            old_war_members.append(items['name'])


    #RETROGRADATION
    print("\n\t*****RETROGRADATION*****")
    retrogradation_list = [member['name'] for member in all_members_name]

    for actif in old_war_members:
        if not actif:
            continue
        if actif in retrogradation_list:
            retrogradation_list.remove(actif)

    for member_name in retrogradation_list:
        print(f"{member_name}")

except Exception as e:
    print("Echec de la récuperation des données:", str(e))
