# ----- 2.1 ----- #
favorieten = ['Martin Garrix']
favorieten.append('Zanger Rinus')

favorieten[1] = 'Brooks'
print(favorieten)


# ----- 2.3 ----- #
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(grades.count(7))
grades[8] = 4
grades.sort()
print(round(sum(grades) / len(grades), 1))