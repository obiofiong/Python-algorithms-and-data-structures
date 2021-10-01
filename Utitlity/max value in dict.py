dict_ = { "john" : 1, "mich" : 500, "edwin": 200, "sarah": 229, "Justice" : 770}

array_of_entry = set(zip(dict_.values(), dict_.keys())) #can also make it a list or any other yuo like

max_group = max(array_of_entry)

max_value = max_group[0]
max_key = max_group[1]

print(max_key)