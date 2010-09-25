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

% meeting(PartnerIds , Time)
%meeting([1,2,3],2).
%meeting(X,Time) :-

partners([]).
partners([P|Rest]) :-
    partner(P,_),
    not_member(P,Rest),
    partners(Rest).

not_member(_,[]).
not_member(Z,[X|Tail]) :-
    Z \= X,
    not_member(Z,Tail).
    

