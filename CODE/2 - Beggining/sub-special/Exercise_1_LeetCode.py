def ZigZag(Row, String):

    operation = True #Index controller
    matrix = []
    ext_matrix = [] #New String

    c = 0 #Determinate the row
    
    for i in range(Row): 
        matrix.append([]) #Create the matrix

    for i in String: #Append the element

        matrix[c].append(i)

        #Control the status of the index
        if operation == True:
            c+= 1
        elif operation == False:
            c-= 1

        #Decision of sum or sub the index
        if c == (Row - 1): 
            operation = not operation
        if c == 0:
            operation = not operation
        
    
    for i in matrix:
        ext_matrix.extend(i)
    
    return ext_matrix

control = True

print("> Insert the number of row and the string: ")

while control: #Check the value's insert
    try:
        row = int(input("> "))
        string = input("> ")
    except ValueError:
        print("Invalid data. Retry: ")
        continue

    #Controlling the condition
    if len(string) not in range(0, 1000):
        print("Invalid data. Retry: ")
        continue
    if row not in range (0, 1000):
        print("Invalid data, retry: ")
        continue

    control = not control

print(ZigZag(row, string)) #Printing the resault