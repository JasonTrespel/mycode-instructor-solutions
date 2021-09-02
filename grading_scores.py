#!/usr/bin/env python3

## Giving letter grades based on number score.

results = 'Your letter grade is '

score = float(input("What is your score?"))

# if input is higher than or equal to 90
if score >= 90:
    results = results + 'A! Amazing job!'
# if input is higher than or equal to 80
elif score >= 80:
    results = results + 'B! Great job.'
# if input is higher than or equal to 70
elif score >= 70:
    results = results + 'C. Cs get Degrees.'
# if input is higher than or equal to 60
elif score >= 60:
    results = results + 'D. Room for improvment.'
# all other lower integers
else:
    results = results + 'E. For extra failure.'

print(results)
