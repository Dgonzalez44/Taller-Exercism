def classify(numero):
    aliquot_suma = 0
    if numero < 1:
        raise ValueError("Error")
    for n in range(1, numero):
        if numero % n == 0:
            aliquot_suma += n
    if aliquot_suma == numero:
        return "perfect"
    elif aliquot_suma > numero:
        return "abundant"
    else:
        return "deficient"
pass