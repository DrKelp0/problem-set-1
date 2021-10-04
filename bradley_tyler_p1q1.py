# Quiz Creation Activity

# Quiz has 5 questions the user will answer
# It will keep track of score and give
# a final result

print("Welcome to this Epic quiz")
score_end = 0

print("What is 2 + 5?")
q1_ans = float(input())
if q1_ans == 7:
    print("Great job!")
    score_end = score_end + 1
else:
    print("Better luck next time.")
    score_end = score_end + 0
print(f"You have {score_end} questions correct so far.")

print("What is Obama's last name?")
q2_ans = input()
if q2_ans == "Obama":
    print("Wow, you're smart!")
    score_end = score_end + 1
elif q2_ans == "obama":
    print("Wow, you're smart!")
    score_end = score_end + 1
else:
    print("Wrong.")
    score_end = score_end + 0
print(f"You have {score_end} questions correct so far.")

print("How many stars are on the U.S. flag?")
q3_ans = float(input())
if q3_ans == 50:
    print("You're pretty smart, Great Job!")
    score_end = score_end + 1
else:
    print("You are correctn't")
    score_end = score_end + 0
print(f"You have {score_end} questions correct so far.")

print("Answer this math question")
print("3 + (6(11 + 1 - 4)) / 8 * 2")
q4_ans = float(input())
if q4_ans == 15:
    print("Amazing work, but can you get the last one right?")
    score_end = score_end + 1
else:
    print("Incorrect")
    score_end = score_end + 0
print(f"You have {score_end} questions correct so far.")

print("How do you spell pneumonoultramicroscopicsilicovolcanoconiosis")
q5_ans = input()
if q5_ans == "pneumonoultramicroscopicsilicovolcanoconiosis" :
    print("You are a genius!")
    score_end = score_end + 1
else:
    print("Nice try")
    score_end = score_end + 0

print(f"You got {score_end} questions right in total")
if score_end == 5:
    print("You got 100% on this quiz!")
    print("You are part of the 1% smartest people in the world!")
elif score_end == 4:
    print("You got 80% on this quiz!")
    print("You are clearly very smart, but you could be smarter.")
elif score_end == 3:
    print("You got 60% on this quiz")
    print("You have some knowledge, but lack a meaningful amount.")
elif score_end == 2:
    print("You got 40% on this quiz")
    print("You still have a ways to go.")
elif score_end == 1:
    print("You got 20% on this quiz")
    print("You need lots of work.")
elif score_end == 0:
    print("You got 0% on this quiz")
    print("You are very dumb")


