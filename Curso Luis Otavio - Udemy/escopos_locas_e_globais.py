# -*- coding: utf-8 -*-
"""
*Curso Luiz Otavio - Udemy 
Aulas: 108,

-Escopo de funções

"""

#O escopo global é o escopo onde todo código é alcaçavel
#O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

x = 1

def escopo():
    x = 10
    print(x)
    #esse x é uma nova variavel
    def outra_funcao():
        y = 20
        print(x,y)
    outra_funcao() #essa função só existe dentro da "função pai"
            
escopo()
#vai printar o x de dentro da função
print(x) #vai printar o x de fora da função


"""
Podemos chamar a variavel global:
    *porem é uma má pratica
"""

y = 5

def chama_varivavel_global():
        global y 
        y = 50
        print(y)
        
print(y) #imprime 5
chama_varivavel_global() #imprime 50