from faker import Faker
from collections import Counter
import json

fake = Faker()
color_list = []

for i in range(20):
    color = fake.color_name()
    color_list.append(color)
print(color_list)


def remove_dups(sample):
    no_dups = []
    check_dups = Counter(sample)
    print(check_dups, "\n", f"Total items before removal: {len(sample)}")

    if type(sample) is list and len(sample) != 0:
        for x in sample:
            if x not in no_dups:
                no_dups.append(x)
        print(f"Total items after removal: {len(no_dups)}")
        return (no_dups)
    return "Please enter a string with at least 1 item"


remove_dups(color_list)


color_dict = {color: len(color) for color in color_list}
print(color_dict)


with open("./data/color_list.json", "w") as json_wfile:
    json.dump(color_dict, json_wfile, indent=4, skipkeys=True)
print("done!")


with open("./data/color_list.json", "r") as json_rfile:
    color_read_dict = json.load(json_rfile)
    for key, value in color_read_dict.items():
        if value >= 4:
            print(f"Color name: {key}, its length: {value}")
        else:
            print(f"This color has value < 4: {key}, {value}")
