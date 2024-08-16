import os

FILE_DATA = "./data.txt"


async def WeeklyActivity(ctx, session, ID_CLAN):
    try:
        data = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/capitalraidseasons?limit=1").json()['items'][0]
        all_members_name = session.get("https://api.clashofclans.com/v1/clans/%23" + ID_CLAN + "/members").json()['items']


        old_war_members = []
        if (os.path.exists(FILE_DATA)):
            with open(FILE_DATA, "r") as fichier:
                old_war_members = fichier.read().split('\n')

        retrogradation_list = [member['name'] for member in all_members_name]

        # PROMOTION
        members_promoted = []
        acutal_war = [member['name'] for member in data['members']]
        await ctx.send("\n\t*****PROMOTION*****")
        for member_info in all_members_name:
            member_name = member_info['name']
            if member_name in old_war_members or member_name in acutal_war:
                if member_info['role'] not in ['coLeader', 'leader', 'admin']:
                    if member_name in old_war_members and member_name in acutal_war:
                        members_promoted.append(member_info['name'])
                retrogradation_list.remove(member_name)
        await ctx.send(members_promoted)

        # RETROGRADATION
        await ctx.send("\n\t*****RETROGRADATION*****")
        await ctx.send(retrogradation_list)

        # ECRITURE DES ACTIFS DE LA SEMAINE DANS LE FICHIER
        with open(FILE_DATA, "w") as file:
            # file.write(formatted_end_time + '\n')
            for items in data['members']:
                file.write(items['name'] + '\n')

    except Exception as e:
        await ctx.send(str(e))
