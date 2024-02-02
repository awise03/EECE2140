def sort_matrix(in_mat, mode_select = 0):
    sorted_matrix = []

    if(mode_select == 0):
        for k in range(len(in_mat)):
            sorted_matrix.append(sorted(in_mat[k]))

    elif(mode_select == 1):
        sorted_column = []

        for c in range(len(in_mat[0])):
            columns = []
            for r in range(len(in_mat)):
                columns.append(in_mat[r][c])
            sorted_column.append(sorted(columns, reverse = True))
        # print(sorted_column)

        for c in range(len(sorted_column[0])):
            sorted_row = []

            for r in range(len(sorted_column)):
                sorted_row.append(sorted_column[r][c])
                # print(sorted_row)

            sorted_matrix.append(sorted_row)
    else:
        print("Error, mode_select not 0 or 1")
        return -1
    return sorted_matrix

A = [[3, 6, -4, 6], [-8, -4, -1, -7], [-5, 3, -1, 9]]
print(sort_matrix(A))
print(sort_matrix(A, 1))

print(7%5)