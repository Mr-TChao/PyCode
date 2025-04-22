# ex14.py 提示和传递

from sys import  argv
script, user_name= argv
prompt = '>'

print(f'Hi {user_name}, I\'M THE {script} script)')
print(f"I'd like to ask you a few questions.")
likes = input(prompt)

print(f"What do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright , so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
''')