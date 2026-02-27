names = [" Alice ", "bob", " CHARLIE "]

# Remove extra spaces 

for i in range(len(names)):
    names[i] = names[i].strip()
print("remove extra spaces", names)
#Convert all names to lowercase

for i in range(len(names)):
    names[i] = names[i].lower()
print("convert all names to lowercase", names)
#Print the cleaned list
print("Cleaned list of names:", names)