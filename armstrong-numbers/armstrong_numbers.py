def is_armstrong_number(numero):
    number_text = str(numero)
    count, size = 0, len(number_text)
    for i in number_text:
        count += int(i) ** size
    return count == numero
