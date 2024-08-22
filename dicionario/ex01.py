x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}

print(x)
print(x["RN"])
print(x["PB"])

print("\n")

print(len(x))
print(*x)

print("\n")

for item in x.items(): 
    print(item)

print("\n")

for item in x.values(): 
    print(item)


