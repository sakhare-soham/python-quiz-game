                                    #Kaun Banega Crorepati (KBC) game 
Question = [ ["During which subject did the student fall asleep in class?", "Math","Science","English","All of These",4]
            ,["Which lecturer do students bunk the most?","Maths","Science","English","none of These",1]
            ,["Which subject has the highest attendance?","Maths","Science","English","none of These",4]
            ,["Which subject do students find the most difficult?","Maths","Science","English","All of These",4]
            ,["When do students start getting serious for exams?","from starting of the semester","one month before exams","3 days before exams","1 day before exams",4]
            ]

prizes = ["1 crore","2 crore","3 crore","5 crore","7 crore"]

    # way to create options 
i = 0
for Question in Question:
    
    print(Question [0])
    print(f"a., {Question [1]}")
    print(f"b., {Question [2]}")
    print(f"c., {Question [3]}")
    print(f"d., {Question [4]}")

# for i, q in enumerate(Question):
#     print("\n" + q[0])
#     print(f"a. {q[1]}")
#     print(f"b. {q[2]}")
#     print(f"c. {q[3]}")
#     print(f"d. {q[4]}")

    # down code is checking answers is correct or not 
    try:
        a = int(input("Enter the correct option number: 1 for a, 2 for b, 3 for c, 4 for d: "))
        if a == Question[5]:
            print(f" congratulations!   ")

        # if a == q[5]:
        #     print(f"🎉 Congratulations! You won {prizes[i]} 🎉")
        else :
            print (f"The correct answer is {Question [5]}")
            print ("Better luck next time")
        
    # if someone try to use other letter except 1,2,3,4 

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")

    
    print (f"you won : {prizes[i]}")
    i += 1