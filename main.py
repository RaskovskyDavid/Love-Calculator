# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

low_name1 = name1.lower()
low_name2 = name2.lower()
low_name = low_name1 + low_name2
score1 = low_name.count('t') + low_name.count("r") + low_name.count("u") + low_name.count("e")
score2 = low_name.count('l') + low_name.count("o") + low_name.count("v") + low_name.count("e")

love_score = int(str(score1)+ str(score2))
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

