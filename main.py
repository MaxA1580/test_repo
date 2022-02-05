from prettytable import PrettyTable as pt

print("This is test code")
table = pt()
table.field_names = ["1","2","3"]
table.add_row(["first","second","third"])
print(table.get_string(title = "test table"))
