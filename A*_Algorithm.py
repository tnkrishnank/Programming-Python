import igraph as ig
import copy

import matplotlib.pyplot as plt
from PIL import Image

def visualize():
    G.es['weight'] = cost
    G.es['label'] = cost
    visual_style = {}
    visual_style["bbox"] = (800, 800)
    visual_style["margin"] = 100
    visual_style["vertex_color"] = 'green'
    visual_style["vertex_size"] = 60
    visual_style["vertex_label_size"] = 30
    visual_style["edge_curved"] = False
    visual_style["layout"] = G.layout_sugiyama()
    ig.plot(G, "Graph.png", **visual_style)

    img = Image.open(r"Graph.png")
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    
def name_id():
    print()
    for i in range(len(G.vs)):
        print("VERTEX ID : ", G.vs[i]["id"], "VERTEX NAME : ", G.vs[i]["label"])

def check(goal):
    if goal == 1:
        print("GOAL STATE REACHED !")
    else:
        print("GOAL STATE NOT REACHED !")

def A_STAR(s, g):
    global goal
    q = []
    q.append([[s], h[s]])
    while len(q) != 0:
        print("TRAVERSING", q)
        qt = {}
        for i in q:
            if g in i[0]:
                qt[q.index(i)] = i
        for i in qt.keys():
            q.pop(i)
        minval = min(q, key=lambda x: x[1])
        index = q.index(minval)
        temp = q[index]
        q.pop(index)
        for i in qt.keys():
            q.insert(i, qt[i])
        for i in range(n):
            sel = copy.deepcopy(temp)
            if a[sel[0][-1]][i] > 0 and (i not in sel[0]):
                sel[0].append(i)
                dist = 0
                for j in range(len(sel[0])-1):
                    dist += a[sel[0][j]][sel[0][j+1]]
                dist += h[sel[0][-1]]
                sel[1] = dist
                p = 0
                for k in q:
                    if (sel[0][-1] in k[0]) and (k[1] <= sel[1]):
                        p = 1
                if p == 0:
                    for k in q:
                        if (k[0][-1] in sel[0]) and (sel[1] <= k[1]):
                            q.pop(q.index(k))
                if p == 0:
                    q.append(sel)
        j = 0
        for i in q:
            if g in i[0]:
                j += 1
        if j == len(q):
            break
    if len(q) > 0:
        goal = 1
    print("TRAVERSING", q)

G = ig.Graph(directed=False)
n = int(input("ENTER NUMBER OF VERTICES : "))
print()
G.add_vertices(n)
h = {}
a = []

for i in range(n):
    a.append([0]*n)

for i in range(len(G.vs)):
    G.vs[i]["id"] = i
    G.vs[i]["label"] = input("ENTER VERTEX " + str(i+1) + " NAME            : ")
    h[i] = int(input("ENTER VERTEX " +  str(i+1) + " HEURISTIC VALUE : "))

name_id()
graph = []
cost = []

while True:
    print()
    print("ENTER AN EDGE")
    print("ENTER NEGATIVE INTEGER TO STOP GETTING INPUTS")
    x = int(input("START : "))
    y = int(input("END   : "))
    c = int(input("COST  : "))
    if x > n or y > n:
        print()
        print("INVALID START OR END !")
    if x < 0 or y < 0:
        break
    t = (x, y)
    a[x][y] = c
    a[y][x] = c
    graph.append(t)
    cost.append(c)

"""
graph = [(0, 1), (0, 2), (0, 3), (1, 5), (2, 4), (2, 5), (3, 4), (4, 6), (5, 6), (6, 7)]
cost = [6, 5, 10, 6, 7, 6, 6, 6, 4, 3]
j = 0
for i in graph:
    a[i[0]][i[1]] = cost[j]
    a[i[1]][i[0]] = cost[j]
    j += 1
h = {0: 17, 1: 10, 2: 13, 3: 4, 4: 2, 5: 4, 6: 1, 7: 0}
"""

G.add_edges(graph)
print()
s = int(input("ENTER START STATE : "))
g = int(input("ENTER GOAL STATE  : "))
print()
if s < 0 or s > n-1 or g < 0 or g > n-1:
    print("INVALID START OR GOAL STATE !")
    exit(0)

goal = 0
print("A* ALGORITHM")
print()
A_STAR(s, g)
check(goal)
print()

visualize()
