import igraph as ig

import matplotlib.pyplot as plt
from PIL import Image

def visualize():
    visual_style = {}
    visual_style["bbox"] = (800, 800)
    visual_style["margin"] = 100
    visual_style["vertex_color"] = 'green'
    visual_style["vertex_size"] = 60
    visual_style["vertex_label_size"] = 30
    visual_style["edge_curved"] = False
    visual_style["edge_width"] = [1 + 4 * int(sel) for sel in G.es["sel"]]
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

def HC(s, g):
    global goal
    sel = s
    while True:
        q = []
        for i in range(n):
            if a[sel][i] > 0:
                q.append(i)
        val = [h[x] for x in q]
        minval = min(val)
        index = val.index(minval)
        if q[index] == g:
            goal = 1
            break
        if minval < h[sel]:
            v.append(q[index])
            print("TRAVERSING", q[index])
            sel = q[index]
        else:
            break

G = ig.Graph(directed=False)
n = int(input("ENTER NUMBER OF VERTICES : "))
print()
G.add_vertices(n)
h = {}
loc = {}

for i in range(len(G.vs)):
    G.vs[i]["id"] = i
    G.vs[i]["label"] = input("ENTER VERTEX " + str(i+1) + " NAME            : ")
    x = int(input("X CO-ORDINATE OF VERTEX " + str(i+1) + "      : "))
    y = int(input("Y CO-ORDINATE OF VERTEX " + str(i+1) + "      : "))
    loc[i] = (x, y)

name_id()
graph = []

while True:
    print()
    print("ENTER AN EDGE")
    print("ENTER NEGATIVE INTEGER TO STOP GETTING INPUTS")
    x = int(input("START : "))
    y = int(input("END   : "))
    if x > n or y > n:
        print()
        print("INVALID START OR END !")
    if x < 0 or y < 0:
        break
    t = (x, y)
    graph.append(t)

#loc = [(1, 2), (2, 3), (2, 4), (2, 2), (1, 4), (3, 4), (3, 2), (4, 4), (3, 3), (3, 1)]
#graph = [(0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 9), (5, 7), (5, 8), (6, 8), (8, 9)]
#loc = [(1, 2), (1, 3), (2, 4), (2, 3), (2, 2), (3, 2), (3, 1), (4, 4), (4, 2)]
#graph = [(0, 1), (1, 3), (2, 3), (2, 5), (3, 4), (4, 6), (5, 8), (6, 8), (7, 8)]

G.add_edges(graph)
print()
s = int(input("ENTER START STATE : "))
g = int(input("ENTER GOAL STATE  : "))
print()
if s < 0 or s > n-1 or g < 0 or g > n-1:
    print("INVALID START OR GOAL STATE !")
    exit(0)
a = G.get_adjacency()

for i in range(len(G.vs)):
    h[i] = abs(loc[i][0]-loc[g][0]) + abs(loc[i][1]-loc[g][1])

v = []
goal = 0
print("HILL CLIMBING ALGORITHM")
print()
HC(s, g)
check(goal)
p = [(s, v[0])]
for i in range(len(v)-1):
    p.append((v[i], v[i+1]))
p.append((v[len(v)-1], g))
c = []
for i in graph:
    if i in p:
        c.append(True)
    else:
        c.append(False)
G.es['sel'] = c
print()

visualize()
