# read a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal
if __name__ == '__main__':
    n = int(input()) # this is the number of lines input by the user
    student_marks = {}  # this is the student dictionary
    for _ in range(n): # excute the for loop for n number of times
        name, *line = input().split() # assign the "name value" to name, and the remaining values in a list to line, inside the list the values are of string type, inputs are splitted on the space
        scores = list(map(float, line))# convert the string values of line into float and saving the list in "scores" variable
        student_marks[name] = scores # here we are passing the name as a key and scores as a value
    query_name = input()# take the query name from the user to find the average marks for that particular user
    marks = student_marks[query_name] #save the marks for a particular student
   # format (value, '.nf')  #format the output to a particular number of decimcal places
    print(format(sum(marks)/3, '.2f'))
