number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    # 新块从这里开始
    print("Congratulations, you guessed it.")
    print("(but you do not win any prizes!)")
    # 新块在这里结束

elif guess < number:
    # 另一个新块
    print("No, it is a little higher than that")
    # 你可以在此做任何你希望改代码块内进行的事情.

else:
    print("No, it is a little lower than that")
    # 你必须通过猜测一个大于 设置的数字来达到这里. 

print("Done")