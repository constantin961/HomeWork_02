list01 = [32, 19, 39, 30]
print(f'Lungimea listei: {len(list01)}')  #Homework EX1.1
total = 0
impare = []
for n in list01:
    total += n
    if n % 2 == 1:
        impare.append(n)
print(f"Suma numerelor : {total}")  #Homework EX1.2
print(f"Numerele impare: {impare}") #Homework EX1.3
numere_introduse = []
nr_01 = int(input(f"Cite numere n doriti sa introduceti? "))  #Homework EX2.1
for n in range(nr_01):
    numere_introduse.append(int(input(F"Introduceti {n + 1} cifra:")))
suma_numere = 0
for n in numere_introduse:
    suma_numere += n
    media = suma_numere / len(numere_introduse)
print(f"Media numerelor introduse :{media}")  #Homework EX2.2

nota = []
utilizatori = []
nr_utilizatori = int(input(f'Introduceti numarul de utilizatori:'))  #Homework 3.1
for k in range(nr_utilizatori):
    nota.append(int(input(f"Nota:")))
    utilizatori.append(input(f"Nume:"))
max_nota = max(nota)
max_nota_index = nota.index(max(nota))

print(f"Cea mai mare nota are {utilizatori[max_nota_index]} nota {max_nota}") #Homework 3.2