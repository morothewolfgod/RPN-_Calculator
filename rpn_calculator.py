
import string, operator

error_flag = False

def is_valid_number(n):
    is_valid_number = True
    try:
        num = float(n)
        is_valid_number = num == num
    except ValueError:
        is_valid_number = False

    return is_valid_number

def add_val_to_array(n):
    try:
        int_value = int(n)
        return int_value
    except ValueError:
        return float(n)

def exit_program (n):
    global error_flag 
    error_flag = True
    if n == 1:
       print("Two valid numbers are needed to do a math operation")
    elif n == 2:
        print("A math operation is needed")
    elif n == 3:
        print("Entry must be a valid number or operator")
    elif n == 4:
        print("Exiting program")
        exit(1)

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

val=[]
while True:
    error_flag = False
    #loops through values added in console
    for input in string.split(raw_input()):
        val_length = len(val)
        #if value is an operation and has valid numbers and amount of number do operation 
        if input in operations:
            if val_length >= 2 and is_valid_number(val[0]) and is_valid_number(val[1]):
                #adding result at bottom of stack and removing value at top of stack
                val[0] = operations[input](val[0],val[1])
                val.pop()
            else:
                exit_program(1)
        #if value is a valid number add
        elif is_valid_number(input):
            if (val_length + 1 > 2):
                 exit_program(2)
            else:
                val.append(add_val_to_array(input))
        #the program is exiting based on request
        elif input == "q":
            exit_program(4)
        else:
            exit_program(3)
        # updating val_length to current length
        val_length = len(val) 
    #if no errors occured and a value is in val[], print value at top of stack
    if val_length > 0 and error_flag == False:
        print(val[val_length-1])