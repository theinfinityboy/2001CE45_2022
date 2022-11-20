import os
import math
#importing library 
from datetime import datetime
start_time = datetime.now()

os.system('cls')
#clearing screen
def team_pak_list():
	#making playing 11 list of pakistan
    with open('teams.txt') as team_name_file:
        str_team_pak=''
        for line in team_name_file:
            if line[0]=='P':
                str_team_pak=line
				#searching for team name that is pakistan then traversing though that line 

        start_index_pak=str_team_pak.find(':')
        pak_team_xi=str_team_pak[start_index_pak+2:len(str_team_pak)-1]
        team_pak=pak_team_xi.split(', ')
		#splitted on the basis of comma because names in the txt file are separated by comma.

        return team_pak

def team_ind_list():
	#making playing 11 list of india
    with open('teams.txt') as team_name_file:
        team_ind_str=''
        for line in team_name_file:
            if line[0]=='I':
                team_ind_str=line
				#searching for team name that is pakistan then traversing though that line 



        start_index_ind=team_ind_str.find(':')
        ind_team_xi=team_ind_str[start_index_ind+2:len(team_ind_str)-1]
        team_ind=ind_team_xi.split(', ')
		#splitted on the basis of comma because names in the txt file are separated by comma.
	

        return team_ind


#Help
def scorecard():
	pass


###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
