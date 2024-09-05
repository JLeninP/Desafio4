import sys
import sympy as sp

B = sp.symbols('B', real = True)
H = sp.symbols('H', real = True)
S = sp.symbols('S', real = True)
n = sp.symbols('n', real = True)

Q = (B*H)**(5/3)*sp.sqrt(S)/(n*(B + 2*H)**(2/3)) #Funcion Q(B, H, S, n)

#Derivadas Parciales
dQ_dB = sp.diff(Q, B)
dQ_dH = sp.diff(Q, H)
dQ_dS = sp.diff(Q, S)
dQ_dn = sp.diff(Q, n)

#Entrada de Datos 
sys.stdout.write("\n\t-Ingresar valores separados por espacios (a b c).")
sys.stdout.write("\n\t-Usar punto para valores con decimales (0.1).")

#Imprimiendo funcion H(B, H, S, n)
# sp.pprint(H)

sys.stdout.write("\n\nIngresar B, H, S y n: ")
L: list[float] = list(map(float, sys.stdin.readline().split()))

sys.stdout.write("\nIngresar estimaciones de error de B, H, S y n: ")
eL: list[float] = list(map(float, sys.stdin.readline().split()))

Bi: float = L[0]
Hi: float = L[1]
Si: float = L[2]
ni: float = L[3]

eB = eL[0]
eH = eL[1]
eS = eL[2]
en = eL[3]
#Error estimado de H
eQ = dQ_dB*eB + dQ_dH*eH + dQ_dS*eS + dQ_dn*en

#Evaluando las funciones Q(B, H, S, n) y Delta_Q(B, H, S, n) en 
#los puntos Bi, Hi, Si, ni, eB, eH, eS, en. 
eQ_eval: float = sp.N(eQ.subs({B:Bi, H:Hi, S:Si, n:ni}))
Q_eval: float = sp.N(Q.subs({B:Bi, H:Hi, S:Si, n:ni}))

#Salida en Pantalla
sys.stdout.write('\n=============SOLUCIÓN=============')
sys.stdout.write(f'\nQ = {Q_eval}')
sys.stdout.write(f'\neQ = {eQ_eval}')
sys.stdout.write(f'\nQ - eQ = {Q_eval - eQ_eval}')
sys.stdout.write(f'\nQ + eQ = {Q_eval + eQ_eval}')
sys.stdout.write('\n===========FIN PROGRAMA===========\n')
