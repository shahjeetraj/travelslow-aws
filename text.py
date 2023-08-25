dict_example = {'a': 1, 'b': 2}

print("original dictionary: ", dict_example)

dict_example['a'] = 100  # existing key, overwrite
dict_example['c'] = 3  # new key, add
dict_example['d'] = 4  # new key, add

print("updated dictionary: ", dict_example)

test_dict = {"mango":1,"banana":2}
sorted_test_dict = sorted(test_dict)
print(f"{test_dict.get(sorted_test_dict[0])} {sorted_test_dict[0].upper()}")
print(f"{test_dict.get(sorted_test_dict[1])} {sorted_test_dict[1].upper()}")