:- use_module(library(clpfd)).
% partner(IdPartner , Persons)
% IdPartner - Integer that represents exactly one partner
% Agents   - Number of agents that partner contains
partner(1,3).
partner(2,1).
partner(3,5).
partner(4,2).

% room(IdRoom , Capacity)
% IdPartner - Integer that represents exactly one room
% Capacity   - Capacity of the room
room(1,2).
room(2,5).


% request(Partners) - request to hold meeting between partners
% Partners - list of partners Id
request([1,2]).
request([1,3,4]).
request([3,2]).

% meeting(PartnerIds , Time, Room)
%meeting([1,2,3],2).
%meeting(X,Time) :-
%meeting(Partners,Time,Room) :-
%    request(Partners),
%    room(Room,RoomSize),
%    persons_count(Partners,RoomSize).
meeting(Partners,_,Room) :-
    request(Partners),
    room(Room,RoomSize),
    persons_count(Partners,Count),
    RoomSize >= Count.


partners([]).
partners([P|Rest]) :-
    partner(P,_),
    not_member(P,Rest),
    partners(Rest).

not_member(_,[]).
not_member(Tested,[First|Tail]) :-
    Tested \= First,
    not_member(Tested,Tail).

persons_count([],0).
persons_count([_|Rest],Count) :-
    persons_count(Rest,PartResult),
    Count is PartResult+1.

:- Times = [A1,B,C], Times ins 1..2,
   Places = [X,Y,Z], Places ins 1..2,
   meeting([1,2], A1, X), meeting([1,3,4], B, Y), meeting([3,2], C, Z),
   (A1 #= B) #==> X #\= Y, A1 #= C #==> X #\= Z, C #= B #==> Z #\= Y,
   labeling([down], Places), labeling([down], Times),
   write('Times'),write(Times),write(' Rooms'),write(Places).



