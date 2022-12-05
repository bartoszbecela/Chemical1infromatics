def my_grade():
    for key in dictionary:
        if x in key:
            print(dictionary[key])



x = int(input("Enter your points"))
dictionary = {range(95,100) : "You have got 5.5",
              range(90,95)  : "You have got 5.0",
              range(85,90)  : "You have got 4.5",
              range(80,85)  : "You have got 4.0",
              range(75,80)  : "You have got 3.5",
              range(70,75)  : "You have got 3.0",
              range(65,70)  : "You have got 2.5",
              range(60,65)  : "You have got 2.0",
              range(0,60) : "You didn't pass the exam, sorry "}




my_grade()