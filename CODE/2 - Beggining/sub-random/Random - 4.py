var_str: str = "pallonetto"
list_var_sudd: list = [var_str[x: x+3] for x in range(0, len(var_str), 3)]
*b, = var_str

var_list: list = [1, 2, 3, 4, 5]
var_list: list = [x**2 for x in var_list if x != 5]

str_list: list = ["pallonetto", "palla", "pallone", "pallino", "paolo"]
str_max: str = max(str_list, key = len)

print(b)
print(list_var_sudd)
print(var_list)
print(str_max)

DictList = {"1": "2", "3": "4", "5": [1, 2, 3, 4]}

print(DictList["5"])
