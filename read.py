import json

with open("text/keywords.json") as json_file:
    data = json.load(json_file)
    val = data["keywords"]
    for i in val:
        print(i)
lis = ["apple", "grape", "melon"]

check = any(item in val for item in lis)

if check is True:
    print("The list {} contains all elements of the list {}".format(val, lis))
else:
    print("No, List1 doesn't have all elements of the List2.")