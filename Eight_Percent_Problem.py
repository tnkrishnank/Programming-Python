import copy
from sys import exit

def check(goal):
    if goal == 1:
        print("GOAL STATE REACHED !")
    else:
        print("GOAL STATE NOT REACHED !")

def eight_percent(s, g, pos):
    global goal
    if g not in visited:
        visited.append(s)
        l = []
        if pos == 1:
            l = [2, 4]
        elif pos == 2:
            l = [1, 3, 5]
        elif pos == 3:
            l = [2, 6]
        elif pos == 4:
            l = [1, 5, 7]
        elif pos == 5:
            l = [2, 4, 6, 8]
        elif pos == 6:
            l = [3, 5, 9]
        elif pos == 7:
            l = [4, 8]
        elif pos == 8:
            l = [5, 7, 9]
        elif pos == 9:
            l = [6, 8]
        else:
            pass
        for i in l:
            temp_list = copy.deepcopy(s)
            temp_list[pos-1] = temp_list[i-1]
            temp_list[i-1] = -1
            if temp_list not in visited:
                print(temp_list)
                if temp_list == g:
                    goal = 1
                    visited.append(temp_list)
                    print("GOAL STATE REACHED !")
                    exit()
                else:
                    eight_percent(temp_list, g, i)

s = []
#s = [5, 6, 7, 1, 4, 8, 2, 3, -1]
print("ENTER INITIAL MATRIX")
for i in range(9):
    s.append(int(input("ENTER ELEMENT " + str(i) + " : ")))

print()

g = []
#g = [-1, 5, 6, 1, 4, 7, 2, 3, 8]
print("ENTER FINAL MATRIX")
for i in range(9):
    g.append(int(input("ENTER ELEMENT " + str(i) + " : ")))

goal = 0
visited = []
print("EIGHT PERCENT PROBLEM")
print()
eight_percent(s, g, s.index(-1)+1)
check(goal)
print()
