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
meeting(Partners,Time,Room) :-
    request(Partners),
    room(Room,X),
    persons_count(Partners,X).



partners([]).
partners([P|Rest]) :-
    partner(P,_),
    not_member(P,Rest),
    partners(Rest).

not_member(_,[]).
not_member(Z,[X|Tail]) :-
    Z \= X,
    not_member(Z,Tail).

persons_count([],0).
persons_count([_|Rest],Count) :-
    persons_count(Rest,Y),
    Count is Y+1.

