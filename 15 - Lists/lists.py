import copy

ages = [12, 34, 67, 13,[3,5], 34]

ages_copy=copy.deepcopy(ages)

ages_copy[4][0]=9

print(ages)
print(ages_copy)


