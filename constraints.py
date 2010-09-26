#!/usr/bin/python
import itertools

# Definitions, later read from arguments

# partners definition in format of tuple - (PartnerName, PartnerID, NumOfAgents)
partners = [("Partner1",1,2),("Partner2",2,3),("Partner3",3,2),("Partner4",4,1),("Partner5",5,2),("Partner6",6,1),("Partner7",7,2)]

# available rooms for meeting - array of rooms - [RoomName, RoomID, Capacity], capacity define max num. of agents for one meeting
rooms = [['Room1',0,2],['Room2',1,4],['Room3',2,2]]

# requests for meetings - in  format of arrays of partner ids, meeting id
req_meetings = [([0,1],1),([1,2,3],2),([0,6],3),([3,4,5,6],4),([2,4],5),([3,5],6),([0,1,5,6],7),([4,5],8), ([0,4],9), ([1,2,3,4],10)]

# time blocks in which meeting can be arrange
time_blocks = 4


# Generator of Prolog code

code = ":- use_module(library(clpfd)). \n"

# Partners clauses

code += "% Partners definition \n"

for partner in partners :
    code += "partner(" + str(partner[1]) + "," + str(partner[2]) + "). \n"


code += "% Rooms definition \n"

for room in rooms :
    code += "room(" + str(room[1]) + "," + str(room[2]) + "). \n"

code += "% Meeting requests definition \n"
for request in req_meetings :
    code += "request(" + str(request[0]) + "). \n"

code += "% Meeting definition \n"
code += '''\nmeeting(Partners,_,Room) :-
    request(Partners),
    room(Room,RoomSize),
    persons_count(Partners,Count),
    RoomSize >= Count.'''

code+= '''\n\npersons_count([],0).

persons_count([_|Rest],Count) :-
    persons_count(Rest,PartResult),
    Count is PartResult+1. \n\n'''


time_names = list()
place_names = list()

for rm in req_meetings :
    time_names.append("Time" + str(rm[1]))
    place_names.append("Place" + str(rm[1]))

code+= ":- Times = " + str(time_names).replace("'","") + ", Times ins 1.." + str(time_blocks) + ",\n"
code+= "   Places = " + str(place_names).replace("'","") + ", Places ins 0.." + str(len(rooms)-1) + ",\n   "
for rm in req_meetings :
    i = str(rm[1])
    code += "meeting(" + str(rm[0]) + ", Time" + i + ", Place" + i + "),"
code+="\n"

# CONSTRAINTS!!!
perms = list(itertools.combinations(range(1,len(req_meetings)+1),2))
for p in perms :
    code+= "Place"+ str(p[0]) + " #= Place" + str(p[1]) + " #==> Time" + str(p[0]) + " #\\= Time" + str(p[1]) + ", \n"


for partner in partners :
    pid = partner[1] - 1
    agents = partner[2]
    p_meetings = list()
    #print(partner[0] + " : ")
    for rm in req_meetings :
        if (rm[0].count(pid) > 0 ) :
            #print(rm)
            p_meetings.append(rm[1])
    if len(p_meetings) <= agents :
        #print(partner[0] + " is OK")
        t=1
    else :
        combs = list(itertools.combinations(p_meetings,agents))
        #print(partner[0])
        #print(combs)
        for comb in combs :
            rest = list(p_meetings)
            for item in comb :
                rest.remove(item)
            constraint = ""
            if(len(comb)>1) :
                for item in comb :
                    constraint += "Time" + str(item)
                    if(comb.index(item)+1 < len(comb)) :
                        constraint += " #= "
                    else :
                        constraint += " #==> "
            for item in rest :
                constraint += "( Time" + str(comb[0]) + " #\\= Time" + str(item) + ") "
                if(rest.index(item)+1 < len(rest)) :
                    constraint +="#/\\ "

            constraint += ","
            #print(constraint)
    #print("\n")
code += constraint
# END OF CONSTRAINTS

code+="labeling([down], Places), labeling([down], Times),\n"
code+="write('Times'),write(Times),write(' Rooms'),write(Places).\n"
#print time_names
#print place_names


#print(code)

out = open("test.prolog", 'w')
out.write(code)
out.close()