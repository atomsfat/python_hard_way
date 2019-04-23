from sys import argv

script, user_name = argv

prompt = '>'

print(f"Hi {user_name} this is script {script}")
print("I would like to ask some questions")
print(f"Do you like me {user_name} ?")
likes = input(prompt)

print("Where do you lives")
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print(f"""
Allright, you said {likes} about liking me.
You lives in {lives}. Not sure where that.
And you have a computer {computer}. Nice
""")
