# get and process input for a list of names
names =  input("Enter names separated by commas: ").title().split(",")

# get and process input for a list of the number of assignments
assignments =  list(map(lambda x: int(x),input("Enter assignment counts seprated by commas: ").split(",")))
# get and process input for a list of grades
grades =  list(map(lambda x: int(x),input("Enter grades separated by commas: ").split(",")))

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name,assignment,grade in zip(names,assignments,grades):
    print(message.format(name,assignment,grade,assignment*2 + grade))


'''
Enter names separated by commas: chandler bing,phoebe buffay,monica geller,ross geller
Enter assignment counts seprated by commas: 3,6,0,2
Enter grades separated by commas: 81,77,92,88
Hi Chandler Bing,

This is a reminder that you have 3 assignments left to submit before you can graduate. You're current grade is 81 and can increase to 87 if you submit all assignments before the due date.


Hi Phoebe Buffay,

This is a reminder that you have 6 assignments left to submit before you can graduate. You're current grade is 77 and can increase to 89 if you submit all assignments before the due date. grade is 77 and can increase to 89 if you submit all assignments before the due date.


Hi Monica Geller,

This is a reminder that you have 0 assignments left to submit before you can graduate. You're current grade is 92 and can increase to 92 if you submit all assignments before the due date.

Hi Ross Geller,

This is a reminder that you have 2 assignments left to submit before you can graduate. You're current grade is 88 and can increase to 92 if you submit all assignments before the due date.
'''