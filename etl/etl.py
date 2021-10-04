def transform(old):
    new_dict = {}
    for clave, val in old.items():
        if len(val) > 1:
            for letter in val:
                new_dict[letter.lower()] = clave
        else:
            new_dict[val[0].lower()] = clave
    return new_dict