#python3 ~/Documents/GitHub/avery-python-projects/simple_equations.py

#This will check if the entered equation is actually an equation.
variables = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def check_for_equation(equation):
    format = True
    reason = ""
    if "=" not in equation:
        format = False
        reason = "there is no equal sign in your equation"
    vars = []
    for character in equation:

        if character.lower() in variables:
            vars.append(character)
    if len(vars)==0:
        format = False
        if len(reason)==0:
            reason = "there is no variable in your equation"
        else:
            reason += " and there is no variable in your equation"
    elif len(vars)>1:
        format = False
        if len(reason)==0:
            reason = "there are multiple variables in your equation"
        else:
            reason += " and there are multiple variables in your equation"
    return format, reason
#Get equation to solve
print("Hello! Welcome to the equation solver. ")
while True:
    input_equation = input("Enter your equation (please only enter equations with one variable and no * or / operators.): ")
    correct_format, reason = check_for_equation(input_equation)
    if correct_format:
        break
    else:
        print("There is some mistake. Your equation is not in the correct format and the reason is "+reason+". Please try again. ")

#Get rid of spaces
equation = ""
for i in input_equation:
    if i != " ":
        equation += i
def simplify_fractions(fraction):
    sign = ""
    numerator, denominator = fraction.split("/")
    if denominator[0] == "-" and numerator[0] == "-":
        sign = ""
    elif denominator[0] == "-" or numerator[0] == "-":
        sign = "-"
    else:
        sign = ""
    if "-" in numerator:
        numerator = numerator[1:]
    if "-" in denominator:
        denominator = denominator[1:]
    numerator_factors = []
    denominator_factors = []
    for i in range(1, int(numerator)+1):
        if int(numerator) % i == 0:
            numerator_factors.append(i)
    for i in range(1, int(denominator)+1):
        if int(denominator) % i == 0:
            denominator_factors.append(i)
    gcf = 0
    for number in numerator_factors:
        if number in denominator_factors:
            gcf = number
    new_numerator = int(int(numerator)/gcf)
    new_denominator = int(int(denominator)/gcf)
    if new_denominator == 1:
        return sign+str(new_numerator)
    else:
        return sign+str(new_numerator) + "/" + str(new_denominator)
#Find the variable
for i in equation:
    if i.lower() in variables:
        variable = i
        break

#Split equation up into right side and left side
left_side, right_side = equation.split("=")
#Split up sides into terms
operators = ["+", "-"]
def split_terms(right_side, left_side, variable):
    right_side_terms = []
    left_side_terms = []
    #Splits the terms on the right side
    term = ""
    for i in range(len(right_side)):
        value = right_side[i]
        if value in operators:
            if len(term)>0:
                term = ""
                term += value
            else:
                term += value
        elif value != variable:
            term += value
            if i == len(right_side) - 1:
                right_side_terms.append(term)
            if i == 0:
                term = "+"+term
                if len(right_side)>1:
                    if right_side[i+1] in operators:
                        right_side_terms.append(term)
                        term = ""
                else:
                    right_side_terms.append(term)
                    term = ""
            if i != 0 and i != len(right_side)-1 and right_side[i+1] in operators:
                    right_side_terms.append(term)
        else:
            if i == 0:
                term = "+1"+variable
            elif right_side[i-1] in operators:
                term += "1"+variable
            else:
                term += variable
            right_side_terms.append(term)
    term = ""
    #Splits the terms on the left side
    for i in range(len(left_side)):
        value = left_side[i]
        if value in operators:
            if len(term)>0:
                term = ""
                term += value
            else:
                term += value
        elif value != variable:
            term += value
            if i == len(left_side) - 1:
                left_side_terms.append(term)
            if i == 0:
                term = "+"+term
                if len(left_side)>1:
                    if left_side[i+1] in operators:
                        left_side_terms.append(term)
                        term = ""
                else:
                    left_side_terms.append(term)
                    term = ""
            if i != 0 and i != len(left_side)-1 and left_side[i+1] in operators:
                left_side_terms.append(term)
        else:
            if i == 0:
                term = "+1"+variable
            elif left_side[i-1] in operators:
                term += "1"+variable
            else:
                term += variable
            left_side_terms.append(term)
    return right_side_terms, left_side_terms
right_side_terms, left_side_terms = split_terms(right_side, left_side, variable)
left_side_term = ["+1x", "-9"]

#Combines the variables within each side
def combine_var(side, variable):
    variables = []
    for term in side:
        if variable in term:
            variables.append(term)

    total = 0
    for element in variables:
        if len(element) == 2:
            if element[0]=="+":
                total += 1
            elif element[0] == "-":
                total -= 1
        else:
            var_number = ""
            for char in element:
                if char != variable and char not in operators:
                    var_number += char
                elif char == "-":
                    var_number += "-"
            if len(var_number) >0:
                total += int(var_number)
    return str(total) + variable

#combines the numbers within each side
def combine_ints(side, variable):
    total = 0
    for term in side:
        if variable not in term and term not in operators and len(term)>1:
            if term[0]=="+":
                total += int(term[1::])
            else:
                total -= int(term[1::])
    if total >= 0:
        return "+"+str(total)
    else:
        return str(total)

left_var = combine_var(left_side_terms, variable)
right_var = combine_var(right_side_terms, variable)
left_ints = combine_ints(left_side_terms, variable)
right_ints = combine_ints(right_side_terms, variable)

#Finds the total number of variables and the total number of numbers
def find_totals(left_var, right_var, left_int, right_int,variable):
    total_var = int(left_var[:-1:])-int(right_var[:-1:])
    total_int = int(right_int) - int(left_int)
    return str(total_var)+variable, str(total_int)
total_var,total_ints = find_totals(left_var, right_var, left_ints, right_ints, variable)

#Finishes solving for the variable
def solve(total_vars, total_ints):
    value = 0
    if int(total_ints) % int(total_vars[:-1:]) == 0:
        value = str(int(int(total_ints) / int(total_vars[:-1:])))
    else:
        value = str(total_ints) +"/"+str(total_vars[:-1:])
        value = simplify_fractions(value)
    return value
value = solve(total_var, total_ints)
print(variable+ " = "+value)
