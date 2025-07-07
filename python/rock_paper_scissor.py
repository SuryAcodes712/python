import random
from re import S

emojis ={'r':'🪨','p':'📃','s':'✂️'}
choices=("r","p","s")
while True:
    print("Rock Paper or Scissor(r/p/s): ")

    userinput=input("Enter your choice: ").lower()
    if userinput not in choices:
        print("!Invalid Input")
        continue    

    computer_choice=random.choice(choices)

    print(f'you chose {userinput} {emojis[userinput]}')
    print(f'computer chose {computer_choice} {emojis[computer_choice]}')

    if userinput==computer_choice:
        print("Tie")
    elif (
        (userinput=="r" and computer_choice=="s") or 
        (userinput=="p" and computer_choice=="r") or
        (userinput=="s" and computer_choice=="p")):
        print("You win")
    else:
        print("You lose")

    Should_continue=input('continue(y/n): ').lower()    
    if Should_continue=='y':
        continue
    else:
        break
        