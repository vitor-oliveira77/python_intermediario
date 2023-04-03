'''lista = [] 
for numero in range(10): 
    lista.append(numero) 

lista = [ 
    numero * 2 
    for numero in range(10)
] 

print(lista)''' 


## Mapeamento de dados em list comprehension : pega uma lista e joga em outra lista ( contanto que tenha o mesmo número de elemetos)

import pprint # tem recurso mais sofisticados para exibir

def p(v): 
    pprint.pprint(v,sort_dicts=False, width=40)
produtos = [
    {'nome': 'p1', 'preco': 20, }, 
    {'nome': 'p2', 'preco': 10, }, 
    {'nome': 'p3', 'preco': 30, },
]  

novos_produtos = [
    {**produto,'preço': produto ['preco'] * 1.05} 
    if produto ['preco'] > 20 else {**produto} 
    for produto in produtos
] 

print(*novos_produtos, sep='\n') 

print("-----------------------------------")
## filtro : você escolhe oque filtrar e exibir 

novos_produtos = [
    {**produto,'preço': produto ['preco'] * 1.05}  
    if produto['preco'] > 20 else {**produto}  
    for produto in produtos 
    if(produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 
] 

p(novos_produtos)