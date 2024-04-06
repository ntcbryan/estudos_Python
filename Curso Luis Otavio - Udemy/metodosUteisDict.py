"""
Manipulando chaves e valores de um dicionario aula Luiz otavio


"""

pessoa = {
    'nome': 'Bryan',
    'sobrenome': 'Rodrigues',
    'idade': 20,
    'endereços': [
            {'rua': 'rua tal', 'numero': 123},
            {'rua': 'rua tal tal', 'numero': 123},  
       ],
    }
]


#podemos criar um dict:
pessoa = {'nome':'bryan', 'sobrenome' = 'Rodrigues'}

#ou até um dict vazio
pessoa2 = {}    


"""
métodos uteis dos dicionarios em python

len - quantas chaves
keys - iterável de chaves
values - ite´ravel com os valores
item - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
uptate - atualiza um dicionário com outro
"""



