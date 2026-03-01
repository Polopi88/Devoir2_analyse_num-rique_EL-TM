import math
from pointfixe import pointfixe

from bissection import Bissection

def f_tomates(Q):

    return math.exp(Q) + Q**2 - 5


#pour la question c)

def main():
    print("--- Question c) Validation numérique ---")
    
    x_debut = 1.0
    x_fin = 2.0
    tolerance = 0.5e-4 
    
    n_max = 50 

    resultats = Bissection(f_tomates, x_debut, x_fin, tolerance, n_max)

    if resultats:

        Q_n = resultats[-1]
        
        if len(resultats) > 1:
            Q_avant = resultats[-2]
            erreur_estimee = abs(Q_n - Q_avant)
        else:
            erreur_estimee = 0

        print(f"\n>>> RÉSULTATS À COPIER DANS LE RAPPORT <<<")
        print(f"Nombre d'itérations effectuées : {len(resultats) - 1}") 
        print(f"Valeur approximée Qn : {Q_n:.6f}")
        print(f"Erreur estimée (|Qn - Qn-1|) : {erreur_estimee:.6e}")
        print(f"Tolérance demandée : {tolerance:.6e}")

if __name__ == "__main__":
    main()

# fin pour question c)

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