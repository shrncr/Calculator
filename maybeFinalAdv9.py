# Sara Hrnciar
#Lori
#CSC 101
# Program 9: enter an equation. The program converts it to postfix and then calculates the answer. You get to see both!

#calculates the answer using postfix equation given
def actuallyCalc(equation):
    twoNums = []
    for i in equation:
        if i.isdigit():
            twoNums.append(int(i))
        elif i == '+':
            print(twoNums[-2])
            print("+")
            print(twoNums[-1])
            twoNums.append(twoNums.pop(-2) + twoNums.pop(-1))
        elif i == "-":
            print(twoNums[-2])
            print("-")
            print(twoNums[-1])
            twoNums.append(twoNums.pop(-2) - twoNums.pop(-1))
        elif i == "/":
            twoNums.append(twoNums.pop(-2) / twoNums.pop(-1))
        elif i == "*":
            twoNums.append(twoNums.pop(-2) * twoNums.pop(-1))
        elif i == "^":
            twoNums.append(twoNums.pop(-2) ** twoNums.pop(-1))
    return("Your final answer is: " + str(twoNums[0]))

#once the parentheses are gone, converts the contents to postfix
def postFix(equation, symbols):
    
    operInSpecPart = []
    temp = ""

    if type(equation) == str:
        equation = equation.split()
    print("working on: " + str(equation))
    for i in equation:
        #if the char is not a symbol, add it to the temp list
        if i not in symbols:
            temp += i
            #check to see if we need to add the power sign to postfix equation
            if len(operInSpecPart) > 0:
                if symbols[operInSpecPart[len(operInSpecPart)- 1]] == "1":
                    temp += operInSpecPart.pop()
        #if the char is a operator, then add it to the list of operators
        for symb in symbols:
            if i == symb:
                operInSpecPart.append(i)
        #check to see if the operator just added is of higher importance than the one in before it. If it is, add the operator of higher importance
        if len(operInSpecPart) > 1:  
            if symbols[operInSpecPart[len(operInSpecPart)- 1]] >= symbols[operInSpecPart[len(operInSpecPart)- 2]]:
                print(operInSpecPart)
                temp += operInSpecPart.pop(-2) ## or maybe -1
    #once done, add the rest of the operators
    while (len(operInSpecPart) > 0):
        temp += operInSpecPart.pop()
        
    return temp
    
def convertToPostFix(equation, symbols):
    if equation.count("(") == 0:
            equation = equation.replace(")", "")
            return postFix(equation, symbols)
    #makes specPart as specific as possible inside ( innermost parentheses)
    specPart = equation[equation.find("(") +  1:equation.find(")")]

    specPartFirstIndexInEq = equation.find(specPart) - 1
    specPartLastIndexInEq = len(specPart) + specPartFirstIndexInEq + 2
    
    specPart = convertToPostFix(specPart, symbols)
    specPart = specPart.split()
    specPart2 = ""
    
    for i in specPart:
        specPart2+=i
        #rewrite equation with postfix as a singular element (so its basically the same as putting "X" in the program or a digit or something)
    equation =  equation[:specPartFirstIndexInEq] + specPart2 + equation[specPartLastIndexInEq:]
    print("updated equation: " + equation)
    return convertToPostFix(equation, symbols)

    #return(convertToPostFix(equation, symbols))

symbolsMeow = {
    "+": "3", 
    "-": "3", 
    "/": "2", 
    "*": "2", 
    "^": "1"
    }

equationMeow = input("Hey give an equation right freaking now ")
postFixEq = convertToPostFix(equationMeow, symbolsMeow)
print("The postfix notation of your equation is: " + str(convertToPostFix(equationMeow, symbolsMeow)))
print(actuallyCalc(postFixEq))

#( 9 ^ 2 / 4 * ( 4 - 5 - ( 8 * 3 / 2 ) - 2 ) + 3 ) * 3 doesnt work




