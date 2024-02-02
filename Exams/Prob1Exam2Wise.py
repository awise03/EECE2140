import numpy as np

def magic_square(in_list):
    rows = in_list.shape[0]
    cols = in_list.shape[1]
    conditions_count = 0

    if(rows != cols):
        return False
    if(not is_unique(in_list)):
        conditions_count += 1
    
    target_value = sum(in_list[0, :])
    diagonal_sum = reverse_diagonal = 0

    for x in range(rows):
        sum_rows = np.sum(in_list[x, :])
        sum_cols = np.sum(in_list[:, x])

        diagonal_sum += in_list[x][x]
        reverse_diagonal += in_list[x][cols - 1 - x]

        if (sum_rows != target_value) or (sum_cols != target_value):
            return False
        
    if (diagonal_sum != target_value) or (reverse_diagonal != target_value):
        conditions_count += 1
    
    return (True, conditions_count)

def is_unique(in_list):
    values = {}

    for rows in range(len(in_list[0])):
        for cols in range(len(in_list)):
            if(in_list[rows][cols] not in values):
                values[in_list[rows][cols]] = 1
            else:
                return False
    return True
    

test_case1 = np.array([[2, 16, 13, 3],[11, 5, 8, 10], [7, 9, 12, 6], [14, 4, 1, 15]])
test_case2 = np.array([[29**2, 1, 47**2], [41**2, 37**2, 1], [23**2, 41**2, 29**2]])
j = magic_square(test_case1)   
h = magic_square(test_case2)
print(f'Test Case 1: {j}') 
print(f'Test Case 2: {h}') 


    
