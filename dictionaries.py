# this is a single dict
dict = {"key1": "value", "key2": "value"}

# this is a dictionary storing multiple dictionaries
dict_of_dicts = {"dict1": {"key1": "value"}, "dict2": {"key": "value"}}

# add a key/value pair
dict["new key"] = "value of new key"

# update a dict
dict["key1"] = "new key1 value"

# add a new dict to the dict of dicts
dict_of_dicts["new dict name"] = {"key": "value"}

# update a value in the dict of dicts
dict_of_dicts["dict1"]["key1"] = "new value"

# print the dict (returns {'key':'value'}) etc.
print(dict)

# prints the dict of dicts, but is a little cluttered
print(dict_of_dicts)

# a better way is, however this only prints the dict name
for item in dict_of_dicts:
    print(item)

# to print the contents too:
for item in dict_of_dicts:
    print(item, dict_of_dicts[item])

# to delete a value from a dict
del dict["new key"]

# if the key doesn't exist the program will crash though, a safer way
dict.pop("new key", None)

print(dict)
