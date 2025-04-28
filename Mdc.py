def mdc_bruto (num1, num2):
    max_divider = 0
    menor = lambda num1, num2: num1 if num1 < num2 else num2
        
    for i in range(2, menor(num1, num2)):
        if num1%i == 0 and num2%i == 0:
            max_divider = i 

    return max_divider

def mdc_Euclides(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    
    while num1%num2 != 0:
        num1, num2 = num2, num1% num2

    return num2
print(mdc_Euclides(30,20))


