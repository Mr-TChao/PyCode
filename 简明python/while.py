number = 23
running = True

while running:
    guess = int(input("enter an integer:"))
    if guess == number:
        print("congratulations,you guessed it.")
        running = False         # 这将导致循环终止
    
    elif guess < number:
        print("no,it is a little higher than that.")
    
    else:
        print("no,it is a little lower than that.")

else:
    print("the while loop is over.")

print("done")