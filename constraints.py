#!/usr/bin/python

partners = [("Partner1",2),("Partner2",3),("Partner3",2),("Partner4",1),("Partner5",2),("Partner6",1),("Partner7",2)]

for partner in partners :
    print(partner[0] + " - " + str(partner[1]) + " agents")

req_meetings = [[0,1],[1,2,3],[0,6],[3,4,5,6],[2,4],[3,5],[0,1,5,6],[4,5]]

for rm in req_meetings :
    reg_partners = ""
    for partner_id in rm :
        reg_partners += partners[partner_id][0] + " "
    print("Meeting: " + reg_partners)
