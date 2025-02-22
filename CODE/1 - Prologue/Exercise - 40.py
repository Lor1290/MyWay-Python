#Esercizio di LeetCode

def Multi_Array(_MultiArray_):
    
    _SortedMultiArray_ = []
    
    for i in _MultiArray_:

        i.sort()
        print(i)

    for i in _MultiArray_:

        if type(i) != None:

            _SortedMultiArray_.extend(i)
    
    _SortedMultiArray_.sort()

    return _MultiArray_, _SortedMultiArray_

cicle = True

print()
print("Welcome to my new application, where you are going to give me a series of 'multi-array', and i'm going to create a single 'sorted-array'")
print("In this case, you have to insert a series of number, and write 'enter' each thime you want this series of number to be in a single array")
print("Then, if you want to stop, you simply write down 'Stop' on the console, and the application whill let you see the results")
print()
print("Here are some examples =")
print(">>> Input: [1, 2, 10, 4, 6] --> fisrt array")
print(">>>        [12, 75, 32, 11, 14] --> second array")
print(">>>        [1, 2, 78, 44, 55, 99, 102] --> third array")
print()
print(">>> The final 'multi-array' will be: [[1, 2, 4, 6, 10], [11, 12, 14, 32, 75], [1, 2, 44, 55, 78, 99, 102]]")
print("    (P.S. if you notice, the numbers in the insgle array are sorted)")
print(">>> the final 'sorted-array' will be: [1, 1, 2, 2, 4, 6, 8, 10, 11, 12, 14, 32, 44, 55, 75, 78, 99, 102]")
print()
print("There are also some rules = ")
print("                            - If you want to insert a 'Null' value, just type 'Null', and then press 'enter'")
print("                            - The lenght of the 'sorted-array' cant be over 10E4 and less than 0")
print("                            - The lenght of the 'multy-array' can't be over 500 and less than 0")
print("                            - The number in the 'multy-array' can't be over 10E4 and less than -10E4")
print("                            - The number in the 'multy-array' if added up, can't get over 10E4")
print("\n" * 3)

while cicle:

    print()
    print("What you want to do now?")
    print("--> press '1' if you want to continue")
    print("--> press '2' if you want to exit")
    decision = input("Insert... ")
    print()

    if decision == "1": 

        _MultiArray_ = []
        
        while True:    
            
            _list_ = []           
            _numbers_ = input("Insert the number into the 'multy-array': ")
            
            if _numbers_.lower() == "stop":

                break
                       
            if _numbers_.lower() == "null":

                _MultiArray_.append([])
                continue
                            
            if sum(_list_) > 10 ** 4:
                    
                print(">>> The number in this 'multy-array' are too big... ")
                continue
                    
            if len(_list_) > 500:

                print(">>> this 'multy-array' is too big... ")
                continue
           
            for i in _list_:

                if i > 10 ** 4 or i < -10**4:

                    _list_.pop(i)
            
            _numbers_ = _numbers_.split()
            _list_.insert(0, _numbers_)
            _list_ = [int(i) for i in _list_[0]]
            _MultiArray_.append(_list_)
                
        list_1, list_2 = Multi_Array(_MultiArray_) 

        print()
        print("The 'multy-array' is: ", end="")
        print(list_1)
        print("The 'sorted-array's' is: ", end="")
        print(list_2)
   
    elif decision == "2":

        print(">>>Thanks for using our applications. Goodbye!")
        cicle = False

    else:

        print(">>>You enter a wrong command, retry: ")
