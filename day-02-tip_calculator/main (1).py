#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Bem vindo a calculadora
print("Welcome to the tip calculator.")
#Entrada do valor da conta
bill_value = input("What was the total bill? $")
#Entrada da porcentagem de gorjeta
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
#Qtd de pessoas pra dividir a conta
split_number = input("How many people to split the bill? ")
#Soma da conta + gorjeta
full_bill = float(bill_value) * (1+float(tip_percentage)/100)
#COnta completa dividida pelas pessoas
split_value = full_bill/float(split_number)
#Arredondamento da conta para 2 digitos
# final_value = round(split_value,2)
final_value = "{.2f}".format(split_value)
#Imprimir valor final da conta para cada pessoa
print(f"Each person shoud pay: ${final_value}")
