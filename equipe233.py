import math
from pointfixe import pointfixe

def g1(Q):
    return math.log(-Q/2 +5)

def g2(Q):
    return 10-2*math.exp(Q)

Q0 = 1
tolr = 1e-8
nmax_g1 = 150
nmax_g2 = 5

resultats_g1 = pointfixe(g1, Q0, tolr, nmax_g1)

resultats_g2 = pointfixe(g2, Q0, tolr, nmax_g2)