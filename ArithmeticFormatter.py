def error_tretment(num1,operator,num2):
    if operator == "":
            return "Error: Operator must be '+' or '-'."
    elif not num1.strip().isnumeric() or not num2.strip().isnumeric():
         return 'Error: Numbers must only contain digits.'
         
    elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
    return ""
def calculate(num1,operator,num2):
    pass

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    final_string = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
              
    for exper in problems:
        num1 = ""
        operator = ""
        num2 = ""
        
        next_number = False

        for char in exper:
            if char == "+":
                operator = "+"
                next_number = True
            elif char == "-":
                operator = "-"
                next_number = True
                                  
            elif char != " ":  #Aceita números com espaços internos (ex: "3 80 1" → "3801") e operadores sem espaços (ex: "123+49" → "123 + 49").
           
                if next_number:
                    num2 += char
                else:
                    num1 += char

        error = error_tretment(num1, operator, num2)
        if error != "":
            return error_tretment(num1, operator, num2)
        largura = max(len(num1), len(num2)) + 2
        spaces1 = largura - len(num1)
        spaces2 = largura - len(num2) - 1  

        line1 += " " * spaces1 + num1 + "    "
        line2 += operator + " " * spaces2 + num2 + "    "
        line3 += "-" * largura + "    "

    final_string = f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"
    return final_string


# Teste
print(arithmetic_arranger(["3 80 1 - 2", "123+49"]))
