#!/usr/bin/python
import random
import itertools


# partners generation
# partners definition in format of tuple - (PartnerName, PartnerID, NumOfAgents)
partners = list()

for i in range(1,90) :
    partners.append(("Partner" + str(i), i, random.randint(2,3)))

#print(partners)


# rooms generation
# available rooms for meeting [RoomName, RoomID, Capacity], capacity define max num. of agents for one meeting
rooms = list()

for i in range(1,10) :
    rooms.append(("Room" + str(i), i, random.randint(3,5)))

#print(rooms)


# requests for meetings - in  format of arrays of partner ids, meeting id
req_meetings_list = list()
all_meetings = list()

for i in range(2,4) :
    all_meetings += list(itertools.combinations(range(1,90),i))

#print(all_meetings)

for i in range(1,550) :
    meeting = all_meetings[random.randint(0,len(all_meetings))]
    req_meetings_list.append((meeting))

print req_meetings_list

req_meetings = list()
counter = 0

for meeting in req_meetings_list:
    counter+=1
    req_meetings.append(meeting,counter)
    
#[([1,2],1),([2,3,4],2),([1,5],3),([4,5,6,7],4),([3,5],5),([4,6],6),([1,2,6,7],7),([5,6],8), ([1,5],9), ([2,3,4,5],10), ([2,5],11), ([2,4], 12), ([2,7], 13), ([2,8], 14) ]

# time blocks in which meeting can be arrange - 2 days - 14 time blocks each
time_blocks = 2*16



