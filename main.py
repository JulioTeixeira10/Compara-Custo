with open("C:\\Users\\Usefr\\Desktop\\ComparaPreço\\texto1.txt") as t1:
    produtos1 = {}
    n = 0
    for row in t1:
        idproduto = row[0:7]
        quantidade = float(row[8:-1].strip())
        produtos1[idproduto] = quantidade
        n += 1

with open("C:\\Users\\Usefr\\Desktop\\ComparaPreço\\texto2.txt") as t2:
    produtos2 = {}
    n = 0
    for row in t2:
        idproduto = row[0:7]
        quantidade = float(row[8:-1].strip())
        produtos2[idproduto] = quantidade
        n += 1

if len(produtos1) != len(produtos2):
    print(f"Diferença na quantidade de IDs: Arquivo 1: {len(produtos1)} // Arquivo 2: {len(produtos2)}")
    print("\n")
else:
    print(f"A quantidade de IDs entre ambos arquivos é CORRETA: {len(produtos1)} IDs")
    print("\n")

i = 0
d = 0
for id in produtos1:
    if id in produtos2:
        if produtos1[id] != produtos2[id]:
            print(f"Diferença encontrada: ID: {id} = {produtos1[id]} != {produtos2[id]}")
            i += 1
        else:
            d += 1
            i += 1
    else:
        print("Produto não encontrado no outro arquivo")
        i += 1

if d == len(produtos1):
    print("Não há diferenças de preço entre os dois arquivos.")
else:
    print("\n")
    print(f"Foram encontradas {len(produtos1) - d} diferenças entre os dois arquivos.")