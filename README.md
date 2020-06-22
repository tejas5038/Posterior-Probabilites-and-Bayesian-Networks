# Posterior-Probabilites-and-Bayesian-Networks
Implemented Bayesian Network and Posterior Probabilities on data


Programming language :- python

code structure :- 

Task 1:-
structure divided in below parts:-
1) iterate through string and indetify C or L
 compute Pi and Q for every character

2) using previous value compute Pi and Q for next event and stored required data in file untill last character of string. 

example of command line argument :- python compute_a_posteriori.py CCCL

Task 2:-
structure divided in below parts:-
1) contain class bayesian network 
	- conatains computeProbability(b,e,a,j,m) function 
		--> it will compute joit probability 

2) Contains portion that read from command line argument and convert it into event True or False value 


3) Add all remaining event's possible combinations using recursive calls and compute joint probability 


example of command line argument :- python bnet.py Bt Af Et

