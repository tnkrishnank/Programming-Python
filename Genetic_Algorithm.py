import copy

#FUNCTIONS
def normalize(bval):
    return rmin + (((rmax - rmin) / ((2 ** nbit) - 1)) * bval)

def obj_fn(x, y):
    return (((x ** 2) + y - 11) ** 2) + ((x + (y ** 2) - 7) ** 2)

def fitness_fn(val):
    return 1 / (1 + val)

def nearest_val(cp, val):
    c = []
    for i in cp:
        c.append(float(format(abs(i-val), ".3f")))
    return c.index(min(c))

def crossover(x, y, r):
    if r > cprob:
        s1 = x1[x] + x2[x]
        s2 = x1[y] + x2[y]
        temp = s1[csite:]
        s1 = s1[:csite] + s2[csite:]
        s2 = s2[:csite] + temp
        x1_alt.append(s1[:len(s1)//2])
        x1_alt.append(s2[:len(s2)//2])
        x2_alt.append(s1[len(s1)//2:])
        x2_alt.append(s2[len(s2)//2:])

def mutation(val, r):
    if r > mprob:
        s = x1[val] + x2[val]
        if s[msite] == "0":
            s = s[:msite-1] + "1" + s[msite:]
        else:
            s = s[:msite-1] + "0" + s[msite:]
        x1_alt.append(s[:len(s)//2])
        x2_alt.append(s[len(s)//2:])

#VARIABLES ASSIGNMENT
nsample = 5
nbit = 10
rmin = 0
rmax = 6
cprob = 0.8
mprob = 0.05
csite = 11
msite = 10
x1 = ['1100100000', '0011100111', '0111001000', '1000010100', '1011100011']
x2 = ['1110010000', '0001001101', '1010100001', '1001000110', '1100011000']
rn = [0.472, 0.108, 0.723, 0.972, 0.363, 0.723, 0.429, 0.01]
x1_alt = []
x2_alt = []

print(x1)
print(x2)
print()

g = 0
while (x1 != x1_alt or x2 != x2_alt):
    if g > 0:
        x1.clear()
        x2.clear()
        x1 = copy.deepcopy(x1_alt)
        x2 = copy.deepcopy(x2_alt)
    g = 1

    #CALCULATING DECIMAL FROM BINARY STRNIG
    x1n = []
    for i in x1:
        x1n.append(int(i, 2))

    x2n = []
    for i in x2:
        x2n.append(int(i, 2))

    #NORMALIZING THE DECIMAL VALUES
    x_1 = []
    for i in x1n:
        x_1.append(float(format(normalize(i), ".3f")))

    x_2 = []
    for i in x2n:
        x_2.append(float(format(normalize(i), ".3f")))

    #CALCULATING f(x) VALUES
    f = []
    for i in range(nsample):
        f.append(float(format(obj_fn(x_1[i], x_2[i]), ".3f")))

    #CALCULATING FITNESS VALUES
    fitness = []
    for i in f:
        fitness.append(float(format(fitness_fn(i), ".3f")))

    #CALCULATING PROBABILITIES
    sum_fitness = sum(fitness)
    p = []
    for i in fitness:
        p.append(float(format((i / sum_fitness), ".3f")))

    #CALCULATING CUMULATIVE PROBABILITY
    s = 0
    cp = []
    for i in p:
        s = float(format((s + i), ".3f"))
        cp.append(s)

    #FINDING CLOSEST VALUE
    nval = []
    for i in range(nsample):
        nval.append(nearest_val(cp, rn[i]))

    #CROSSOVER AND MUTATION
    x1_alt.clear()
    x2_alt.clear()
    if nsample % 2 == 0:
        t = nsample
    else:
        t = nsample - 1
    for r in range(nsample, len(rn)):
        for j in range(len(nval)):
            for k in range(j+1, len(nval)):
                if len(x1_alt) < t:
                    crossover(nval[j], nval[k], r)
                else:
                    break
    for r in range(nsample, len(rn)):
        for j in range(len(nval)):
            if len(x1_alt) < nsample:
                mutation(nval[j], r)
            else:
                break

    print(x1_alt)
    print(x2_alt)
    print()