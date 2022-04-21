n = int(input("Zadejte číslo: "))
list_cifer = [int(a) for a in str(n)]
soucet = sum(list_cifer)
print("Ciferný součet čísla " + str(n) + " je " + str(soucet))