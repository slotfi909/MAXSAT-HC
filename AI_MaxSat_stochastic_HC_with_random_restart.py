#with random restart

import random
from random import *

def test():
    # thisList=[4]
    # tmp=thisList.pop()
    # print(2)
        pass
def fitness(Mylist,val_list):
    local_max=0
    local_or = 0
    for i3 in range(len(Mylist)):
        if Mylist[i3] != 0:  # while the clause hasn't ended
            local_or = local_or | val_list[
                i3]  # local_or is either satisfied or must be satisfied by other variables in the clause
        elif Mylist[i3] == 0:  # if clause ended ....
            if local_or == 1:  # and clause is satisfied...
                local_max += 1  # add 1 to local max
            local_or = 0
    return local_max


def bitFlip(variables_dict, i):
    temp_variables_dict=variables_dict.copy()
    if temp_variables_dict[i]=={0}:
        temp_variables_dict[i]={1}
    else: temp_variables_dict[i] = {0}
    return temp_variables_dict

def variablesDictToValList(Mylist,variables_dict):
    temp_val=[]
    temp_list=[]
    val_list=[]
    temp_val.append(2)
    for i in Mylist:
        if i != 0:  # if the clause hasn't ended...
            temp_list.append(list(variables_dict[abs(i)]))  # adding the abs values of the input
        elif i == 0:
            temp_list.append(list(temp_val))  # adding 2 whenever we hit End Of Line
    for i in temp_list:
        val_list += i  # removing the inside lists
    for i1 in range(0, len(Mylist)):  # changing the variables whenever we see a negative input
        if Mylist[i1] < 0:
            if val_list[i1] == 0:
                val_list[i1] = 1
            else:
                val_list[i1] = 0
    return val_list

def main():
    final_dict = {}
    final_dict_res = {}
    temp_list = []
    temp_val = []
    file = open("Max-Sat_20_80.txt", "r")
    c = file.read()
    c = c.replace("\n", " ")
    # print(c[0])
    Mylist = c.split(" ")
    for i in Mylist:
        if i == '':
            Mylist.remove(i)
    del c
    NumberOfVar = Mylist.pop(0)
    NumberOfCl = Mylist.pop(0)
    for i in range(0, len(Mylist)): #turning characters to integers
        Mylist[i] = int(Mylist[i])
    val_list = []
    variables_dict = {}
    copy_variables_dict = {}
    # ****************************************
    variables_dict.clear()
    copy_variables_dict.clear()
    temp_list.clear()
    temp_val.clear()
    val_list.clear()
    global_max=0

    #get number of random restarts
    print("enter number of random restarts:")
    num_random_restart=int(input())

    for k in range(num_random_restart): #random restart
        for i in range(int(NumberOfVar)):
            variables_dict[i + 1] = {randint(0, 1)}  #giving random values to variables
        copy_variables_dict = variables_dict     #copying the values
        temp_val.append(2)
        for i in Mylist:
            if i != 0: #if the clause hasn't ended...
                temp_list.append(list(variables_dict[abs(i)]))  #adding the abs values of the input
            elif i == 0:
                temp_list.append(list(temp_val))  #adding 2 whenever we hit End Of Line
        for i in temp_list:
            val_list += i           #removing the inside lists
        for i1 in range(0, len(Mylist)):  #changing the variables whenever we see a negative input
            if Mylist[i1] < 0:
                if val_list[i1] == 0:
                    val_list[i1] = 1
                else:
                    val_list[i1] = 0

        currentFitness=fitness(Mylist,val_list)
        # print(f"first fitness={currentFitness}")
        bestFitness=0
        for i2 in range(10000):
            sumOfFitnesses=0
            listOfFitnessOfNeighbors = []
            for i in range(int(NumberOfVar)):
                temp_variables_dict=bitFlip(copy_variables_dict,i+1)
                temp_val_list=variablesDictToValList(Mylist,temp_variables_dict)
                temp_Fitness=fitness(Mylist,temp_val_list)
                listOfFitnessOfNeighbors.append(temp_Fitness)
                if currentFitness < temp_Fitness:
                    sumOfFitnesses+=temp_Fitness #for calculating the chance for stochastic HC
                if temp_Fitness > bestFitness:
                    bestFitness=currentFitness
                    final_dict=temp_variables_dict
            tempNumber=0
            neighborsChance=[]
            for i in listOfFitnessOfNeighbors:
                if currentFitness<i:
                    neighborsChance.append(i/sumOfFitnesses)
                    tempNumber+=i/sumOfFitnesses
                else: neighborsChance.append(0)


            #choosing a new state based on stochastic HC
            allChancesAreZero=True
            for j in neighborsChance:
                if j!=0:
                    allChancesAreZero=False
                    break
            if allChancesAreZero:
                # print(f"after {i}runs, stuck in a local maximum")
                # print(bestFitness)
                # print(final_dict)
                # exit(0)
                break

            population=list(range(int(NumberOfVar)))
            res=choices(population=population,weights=neighborsChance,k=1)
            temp_variables_dict= bitFlip(copy_variables_dict, res.pop() + 1)
            temp_val_list = variablesDictToValList(Mylist,temp_variables_dict)
            currentFitness=fitness(Mylist,temp_val_list)
            variables_dict=temp_variables_dict
            val_list=variablesDictToValList(Mylist,variables_dict)
    if bestFitness > global_max:
        global_max=bestFitness
        final_dict_with_random_restart=variables_dict
        # print(bestFitness)
        # print(final_dict)
    print(f'global_max={global_max}')
    print(variables_dict)



test()
main()
