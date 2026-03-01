import time
import math

def pointfixe(g, Q0, tolr, nmax):
    X = [0] * (nmax + 1)
    x_actuel = Q0

    for i in range(nmax + 1):
        if i == 0:
            print(f'{i} Qn = {x_actuel:E}')
            time.sleep(0.5)
            X[i] = x_actuel

        elif i == 1:
            x_precedent = X[i-1]
            x_actuel = g(x_precedent)
            
            err_abs = abs(x_actuel - x_precedent)
            
            if x_actuel != 0:
                err_rel = err_abs / abs(x_actuel)
            else:
                err_rel = err_abs

            print(f'{i} Qn = {x_actuel:E}, |en| = {err_abs:E}')
            time.sleep(0.5)
            X[i] = x_actuel

            if err_rel < tolr:
                print('La méthode du point fixe a convergé!')
                return X[:i+1]

        else:
            x_precedent = X[i-1]
            x_avant_precedent = X[i-2]
            x_actuel = g(x_precedent)

            err_abs = abs(x_actuel - x_precedent)
            err_prev = abs(x_precedent - x_avant_precedent)
            
            if x_actuel != 0:
                err_rel = err_abs / abs(x_actuel)
            else:
                err_rel = err_abs

            if err_prev != 0:
                ratio1 = err_abs / err_prev
                ratio2 = err_abs / (err_prev ** 2)
            else:
                ratio1 = 0
                ratio2 = 0

            print(f'{i} Qn = {x_actuel:E}, |en| = {err_abs:E}, Ratio1 = {ratio1:E}, Ratio2 = {ratio2:E}')
            time.sleep(0.5)
            X[i] = x_actuel

            if err_rel < tolr:
                print('La méthode du point fixe a convergé!')
                return X[:i+1]
            
            if math.isinf(x_actuel) or math.isnan(x_actuel):
                print('La méthode diverge.')
                return X[:i+1]

    print('La méthode du point fixe n\'a pas convergé...')
    return X