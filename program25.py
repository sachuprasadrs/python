def sort_dictionary(d):
     ascending_by_keys = dict(sorted(d.items()))
     descending_by_keys = dict(sorted(d.items(), reverse=True))
     ascending_by_values = dict(sorted(d.items(), key=lambda x: x[1]))
     descending_by_values = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

     return ascending_by_keys, descending_by_keys, ascending_by_values, descending_by_values

dictionary = {'a': 3, 'c': 1, 'b': 2}

asc_keys, desc_keys, asc_values, desc_values = sort_dictionary(dictionary)

print("Ascending by keys:", asc_keys)
print("Descending by keys:", desc_keys)
print("Ascending by values:", asc_values)
print("Descending by values:", desc_values)
