maior = 0
total = 0
while total < 10:
    n = int(raw_input("valor: "))
    if n > maior:
        maior = n
    total = total + 1
print "MAIOR: ", maior
