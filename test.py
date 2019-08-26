# d = {'a': [1,4,6],'b':[2,8,4]}

# best_mods = []
# for k, v in d.items():
# 	print(v)
# 	print(max(v))
# 	print(v.index(max(v)))
# 	mod = k + str(v.index(max(v))+2)  # get index of best model and add two to get the number of the model
# 	best_mods.append(mod)

# print(best_mods)


# d = {}
# d["Resnet2"] = {}

# d["Resnet2"]["dnp0.jpg"] = "dog pooping"
# d["Resnet2"]["dnp1.jpg"] = "dog not pooping"
# d["Resnet2"]["dp0.jpg"] = "dog pooping"
# d["Resnet2"]["dp1.jpg"] = "dog pooping"

# print(d)

import json
with open("actuals.json", "r") as read_file:
    data = json.load(read_file)

data = data[0]
print(data)