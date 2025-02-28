def searchMatrix(matrix, target):
    fst_idx, lst_idx = 0, len(matrix)

    """Finding row"""
    while fst_idx != lst_idx:
        row_idx = (fst_idx + lst_idx) // 2
        if target > matrix[row_idx][-1]:
            fst_idx = row_idx + 1
        elif target <= matrix[row_idx][-1]:
            if target >= matrix[row_idx][0]:
                break
            else:
                lst_idx = row_idx
        else: return True

    fst_idx, lst_idx = 0, len(matrix[0])
    while fst_idx != lst_idx:
        col_idx = (fst_idx + lst_idx) // 2
        if target < matrix[row_idx][col_idx]:
            lst_idx = col_idx
        elif target > matrix[row_idx][col_idx]:
            fst_idx = col_idx + 1
        else:
            return True
    return False


# mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# tar = 3
# print(searchMatrix(mat, tar))

# mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# tar = 10
# print(searchMatrix(mat, tar))
