products =[["Phone", 340, False], ["PC", 1400, True], ["Tablet", 980, True]]
# Create another list base on the products and include only products which
# are on sale with the third data = True
# Do it the usual way of constructing the list.
# new_list =[["PC", 1400, True], ["Tablet", 980, True]]

new_list = []
for each in products:
    if each[2] == True:
        new_list.append(each)
print(new_list)
# list comprehension
compr_list = [each for each in products if each[2] == True]
print(compr_list)

# dictionary comprehension
age_dict = {"Ann": 17, "Jane": 19, "Jack": 20}
# Construct a new age dictionary that contains only people who are above 18
new_dict = {name: age for name, age in age_dict.items() if age > 18}
print(new_dict)