a = 5  # first assignment
print(a)
a = 10  # second assignment...a is changed
print(a)
print(a + a)
a = a + a  # re-assignment in reference to second assignment
print(a)
print(type(a))  # using 'type' to find out type of assignment
a = 30.1
print(type(a))
# never use special built in keywords as variable names == results in an error
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
