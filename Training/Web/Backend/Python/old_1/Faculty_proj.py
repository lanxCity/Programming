import random

list_of_dep = [
    "TAE", "TCE", "TEL", "TFT", "TIE",
    "TME", "TPE", "TWE",
]

dep_arr = []

while True:
    a = list_of_dep[random.randint(0, len(list_of_dep) - 1)]
    list_of_dep.remove(a)

    b = ''
    if list_of_dep:
        b = list_of_dep[random.randint(0, len(list_of_dep) - 1)]
        list_of_dep.remove(b)

    new_deps = [a, b]
    dep_arr.append(new_deps)

    if not list_of_dep:
        break

print(dep_arr)








