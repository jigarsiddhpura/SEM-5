Female(nami).
female(robin).
female(otama).
female(hancock).
male(luffy).
male(zoro).
male(sanji).
male(ace).
parent(nami,zoro).
parent(sanji,zoro).
parent(sanji,lizza).
parent(zoro,hancock).
parent(zoro,otama).
parent(otama,jimmy).
parent(zoro,ace).
parent(ace,jimmy).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.

