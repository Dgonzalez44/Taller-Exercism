def is_isogram(palabra):
  letras = [ch for ch in palabra.lower() if "a" <= ch <= "z"]
  return len(letras) == len(set(letras))