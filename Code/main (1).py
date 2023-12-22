from os import system

# command names
commands = [
    "createdir",
    "removedir",
    "rename",
    "findme",
    "fish",
    "memusage",
    "terminate",
    "spy",
    "closeter",
    "panda",
    "cls",
    "closeall",
    "removefile",
    "list",
    "play",
    "jokes",
    "factor",
    "multiply",
    "square",
    "squareroot",
    "sum",
    "createfile"
    ]
    
def shell_help():

    """
    Function to display the help text for the shell on startup.
    """

    f = open('startup_files/startup.txt', 'r')        
    print(f.read())
    print('\n')
 
def insufarg():
    print("Insufficient arguments to the command")

def shell():

    """
    Function that runs the shell.
    """

    startup = 1
    from_cmd_error = 0

    while 1:
        if startup == 1:
            startup = startup + 1
            _ = system('clear')
            shell_help()        
        
        if (from_cmd_error == 0):
            userinput = input("\033[1mPshell@\033[94muser\033[0m$ ")
            pass
        else:
            userinput = closest_command + " " + userinput
            from_cmd_error = 0
        
        input_arr = userinput.split()
        if(input_arr[0] == "sos"): # shell help
            shell_help()
        elif(input_arr[0]==commands[0]):
            if len(input_arr) == 3:
                system('python3 createdir.py '+input_arr[1]+' '+input_arr[2])
            else :
                insufarg()
        elif(input_arr[0]==commands[1]):
            if len(input_arr) ==2:
                system('python3 removedir.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[2]):
            if len(input_arr) ==3:
                system('python3 rename.py '+input_arr[1]+' '+input_arr[2])
            else :
                insufarg()
        elif(input_arr[0]==commands[3]):
                system('python3 findme.py')
        elif(input_arr[0]==commands[4]):
            if len(input_arr)==2:
                system('python3 file.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[5]):
            system('python3 memusage.py')
        elif(input_arr[0]==commands[6]):
            if len(input_arr)==2:
                system('python3 terminate.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[7]):
            system('python3 pid.py')
        elif(input_arr[0]==commands[8]) :
            system('python3 closeter.py')
        elif(input_arr[0]==commands[9]):
            if len(input_arr)==2:
                system('python3 panda.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[10]) :
            system('python3 cls.py')
        elif(input_arr[0]==commands[11]):
            if len(input_arr)==2:
                system('python3 closeall.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[12]):
            if len(input_arr)==2:
                system('python3 removefile.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[13]):
            if len(input_arr)==2:
                system('python3 list.py '+input_arr[1])
            elif len(input_arr)==1:
                system('python3 list.py')
            else :
                insufarg()
        elif(input_arr[0]==commands[14]):
            if len(input_arr)==1:
                system('python3 play.py')
            else:
                insufarg()
        elif(input_arr[0]==commands[15]):
            if len(input_arr)==1:
                system('python3 jokes.py')
            else :
                insufarg()
        elif(input_arr[0]==commands[16]):
            if len(input_arr)==2:
                system('python3 factor.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[17]):
            size=len(input_arr)
            size=size
            mul=1
            for i in range(1,size):
                temp=input_arr[i]
                mul=int(temp)*mul
            print(mul)
        elif(input_arr[0]==commands[18]):
            if len(input_arr)==2:
                system('python3 square.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[19]):
            if len(input_arr)==2:
                system('python3 Squreroot.py '+input_arr[1])
            else :
                insufarg()
        elif(input_arr[0]==commands[20]):
            size=len(input_arr)
            size=size
            summation=0
            for i in range(1,size):
                temp=input_arr[i]
                summation=int(temp)+summation
            print(summation)
        
        elif(input_arr[0]==commands[21]):
            if len(input_arr)==3:
                system('python3 createfile.py '+input_arr[1]+" "+input_arr[2])
            else :
                insufarg()

         
        else :
            print("command not found ! Use man command to get information about commands")


                    

shell()
