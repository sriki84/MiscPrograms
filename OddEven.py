#ODD or even
while True:
    try:
        num = int(input("Enter a number: "));
        if num == 0:
            print("Given number is zero!");           
        elif num%2 ==0:
            print("Given number is Even!");
        else:
            print("Given number is odd!");
                
    except (RuntimeError,ValueError) as inst:
        print("Invalid input; whole Numbers only! ");
        continue;
    else:
        while True:
            play = input("Wanna play again? (Y/N) : ");
            if(play not in ('y','n')):
                print("Incorrect input. Please enter Y/N only!");
                continue;
            else:
                break;
                    
        if play == "y":
            continue;
        else:
            print("bbye!");
            break;

                
        
      
