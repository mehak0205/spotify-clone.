sum=0
while(True):
	userInput=input("Enter the item price or enter q to quit : \n")
	if(userInput!='q'):
		sum=sum+int(userInput)
		print(f"Total order so far is {sum}")
	else:
		print(f"Your total bill is {sum}. Thanks for shopping with us.")
		break
