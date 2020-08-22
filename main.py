import random
def user_option():
    user_choice = input("Please Enter :\n"
                 "R for rock\n"
                 "P for paper\n"
                 "S for scissor\n"
                 "--------------"
                 " ")
    if user_choice in ["R","r"]:
        user_choice = 'r'
    elif user_choice in ["S", "s"]:
        user_choice = 's'
    elif user_choice in ["P", "p"]:
        user_choice = 'p'
    return user_choice

def comp_option():
    comp_choice = random.randint(1,3)
   #1= r(rock) , 2=p(paper) , 3=s(scissor)
    return comp_choice

while True:

    uc = user_option()
    cc = comp_option()

    if uc == 'r' and cc == 1:
        print("You choose rock , computer choose rock, Hence tie:)")
    elif uc == "r" and cc == 2:
        print("You choose rock , computer choose paper , Hence you loose:))")
    elif uc == "r" and cc == 3:
        print("You choose rock, computer choose scissor , Hence you win:(")

    if uc == 'p' and cc == 2:
        print("You choose paper , computer choose paper, Hence tie :)")
    elif uc == "p" and cc == 1:
        print("You choose paper, computer choose rock , Hence you win:))")
    elif uc == "p" and cc == 3:
        print("You choose paper, computer choose scissor , Hence you loose:(")

    if uc == 's' and cc == 3:
        print("You choose scissor, computer choose scissor , Hence tie:(")
    elif uc == "s" and cc == 2:
        print("You choose scissor, computer choose paper , Hence you win:))")
    elif uc == "s" and cc == 1:
        print("You choose scissor, computer choose rock , Hence you losse:(")

    n = input("Want to continue: y/n ")
    if n == 'y':
         pass
    elif n == 'n':
         print("Thank You")
         break
    else:
        break



    