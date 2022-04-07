# rewards are based on the rewards found during the episodes
reward= { 
    "A": {"A":0, "B":1, "C": 0, "D":0, "E": 0, "F":0,"G":0, "H":1},
    "B": {"A":1, "B":0, "C": -10, "D":0, "E": 0, "F":0,"G":0, "H":0},
    "C": {"A":0, "B":0, "C": 0, "D":-10, "E": 0, "F":0,"G":0, "H":0},
    "D": {"A":0, "B":0, "C": 0, "D":0, "E": 50, "F":0,"G":0, "H":0},
    "E": {"A":0, "B":0, "C": 0, "D":0, "E": 0, "F":0,"G":0, "H":0},
    "F": {"A":0, "B":0, "C": 0, "D":0, "E": 1, "F":0,"G":1, "H":0},
    "G": {"A":0, "B":0, "C": 0, "D":0, "E": 0, "F":1,"G":0, "H":1},
    "H": {"A":1, "B":0, "C": 0, "D":0, "E": 0, "F":0,"G":1, "H":0}
}

# the actions taken from each state during the episodes, represented by "s":["s1'","s2'"]
actions={
    "A": ["B", "H"],
    "B": ["A", "C"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
    "F": ["E","G"],
    "G": ["F", "H"],
    "H": ["A", "G"]
}

# initial Q values set to 0 for every state/action pair found during the episodes
QA = {
    "A": {"B": 0, "H":0},
    "B": {"A": 0, "C": 0},
    "C": {"D":0},
    "D": {"E":0},
    "E": {},
    "F": {"E":0,"G":0},
    "G": {"F":0, "H":0},
    "H": {"A":0, "G":0}
}

# to find the new Q value of a state as each step in each episode happens
def Q(rewards, qas, state, action, discount, alpha, actions):
    maxqa = Qsample(rewards, qas, state, action, discount,actions)
    currentqa = qas[state][action]
    result = (1-alpha)*currentqa + alpha*maxqa
    return result

# to find the Qsample(s, a) value
def Qsample(rewards, qas, state, action, discount,actions):
    possibleQA = actions[action]
    reward = rewards[state][action]
    if len(possibleQA) == 2:
        return reward + discount*max(qas[action][possibleQA[0]],qas[action][possibleQA[1]])
    elif len(possibleQA) == 1:
        return reward + discount*qas[action][possibleQA[0]]
    elif len(possibleQA)==0:
        return reward

# to print the Q(s, a) values more neatly
def printQAs(QA):
    print("A:\tright: "+str(QA["A"]["B"])+"\n\tdown: "+str(QA["A"]["H"]))
    print("B:\tleft: "+str(QA["B"]["A"])+"\n\tright: "+str(QA["B"]["C"]))
    print("C:\tdown: "+str(QA["C"]["D"]))
    print("D:\tdown: "+str(QA["D"]["E"]))
    print("E:\t[no actions]")
    print("F:\tright: "+str(QA["F"]["E"])+"\n\tleft: "+str(QA["F"]["G"]))
    print("G:\tright: "+str(QA["G"]["F"])+"\n\tup: "+str(QA["G"]["H"]))
    print("H:\tdown: "+str(QA["H"]["G"])+"\n\tup: "+str(QA["H"]["A"]))

# set up discount factor and alpha, then run the sequence E1, E2, E3, E4 a set number of times, 
# printing the results at appropriate intervals. Comments including the variable 'ep' allow for the user 
# to run the episodes in any order they would like, as many times as they would like. 
def main(rewards, actions, QA):
    # print("Select an episode to run: \n1: episode 1\n2: episode 2\n3: episode 3\n4: episode 4\n5: exit")
    # ep = input("Selection: ")
    discount = 1
    alpha = .5
    loopcount=1
    # while ep != "5":
    while loopcount <= 50000:
        # if ep == "1":
            QA["A"]["B"]=Q(rewards, QA, "A","B",discount, alpha,actions)
            QA["B"]["C"]=Q(rewards, QA, "B","C",discount, alpha,actions)
            QA["C"]["D"]=Q(rewards, QA, "C","D",discount, alpha,actions)
            QA["D"]["E"]=Q(rewards, QA, "D","E",discount, alpha,actions)
        # elif ep == "2":
            QA["A"]["B"]=Q(rewards, QA, "A","B",discount, alpha,actions)
            QA["B"]["A"]=Q(rewards, QA, "B","A",discount, alpha,actions)
            QA["A"]["B"]=Q(rewards, QA, "A","B",discount, alpha,actions)
            QA["B"]["C"]=Q(rewards, QA, "B","C",discount, alpha,actions)
            QA["C"]["D"]=Q(rewards, QA, "C","D",discount, alpha,actions)
            QA["D"]["E"]=Q(rewards, QA, "D","E",discount, alpha,actions)
        # elif ep == "3":
            QA["A"]["H"]=Q(rewards, QA, "A","H",discount, alpha,actions)
            QA["H"]["G"]=Q(rewards, QA, "H","G",discount, alpha,actions)
            QA["G"]["F"]=Q(rewards, QA, "G","F",discount, alpha,actions)
            QA["F"]["E"]=Q(rewards, QA, "F","E",discount, alpha,actions)
        # elif ep == "4":
            QA["A"]["H"]=Q(rewards, QA, "A","H",discount, alpha,actions)
            QA["H"]["A"]=Q(rewards, QA, "H","A",discount, alpha,actions)
            QA["A"]["H"]=Q(rewards, QA, "A","H",discount, alpha,actions)
            QA["H"]["G"]=Q(rewards, QA, "H","G",discount, alpha,actions)
            QA["G"]["H"]=Q(rewards, QA, "G","H",discount, alpha,actions)
            QA["H"]["G"]=Q(rewards, QA, "H","G",discount, alpha,actions)
            QA["G"]["F"]=Q(rewards, QA, "G","F",discount, alpha,actions)
            QA["F"]["G"]=Q(rewards, QA, "F","G",discount, alpha,actions)
            QA["G"]["F"]=Q(rewards, QA, "G","F",discount, alpha,actions)
            QA["F"]["E"]=Q(rewards, QA, "F","E",discount, alpha,actions)

            if loopcount%10000 == 0:
                print("============== round "+str(loopcount)+" ==============")
                printQAs(QA)
                print("\n======================================\n\n")
        # print("============== episode "+ep+", round "+str(loopcount)+" ==============")
        # printQAs(QA)
        # print("\n================================================\n\n")
        # if ep == "4":
            loopcount+=1
        # print("Select an episode to run: \n1: episode 1\n2: episode 2\n3: episode 3\n4: episode 4\n5: exit")
        # ep = input("Selection: ")

main(reward, actions, QA);
