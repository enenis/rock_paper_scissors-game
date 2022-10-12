import random
def main():
    generate()




def generate():
    score=0
    while True:
        
        mylist=["Rock","Paper","Scissor"]
        rando=random.choice(mylist)
        print(rando)


        win=input("Are You Win: Y/N ").capitalize()
        if win=="Y":
            score+=1
        else:
            score+=0
        con=input("Do you want continue: Y/N ").capitalize()
        if con=="Y":
            continue
        else:
            print("Your Score is : ",score)
            break








if __name__=="__main__":
    main()