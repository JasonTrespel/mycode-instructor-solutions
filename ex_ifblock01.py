#!/usr/bin/env python3

# making a very simple conditional script
# input what score you received on a test
print("What was your score on the test?")
score = int(input())

# start the if block
# if score is greater than or equal to 90
if score >= 90:
    print("You did an amazing job!!")

# if score is greater than or equal to 70
elif score >= 70:
    print("Not too bad! Still a passing score.")

# if score is less than or equal to 69
else:
    print("You need to study more...FAILURE.")
    
