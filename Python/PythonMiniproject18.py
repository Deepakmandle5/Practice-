
# Updated mini project
# Maths Quiz
Questions = [ 
    ["Q1:(100-50)*2",
    "A = 100","B = 50","C = 25","D = 75"],
    ["Q2:(2*2*4*4)",
    "A = 54","B = 64","C = 94","D = 84"],
    ["Q3:(38/2+20/4)",
    "A = 55","B = 64","C = 24","D = 37"],
    ["Q4:(34*4)+(54/6)",
    "A = 105", "B = 410","C = 565","D = 460"],
    ["Q5:(37+9)-(64/8)", 
    "A = 100","B = 38","C = 56","D = 94"],
    ]
correct_answer =["A","B","C","D","B"]
point = 0
i = 0

for q in Questions:
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    answer =(input("Enter the answer: "))

    if answer == correct_answer[i]:
        point = point + 10
        print("Answer is correct.")
        print("You get a 10 points")
    else:
          print("Answer is wrong.")  

    i = i + 1

print("Your total score is",point,"points")          
