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

# Récuperation des données
    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer ' + API})
    data = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/capitalraidseasons?limit=1").json()['items'][0]
    all_members_name = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/members").json()['items']

# Traitement
    old_war_members = []
    if (os.path.exists(FILE_DATA)):
        with open(FILE_DATA, "r") as fichier:
            old_war_members = fichier.read().split('\n')

    # DATE
    end_time = datetime.datetime.strptime(data['endTime'], "%Y%m%dT%H%M%S.%fZ")
    formatted_end_time = end_time.strftime("%d/%m/%Y")

    retrogradation_list = [member['name'] for member in all_members_name]

    # PROMOTION
    acutal_war = [member['name'] for member in data['members']]
    print("\n\t*****PROMOTION*****")
    for member_info in all_members_name:
        member_name = member_info['name']
        if member_name in old_war_members or member_name in acutal_war:
            if member_name in old_war_members and member_name in acutal_war:
                if member_info['role'] not in ['coLeader', 'leader', 'admin']:
                    print(f"{member_name}")
            retrogradation_list.remove(member_name)

    # RETROGRADATION
    print("\n\t*****RETROGRADATION*****")
    for member_name in retrogradation_list:
        print(f"{member_name}")

    # ECRITURE DES ACTIFS DE LA SEMAINE DANS LE FICHIER
    with open(FILE_DATA, "w") as file:
        file.write(formatted_end_time + '\n')
        for items in data['members']:
            file.write(items['name'] + '\n')

except Exception as e:
    print("Echec de la récuperation des données:", e.__str__)
