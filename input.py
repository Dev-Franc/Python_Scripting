name_input = input("Enter a list of names (separated by commas): ")
names = name_input.split(",")
assignment_input = input("Enter a list of assignment (separated by commas): ")
assignments = name_input.split(",")
grade_input = input("Enter a list of Grades (separated by commas): ")
grades = name_input.split(",")
p_grade_input = input("Enter a list of Potential Grades (separated by commas): ")
p_grades = name_input.split(",")


for name, assignment, grade, p_grade in zip(names, assignments, grades, p_grades):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, p_grade)
    print(message)