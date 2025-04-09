def parse_problem(problem):
    op_pos = max(problem.find('+'), problem.find('-'))  
    if op_pos == -1:
         return None, None, None
        
    num1 = problem[:op_pos].replace(" ", "") # garante a formatação independente do n de espaços
    operator = problem[op_pos]
    num2 = problem[op_pos+1:].replace(" ", "")
    
    return num1, operator, num2

def error_tretment(num1,operator,num2):
    if operator == None:
            return "Error: Operator must be '+' or '-'."
    elif not num1.isnumeric() or not num2.isnumeric():
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
    lines = ["","","",""]   
 
              
    for problem in problems:       
        num1, operator ,num2 = parse_problem(problem)
        
        error = error_tretment(num1, operator, num2)
        if error:
            return error
        width = max(len(num1), len(num2)) + 2
        spaces1 = width - len(num1)
        spaces2 = width - len(num2) - 1  

        lines[0] += " " * spaces1 + num1 + "    "
        lines[1] += operator + " " * spaces2 + num2 + "    "
        lines[2] += "-" * width + "    "
        
    final_string = f"{lines[0].rstrip()}\n{lines[1].rstrip()}\n{lines[2].rstrip()}"
    return final_string

# Teste
print(arithmetic_arranger(["3 8       0 1 - 2", "123+49"]))
