num = int(input("Enter a numrator: "))
deno = str(int(input("Enter a denominator: ")))

first_num = int(deno[0]) + 1

n = int(input("Enter a limit to the decimal point you need: "))

if first_num>num:   
    final_result = str(num // first_num) + "."

for i in range(n):
    rem = str(num % first_num)
    quo = str(num // first_num)
    num = int(rem*10 + quo)
    
    final_result = final_result + quo

print(final_result)




    
    



