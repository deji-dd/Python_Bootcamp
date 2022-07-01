import csv

f = open('Exercise_Files/find_the_link.csv', encoding='utf-8')
csv_reader = csv.reader(f)
lines = list(csv_reader)
link = []
my_str = ''
for x in lines:
    for y in x:
        if y.isdigit():
            pass
        else:
            my_str += y
print(my_str)
