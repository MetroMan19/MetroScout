import requests
import json
#vgrmy8SPUvXCUDssToWwmgd1M7XhXQh1wZlXGKr1P30TDsNbrXE1qS5lHQtbzds0

#set up requests headers & urls
headers = {'X-TBA-Auth-Key':'vgrmy8SPUvXCUDssToWwmgd1M7XhXQh1wZlXGKr1P30TDsNbrXE1qS5lHQtbzds0'}

def allTeamMatches(teamKey, year):
    #set up url
    teamMatchURL = ('https://www.thebluealliance.com/api/v3/team/{}/matches/{}/keys'.format(teamKey, year))
    #retrive data from tba
    r = requests.get(teamMatchURL, headers=headers)
    teamMatchList = json.loads(r.text)
    for match in teamMatchList:
        matchURL = ('https://www.thebluealliance.com/api/v3/match/{}'.format(match))
        #retrive data from tba
        r = requests.get(matchURL, headers=headers)
        match = json.loads(r.text)
        for groups in match:
            for teams in match['alliances']:
                
        
