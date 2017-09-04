def diaginal_reverse(general_scope, count_in_row):
    general_scopelist = range(general_scope)
    matrix = [range(i + 1, i + 1 + count_in_row) for i in general_scopelist[::count_in_row]]
    for i in range(len(matrix)):
        print matrix[i]
    print '\n'

    print 'count_in_row = ' + str(len(matrix))
    print 'number of rows in matrix = ' + str(len(matrix[0])) + '\n'

    if len(matrix[0]) < len(matrix):
        raise Exception('Please specify \"count_in_row\" value to be equal or less to number of rows in matrix')
    else:
        rmatrix = [[row[k] for row in matrix] for k in range(len(matrix))]
        for k in range(len(rmatrix)):
            print rmatrix[k]


diaginal_reverse(9, 3)
