# lista de nomes = []
nomes = ["alex","bruno","eduardo","joão","ziraldo","francisco","alexandre","bernado","roberto"]
print(nomes)

#para exebir em ordem 
print(nomes[0])

print("\n")

# para exebir os nomes em um laço de repetição
for nome in nomes:
    print(nome)

# outra forma de exebir a lista
for i in range(len(nomes)): 
    print(f"{i+1}° nome da lista: {nomes[i]}.") 

# colocar a lista em ordem alfabética
nomes.sort()
print("Lista em ordem alfabética:\n")
for nome in nomes:
    print(nome)