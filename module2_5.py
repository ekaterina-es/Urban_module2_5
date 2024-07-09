def get_matrix(n, m, value):
    matrix = []
    for kolvo_strok in range(n):
        spisok2 = []
        matrix.append(spisok2)
        kolvo_strok += 1
        for kolvo_stolb in range(m):
            spisok2.append(value)
            kolvo_stolb += 1
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)