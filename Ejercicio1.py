import sys
import sympy as sp

x: object = sp.symbols('x', real = True)

a: float = sp.S(25)
b: float = sp.S(6)
c: float = sp.S(7)
d: float = sp.S(88)

f: object = a*x**3 - b*x**2 + c*x - d

#Entrada de Datos 
sys.stdout.write("\n\t-Ingresar valores separados por espacios (a b c).")
sys.stdout.write("\n\t-Usar punto para valores con decimales (0.1).")
sys.stdout.write("\n\nIngresar x0, x1 y n(orden de aproximación): ")

L: list[float] = list(map(float, sys.stdin.readline().split()))

x0: float = L[0]
x1: float = L[1]
n: int = int(L[2]) + 1#Sumado 1 porque python no toma el ultimo valor del rango
h: float = x1 - x0

vR: float = f.subs({x:x1}) #Valor Real
fi = f
sys.stdout.write(f"\n\tValor Real = {vR}\n")
sys.stdout.write(F'\nORDEN\tt0\tt1\th\tq(t1) Aproximado\teR (%)')
for i in range(n):
    f_prima = sp.diff(f, x, i + 1)
    
    Rn = f_prima * h**(i + 1) / sp.factorial(i + 1)
    vA = sp.N(fi.subs({x:x0})) #Valor Aprocimado
    eRp = abs((vR - vA)/vR * 100) #Error relativo porcentual
    sys.stdout.write(F'\n{i}\t{x0}\t{x1}\t{h}\t{vA}\t{eRp}')
    fi += Rn

sys.stdout.write('\n--------------------Fin de programa--------------------\n')