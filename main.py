def symmetric_difference(set1, set2):
    # Используем оператор ^ для нахождения симметрической разности множеств
    return set1 ^ set2

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result_set = symmetric_difference(set1, set2)
print("новое уникальное множество:", result_set)
