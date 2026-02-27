marks = [45, 78, 90, 33, 60]
count_pass = 0
count_fail = 0

for mark in marks:
    if mark > 50:
        count_pass += 1
    else:
        count_fail += 1
        
print("Marks of students:", marks)
print("Number of students who passed:", count_pass)
print("Number of students who failed:", count_fail)
    