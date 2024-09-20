print("Act 9 v2")
print("Daniela López Mat:22308051281240")
# zona de class
class Operadores1240:
    # zona de funciones
    def suma1240(self,D,L):
        s1240=D+L
        print(f"La suma de {D} + {L} = {s1240}")

    def resta1240(self,D,L):
        r1240=D-L
        print(f"La resta de {D} - {L} = {r1240}")

    def mult1240(self,D,L):
        m1240=D*L
        print(f"La multiplicacion de {D} * {L} = {m1240}")

    def div1240(self,D,L):
        d1240=D/L
        print(f"La división de {D} / {L} = {d1240}")

    def modulo1240(self,D,L):
        mo1240=D%L
        print(f"El módulo de {D} % {L} = {mo1240}")

    def exp1240(self,D,L):
        e1240=D**L
        print(f"El exponente de {D} ** {L} = {e1240}")

    def co1240(self,D,L):
        c1240=D//L
        print(f"El cociente de {D} // {L} = {c1240}")



# zona de creacion del objeto
operadani=Operadores1240()

# zona de uso de objetos
print(" - Funcion suma")
operadani.suma1240(5,5)

print(" - Funcion resta")
operadani.resta1240(10,5)

print(" - Funcion multiplicacion")
operadani.mult1240(3,6)

print(" - Funcion división")
operadani.div1240(20,5)

print(" - Funcion módulo")
operadani.modulo1240(7,4)

print(" - Funcion exponente")
operadani.exp1240(2,5)

print(" - Funcion cociente")
operadani.co1240(8,4)