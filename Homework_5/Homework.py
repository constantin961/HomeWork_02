# fraza = input("Introduceti fraza: ")
# fraza_dict = fraza.split()
# for n in set(fraza_dict):
#     print(f"Word '{n}' was used {fraza_dict.count(n)}")


fraza = input("Introduceti fraza: ")
fraza_dict = fraza.split()
count_vb = dict()
for n in fraza_dict:
    if n in count_vb:
        count_vb[n] += 1
    else:
        count_vb[n] = 1

print(f'Cuvintu {count_vb[n]} sa repetat de {count_vb[n]}')