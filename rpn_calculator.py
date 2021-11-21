
import string, operator

error_flag = False

def is_valid_number(n):
    is_valid_number = True
    try:
        num = float(n)
    except ValueError:
        is_valid_number = False

    return is_valid_number

def exit_program (n):
    global error_flag 
    error_flag = True
    if n == 1:
       print("Two valid numbers are needed to do a math operation")
    elif n == 2:
        print("Entry must be a valid number or operator")
    elif n == 3:
        print("Exiting program")
        exit(1)

operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

val=[]
while True:
    error_flag = False
    #loops through values added in console
    for input in string.split(raw_input()):
        val_length = len(val)
        #if value is an operation and has valid numbers 
        if input in operations:
            if is_valid_number(val_length-1) and is_valid_number(val_length-2):
                #adding result at bottom of stack and removing value at top of stack
                val[val_length-2] = operations[input](val[val_length-2],val[val_length-1])
                val.pop()
            else:
                exit_program(1)
        #if value is a valid number add
        elif is_valid_number(input):
            val.append(float(input))
        #exit the program is exiting based on request
        elif input == "q":
            exit_program(3)
        else:
            exit_program(2)
        # updating val_length to current length
        val_length = len(val) 
    #if no errors occured and a value is in val[], print value at top of stack
    if val_length > 0 and error_flag == False:
        print(val[val_length-1])