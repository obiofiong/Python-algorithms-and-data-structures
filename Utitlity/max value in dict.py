dict_ = { "john" : 1, "mich" : 500, "edwin": 200, "sarah": 229, "Justice" : 770}

array_of_entry = set(zip(dict_.values(), dict_.keys())) #can also make it a list or any other yuo like

max_group = max(array_of_entry)

max_value = max_group[0]
max_key = max_group[1]

print(max_key)


# Another Method
max_count = None
max_name_month = None
for key in dict_:
    if max_count == None or dict_[key] > max_count:
        max_count = dict_[key]
        max_name_month = key