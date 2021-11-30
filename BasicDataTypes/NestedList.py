n = int(input()) # get the number of students from the user
res = [] # initialise the list
grade = [] #empty list to have all the grades
for i in range(n):  
    name = input() #get the name of the student            # for loop to get all the student values
    mark = float(input()) # get the mark of the student
    res.append([name,mark]) # append a list for each student inside the bigger list
    grade.append(mark) # insert all the students marks in a separate list to prepare for finding the second lowest grade

grade = sorted(set(grade))  # convert the list into a set to have all the unique elements and remove all duplicates, then apply sorted function on the set then store it in the same variable grade,
m=grade[1] # this will give us the second lowest element
name = [] # a list to save the names of the students with the second lowest marks
for val in res: 
    if m == val[1]:
        name.append(val[0])   # val is the list within the bigger result list, val[1] is the marks value, and the for loop is to iterate over all the elements in the bigger list
name.sort() # sort the names in ascending order
for nm in name:
    print(nm)













