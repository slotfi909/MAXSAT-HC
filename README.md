# MAXSAT-HC
a hill-climbing approach to the MAXSAT problem

## what is MAXSAT?
In computational complexity theory, the maximum satisfiability problem (MAX-SAT) is the problem of determining the maximum number of clauses, of a given Boolean formula in conjunctive normal form(CNF), that can be made true by an assignment of truth values to the variables of the formula. It is a generalization of the Boolean satisfiability problem, which asks whether there exists a truth assignment that makes all clauses true.[wikipedia](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem)

## hill climbing
In numerical analysis, hill climbing is a mathematical optimization technique which belongs to the family of local search. It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by making an incremental change to the solution. If the change produces a better solution, another incremental change is made to the new solution, and so on until no further improvements can be found. <br>
<br>
![image](https://github.com/slotfi909/MAXSAT-HC/assets/82094903/a510d732-feda-4954-bdd3-631d3d505ca3)


## input
the input has to be in [DIMACS CNF](https://jix.github.io/varisat/manual/0.2.0/formats/dimacs.html) form for the algorithm to work properly.

example: [input](https://github.com/slotfi909/MAXSAT-HC/blob/main/Max-Sat_20_80.txt)

## states and neighbors
- ### states
  each state is described using a binary string in length of number of variables, so that the ith character of the string, sets the value of ith variable.<br>
  for example, if we have 10 variable for an instance, one of the states can be described by the following string: 1011011110<br>
  which means:<br>
  first variable's value = 1,<br>
  second variable's value = 0,<br>
  third variable's value = 1,<br>
  fourth variable's value = 1,<br>
  so forth...<br>
- ### neighbors
  each neighboring has to differ from the current state by only <b>1 bit</b>. <br>
  so if our currenct state is the one from the example before, it's neighboring state will be: <br>
  <b>0</b>011011110 - 1<b>1</b>11011110 - 10<b>0</b>1011110 - 101<b>0</b>011110 - ....

##
