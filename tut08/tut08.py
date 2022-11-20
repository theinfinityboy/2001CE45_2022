import os
import math
#importing library 
from datetime import datetime
start_time = datetime.now()

os.system('cls')
#clearing screen
def team_pak_list():
	#making playing 11 list
    with open('teams.txt') as team_file:
        str_team_pak=''
        for line in team_file:
            if line[0]=='P':
                str_team_pak=line

        start_index_pak=str_team_pak.find(':')
        pak_team_xi=str_team_pak[start_index_pak+2:len(str_team_pak)-1]
        team_pak=pak_team_xi.split(', ')

        return team_pak


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
