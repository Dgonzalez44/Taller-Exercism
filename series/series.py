def slices(series, longitud):
    result = []
    if longitud > 0 and longitud <= len(series):
        for i in range(len(series) - longitud + 1):
            result.append(series[i:i+longitud])
        return result
    else:
        raise ValueError("Esa entrada no esta permitida")