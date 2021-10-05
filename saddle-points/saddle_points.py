def saddle_points(matrix):
    saddlepoints = []

    if not matrix:
        return []
    
    for rownum,row in enumerate(matrix):
        for columnnum, number in enumerate(row):
            try:
                col = [matrix[j][columnnum] for j in range(len(matrix))]
            except IndexError:
                raise ValueError('irregular matrixes are not supported')
            if number == max(row) and number == min(col):                    
                saddlepoints.append(dict(row = rownum+1, column = columnnum+1))
    return saddlepoints or []
    pass