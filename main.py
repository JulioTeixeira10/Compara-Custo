with open("C:\\Users\\Usefr\\Desktop\\ComparaPreço\\texto1.txt") as t1:
    produtos1 = {}
    n = 0
    for row in t1:
        if not row.endswith('\n'):
            row += '\n'
        idproduto = row[0:7]
        quantidade = float(row[8:-1].strip())
        produtos1[idproduto] = quantidade
        n += 1

with open("C:\\Users\\Usefr\\Desktop\\ComparaPreço\\texto2.txt") as t2:
    produtos2 = {}
    n = 0
    for row in t2:
        if not row.endswith('\n'):
            row += '\n'
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
s = 0
for id in produtos1:
    if id in produtos2:
        if produtos1[id] != produtos2[id]:
            q1, q2 = float(produtos1[id]), float(produtos2[id])
            diff = round(q2 - q1, 3)
            if diff > 0.01 or diff < 0:
                print(f"Diferença -> [{diff}]: ID: {id} = {produtos1[id]} != {produtos2[id]}")
                i += 1
            else:
                pass
        else:
            d += 1
    else:
        print(f"Produto não encontrado no outro arquivo: ID = {id}")
        s += 1

if d == len(produtos1):
    print("Não há diferenças de preço entre os dois arquivos.")
else:
    print("\n")
    print(f"Foram encontradas {i} diferenças entre os dois arquivos.")

if s == 0:
    pass
else:
    print(f"Exitem {s} produtos na lista 1 que não foram encontrados na lista 2")