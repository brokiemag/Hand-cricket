import random as r
import pyfiglet
import matplotlib.pyplot as plt

ascii_banner = pyfiglet.figlet_format(" Indian Premier League")
print(ascii_banner, end="")
print("--hosted by Sohan/brokiemag\n")
print("")
teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
print('Teams')
print(teams,sep='\n')
myteam =  input("Please choose your teams for this season :-")
print("")
myteam = myteam.upper()
tchoice = r.choice(teams)
if tchoice == myteam:
    tchoice = r.choice(teams)
tchoiceft = r.choice(teams)
if tchoiceft == myteam:
    tchoiceft = r.choice(teams)
tchoiceqt = r.choice(teams)
if tchoice == myteam:
    tchoiceft = r.choice(teams)
def ftie():
        teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
        lst2= [1,2,3,4,5,6,7,8,9,10]
        chancese= 6
        no_of_chances_2= 0
        comp_runs= 0
        your_runs= 0
        chances_1= 6
        no_of_chances_1= 0
        lst1 = [1,2,3,4,5,6,7,8,9,10]
        print ("-----------------------------------------------")
        print (f"{tchoiceft} Batting-\n")
        while no_of_chances_2 < chancese:
            bowl= int(input("Enter Runs for your Bowling Turn: "))
            comp_bat= r.choice(lst2)
            if comp_bat==bowl:
                print (f"{tchoiceft} Guess: {comp_bat}{teams} Guess: ",bowl)
                print (f"The {tchoiceft} is Out. {tchoiceft} Runs= ",comp_runs,"\n")
                break
            else:
                comp_runs= comp_runs+comp_bat
                print (f"{tchoiceft} Guess: ",comp_bat,"your Guess: ",bowl)
                print (f"{tchoiceft} Runs: ",comp_runs,"\n")

            if comp_runs > your_runs:
                    break
                
            

        print ("-----------------------------------------------\nyour Batting\n")
        while no_of_chances_1 < chances_1:
            no_of_chances_2= no_of_chances_2+1
            runs= int(input(f"Enter Runs for {myteam} Batting Turn: "))
            comp_bowl= r.choice(lst1)

            if runs==comp_bowl:
                print (f"your Guess: ",runs,f",{tchoiceft} Guess: ",comp_bowl)
                print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                break
            elif runs>10:
                print ("ALERT!! Support No only till 10\n")
                continue
            else:
                your_runs= your_runs+runs
                print (f"your Guess: {runs},{tchoiceft} Guess: {comp_bowl}")
                print ("your runs Now are: ",your_runs,"\n")       
            no_of_chances_1= no_of_chances_1 + 1  

        

        print ("\n-----------------------------------------------\nRESULTS: ")

        if comp_runs < your_runs:
            print (f"\n{myteam} won the Game.\n\n{myteam} Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")
            ascii_banner = pyfiglet.figlet_format("Champions")
            print(ascii_banner, end="")
        elif comp_runs == your_runs:
            print ("The Game is a Tie")
            ftie()
        else:
            print (f"\n{tchoiceft} won the Game.\n\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]","\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
            cong = ["CONGRATS RUNNER UP","BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
            te = r.choice(cong)
            ascii_banner = pyfiglet.figlet_format("YOUR ELIMINATED")
            print(ascii_banner, end="")    
def fwon():
            teamsfw = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
            lst1 = [1,2,3,4,5,6,7,8,9,10]
            chances_1= 20
            no_of_chances_1= 0
            your_runs= 0
            print (f"-----------------------------------------------\nyour Batting\n")
            while no_of_chances_1 < chances_1:
                runs= int(input(f"Enter Runs for {myteam}'s Batting Turn: "))
                comp_bowl= r.choice(lst1)          
                if runs==comp_bowl:
                    print (f"your Guess: {runs},{tchoiceft} Guess: ",comp_bowl)
                    print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                    break
                elif runs>10:
                    print ("ALERT!! Support No only till 10\n")
                    continue
                else:
                    your_runs= your_runs+runs
                    print (f"your Guess: {runs},{tchoiceft} Guess: ",comp_bowl)
                    print (f"your runs Now are: ",your_runs,"\n")           
                no_of_chances_1= no_of_chances_1 + 1           
            lst2= [1,2,3,4,5,6,7,8,9,10]           
            chances_2= 20
            no_of_chances_2= 0
            comp_runs= 0
            print ("-----------------------------------------------")
            print (f"{tchoiceft} Batting-\n")
            while no_of_chances_2 < chances_2:
            
                bowl= int(input(f"Enter Runs for your Bowling Turn: "))
                comp_bat= r.choice(lst2)           
                if comp_bat==bowl:
                    print (f"{tchoiceft} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"The {tchoiceft} is Out. {tchoiceft} Runs= ",comp_runs,"\n")
                    break
                else:
                    comp_runs= comp_runs+comp_bat
                    print (f"{tchoiceft} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"{tchoiceft} Runs: ",comp_runs,"\n")           
                    if comp_runs > your_runs:
                        break
                    
                    no_of_chances_2= no_of_chances_2+1         
                    print ("\n-----------------------------------------------\nRESULTS: ")         
                if comp_runs < your_runs:
                    print (f"\n{myteam} won the Game.\n\n{myteam} Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")
                    ascii_banner = pyfiglet.figlet_format("Champions")
                    print(ascii_banner, end="")
                elif comp_runs == your_runs:
                    print ("The Game is a Tie")
                    ftie()
                else:
                    print (f"\n{tchoiceft} won the Game.\n\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]","\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                    cong = ["CONGRATS RUNNER UP","BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                    te = r.choice(cong)
                    ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                    print(ascii_banner, end="") 
def flose():
            teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
            lst1 = [1,2,3,4,5,6,7,8,9,10]
            chances_1= 20
            no_of_chances_1= 0
            your_runs= 0
            print (f"-----------------------------------------------\nyour Batting\n")
            while no_of_chances_1 < chances_1:
                runs= int(input(f"Enter Runs for {myteam}'s Batting Turn: "))
                comp_bowl= r.choice(lst1)          
                if runs==comp_bowl:
                    print (f"your Guess: {runs},{tchoiceft} Guess: ",comp_bowl)
                    print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                    break
                elif runs>10:
                    print ("ALERT!! Support No only till 10\n")
                    continue
                else:
                    your_runs= your_runs+runs
                    print (f"your Guess: {runs},{tchoiceft} Guess: ",comp_bowl)
                    print (f"your runs Now are: ",your_runs,"\n")           
                no_of_chances_1= no_of_chances_1 + 1           
            lst2= [1,2,3,4,5,6,7,8,9,10]           
            chances_2= 20
            no_of_chances_2= 0
            comp_runs= 0
            print ("-----------------------------------------------")
            print (f"{tchoiceft} Batting-\n")
            while no_of_chances_2 < chances_2:
            
                bowl= int(input(f"Enter Runs for your Bowling Turn: "))
                comp_bat= r.choice(lst2)           
                if comp_bat==bowl:
                    print (f"{tchoiceft} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"The {tchoiceft} is Out. {tchoiceft} Runs= ",comp_runs,"\n")
                    break
                else:
                    comp_runs= comp_runs+comp_bat
                    print (f"{tchoiceft} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"{tchoiceft} Runs: ",comp_runs,"\n")           
                    if comp_runs > your_runs:
                        break
                    
                    no_of_chances_2= no_of_chances_2+1         
                    print ("\n-----------------------------------------------\nRESULTS: ")         
                if comp_runs < your_runs:
                    print (f"\n{myteam} won the Game.\n\n{myteam} Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")
                    ascii_banner = pyfiglet.figlet_format("Champions")
                    print(ascii_banner, end="")
                elif comp_runs == your_runs:
                    print ("The Game is a Tie")
                    ftie()
                else:
                    print (f"\n{tchoiceft} won the Game.\n\n{tchoiceft} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]","\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                    cong = ["CONGRATS RUNNER UP","BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                    te = r.choice(cong)
                    print(te)
                    ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                    print(ascii_banner, end="") 
def qtoss():
        tchoiceqt = r.choice(teams)
        print(f"{tchoiceqt}  VS  {myteam}\n")
        choice =  input("Please choose odd(o) or even(e) :- ")
        print(f"{tchoiceqt} chose a number")
        comp = r.randint(1,10)
        your =int(input("Please Enter a Number between 1 and 10 *to determine the toss* : ")); 
        tvalue= comp+your
        print(f"the {tchoiceqt} chose:- {comp}")
        print(f"{myteam} chose:- {your}")
        print(f"{comp}+{your}={tvalue}") 
        if choice == "e":
            if tvalue%2==0:
                print(f"{myteam} WON") 
                pitchqt = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2) :- ")) 
                if pitchqt == "1":
                    print(f"{myteam} won the toss and chose to BAT")
                    qwon()
                if pitchqt == "2":
                    print(f"{myteam} won the toss and chose to BALL")
                    qlose()
            else:  
                   print(f"{myteam} LOSE")
                   pitchqt = "2"
                   my_listq = [qwon,qlose]
                   r.choice(my_listq)()
        if choice == "o":     
                if(tvalue&1==1):
                    print(f"{myteam} WON") 
                    pitchqt = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2)"))
                    if pitchqt == "1":
                        print(f"{myteam} won the toss and chose to BAT")
                        qwon()
                    if pitchqt == "2":
                        print(f"{myteam} won the toss and chose to BALL")
                        qlose()
                else:  
                        print(f"{myteam} LOSE")
                        pitchqt = "2"
                        my_listq = [qwon,qlose]
                        r.choice(my_listq)()
def ftoss():
    print(f"{tchoiceft}  VS  {myteam}\n")
    choice =  input("Please choose odd(o) or even(e) :- ")
    print(f"{tchoiceft} chose a number")
    comp = r.randint(1,10)
    your =int(input("Please Enter a Number between 1 and 10 *to determine the toss* : ")); 
    tvalue= comp+your
    print(f"the {tchoiceft} chose:- {comp}")
    print(f"{myteam} chose:- {your}")
    print(f"{comp}+{your}={tvalue}") 
    if choice == "e":
        if tvalue%2==0:
            print(f"{myteam} WON") 
            pitchft = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2) :- ")) 
            if pitchft == "1":
                print(f"{myteam} won the toss and chose to BAT")
                qwon()
            if pitchft == "2":
                print(f"{myteam} won the toss and chose to BALL")
                qlose()
        else:  
               print(f"{myteam} LOSE")
               pitchft = "2"
               my_list = [qwon,qlose]
               r.choice(my_list)()
    if choice == "o":     
            if(tvalue&1==1):
                print(f"{myteam} WON") 
                pitchft = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2)"))
                if pitchft == "1":
                    print(f"{myteam} won the toss and chose to BAT")
                    fwon()
                if pitchft == "2":
                    print(f"{myteam} won the toss and chose to BALL")
                    flose()
            else:  
                    print(f"{myteam} LOSE")
                    pitchft = "2"
                    my_list = [fwon,flose]
                    r.choice(my_list)()
def qtie():
        teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
        lst2= [1,2,3,4,5,6,7,8,9,10]
        chancese= 6
        no_of_chances_2= 0
        comp_runs= 0
        your_runs= 0
        chances_1= 6
        no_of_chances_1= 0
        lst1 = [1,2,3,4,5,6,7,8,9,10]
        print ("-----------------------------------------------")
        print (f"{tchoiceqt} Batting-\n")
        while no_of_chances_2 < chancese:
            bowl= int(input("Enter Runs for your Bowling Turn: "))
            comp_bat= r.choice(lst2)
            if comp_bat==bowl:
                print (f"{tchoiceqt} Guess: {comp_bat}{teams} Guess: ",bowl)
                print (f"The {tchoiceqt} is Out. {tchoiceqt} Runs= ",comp_runs,"\n")
                break
            else:
                comp_runs= comp_runs+comp_bat
                print (f"{tchoiceqt} Guess: ",comp_bat,"your Guess: ",bowl)
                print (f"{tchoiceqt} Runs: ",comp_runs,"\n")

            if comp_runs > your_runs:
                    break
                
            

        print ("-----------------------------------------------\nyour Batting\n")
        while no_of_chances_1 < chances_1:
            no_of_chances_2= no_of_chances_2+1
            runs= int(input(f"Enter Runs for {myteam} Batting Turn: "))
            comp_bowl= r.choice(lst1)

            if runs==comp_bowl:
                print (f"your Guess: ",runs,f",{tchoiceqt} Guess: ",comp_bowl)
                print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                break
            elif runs>10:
                print ("ALERT!! Support No only till 10\n")
                continue
            else:
                your_runs= your_runs+runs
                print (f"your Guess: {runs},{tchoiceqt} Guess: {comp_bowl}")
                print ("your runs Now are: ",your_runs,"\n")       
            no_of_chances_1= no_of_chances_1 + 1  

        

        print ("\n-----------------------------------------------\nRESULTS: ")

        if comp_runs < your_runs:
                print (f"\n{myteam} won the Game.\n\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")         
                print("Congrats you have been sent to semi finals")
                ascii_banner = pyfiglet.figlet_format(" Semi finals-")
                print(ascii_banner, end="")
                qtoss()
        elif comp_runs == your_runs:
                print ("The Game is a Tie") 
                ascii_banner = pyfiglet.figlet_format(" tie-")
                print(ascii_banner, end="")    
                qtie()   
        else:
                print (f"\n{tchoiceqt} won the Game.\n\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]",f"\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                print(ascii_banner, end="") 
                cong = ["BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                te = r.choice(cong)
                print(te)     
def qwon():
            teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
            lst1 = [1,2,3,4,5,6,7,8,9,10]
            chances_1= 20
            no_of_chances_1= 0
            your_runs= 0
            print (f"-----------------------------------------------\nyour Batting\n")
            while no_of_chances_1 < chances_1:
                runs= int(input(f"Enter Runs for {myteam}'s Batting Turn: "))
                comp_bowl= r.choice(lst1)          
                if runs==comp_bowl:
                    print (f"your Guess: {runs},{tchoiceqt} Guess: ",comp_bowl)
                    print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                    break
                elif runs>10:
                    print ("ALERT!! Support No only till 10\n")
                    continue
                else:
                    your_runs= your_runs+runs
                    print (f"your Guess: {runs},{tchoiceqt} Guess: ",comp_bowl)
                    print (f"your runs Now are: ",your_runs,"\n")           
                no_of_chances_1= no_of_chances_1 + 1           
            lst2= [1,2,3,4,5,6,7,8,9,10]           
            chances_2= 20
            no_of_chances_2= 0
            comp_runs= 0
            print ("-----------------------------------------------")
            print (f"{tchoiceqt} Batting-\n")
            while no_of_chances_2 < chances_2:
            
                bowl= int(input(f"Enter Runs for your Bowling Turn: "))
                comp_bat= r.choice(lst2)           
                if comp_bat==bowl:
                    print (f"{tchoiceqt} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"The {tchoiceqt} is Out. {tchoiceqt} Runs= ",comp_runs,"\n")
                    break
                else:
                    comp_runs= comp_runs+comp_bat
                    print (f"{tchoiceqt} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"{tchoiceqt} Runs: ",comp_runs,"\n")           
                    if comp_runs > your_runs:
                        break
                    
                    no_of_chances_2= no_of_chances_2+1         
                    print ("\n-----------------------------------------------\nRESULTS: ")         
            if comp_runs < your_runs:
                print (f"\n{myteam} won the Game.\n\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")         
                print("Congrats you have been sent to finals")
                ascii_banner = pyfiglet.figlet_format(" finals-")
                print(ascii_banner, end="")
                ftoss()
            elif comp_runs == your_runs:
                print ("The Game is a Tie") 
                ascii_banner = pyfiglet.figlet_format(" tie-")
                print(ascii_banner, end="")    
                qtie()   
            else:
                print (f"\n{tchoiceqt} won the Game.\n\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]",f"\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                print(ascii_banner, end="")
                cong = ["BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                te = r.choice(cong)
                print(te) 
def qlose():
        teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
        lst2= [1,2,3,4,5,6,7,8,9,10]
        chancese= 20
        no_of_chances_2= 0
        comp_runs= 0
        your_runs= 0
        chances_1= 20
        no_of_chances_1= 0
        lst1 = [1,2,3,4,5,6,7,8,9,10]
        print ("-----------------------------------------------")
        print (f"{tchoiceqt} Batting-\n")
        while no_of_chances_2 < chancese:
            bowl= int(input("Enter Runs for your Bowling Turn: "))
            comp_bat= r.choice(lst2)
            if comp_bat==bowl:
                print (f"{tchoiceqt} Guess: {comp_bat}{teams} Guess: ",bowl)
                print (f"The {tchoiceqt} is Out. {tchoiceqt} Runs= ",comp_runs,"\n")
                break
            else:
                comp_runs= comp_runs+comp_bat
                print (f"{tchoiceqt} Guess: ",comp_bat,"your Guess: ",bowl)
                print (f"{tchoiceqt} Runs: ",comp_runs,"\n")

            if comp_runs > your_runs:
                    break
                
            

        print ("-----------------------------------------------\nyour Batting\n")
        while no_of_chances_1 < chances_1:
            no_of_chances_2= no_of_chances_2+1
            runs= int(input(f"Enter Runs for {myteam} Batting Turn: "))
            comp_bowl= r.choice(lst1)

            if runs==comp_bowl:
                print (f"your Guess: ",runs,f",{tchoiceqt} Guess: ",comp_bowl)
                print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                break
            elif runs>10:
                print ("ALERT!! Support No only till 10\n")
                continue
            else:
                your_runs= your_runs+runs
                print (f"your Guess: {runs},{tchoiceqt} Guess: {comp_bowl}")
                print ("your runs Now are: ",your_runs,"\n")       
            no_of_chances_1= no_of_chances_1 + 1  

        

        print ("\n-----------------------------------------------\nRESULTS: ")

        if comp_runs < your_runs:
                print (f"\n{myteam} won the Game.\n\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")         
                print("Congrats you have been sent to semi finals")
                ascii_banner = pyfiglet.figlet_format(" Semi finals-")
                print(ascii_banner, end="")
                ftoss()
        elif comp_runs == your_runs:
                print ("The Game is a Tie") 
                ascii_banner = pyfiglet.figlet_format(" tie-")
                print(ascii_banner, end="")    
                qtie()   
        else:
                print (f"\n{tchoiceqt} won the Game.\n\n{tchoiceqt} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]",f"\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                print(ascii_banner, end="") 
                cong = ["BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                te = r.choice(cong)
                print(te)
def won():
            teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
            lst1 = [1,2,3,4,5,6,7,8,9,10]
            chances_1= 20
            no_of_chances_1= 0
            your_runs= 0
            print (f"-----------------------------------------------\nyour Batting\n")
            while no_of_chances_1 < chances_1:
                runs= int(input(f"Enter Runs for {myteam}'s Batting Turn: "))
                comp_bowl= r.choice(lst1)          
                if runs==comp_bowl:
                    print (f"your Guess: {runs},{tchoice} Guess: ",comp_bowl)
                    print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                    break
                elif runs>10:
                    print ("ALERT!! Support No only till 10\n")
                    continue
                else:
                    your_runs= your_runs+runs
                    print (f"your Guess: {runs},{tchoice} Guess: ",comp_bowl)
                    print (f"your runs Now are: ",your_runs,"\n")           
                no_of_chances_1= no_of_chances_1 + 1           
            lst2= [1,2,3,4,5,6,7,8,9,10]           
            chances_2= 20
            no_of_chances_2= 0
            comp_runs= 0
            print ("-----------------------------------------------")
            print (f"{tchoice} Batting-\n")
            while no_of_chances_2 < chances_2:
            
                bowl= int(input(f"Enter Runs for your Bowling Turn: "))
                comp_bat= r.choice(lst2)           
                if comp_bat==bowl:
                    print (f"{tchoice} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"The {tchoice} is Out. {tchoice} Runs= ",comp_runs,"\n")
                    break
                else:
                    comp_runs= comp_runs+comp_bat
                    print (f"{tchoice} Guess: ",comp_bat,f"your Guess: ",bowl)
                    print (f"{tchoice} Runs: ",comp_runs,"\n")           
                    if comp_runs > your_runs:
                        break
                    
                    no_of_chances_2= no_of_chances_2+1         
                    print ("\n-----------------------------------------------\nRESULTS: ")         
            if comp_runs < your_runs:
                print (f"\n{myteam} won the Game.\n\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoice} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")         
                print("Congrats you have been sent to semi finals")
                ascii_banner = pyfiglet.figlet_format(" Semi finals-")
                print(ascii_banner, end="")
                qtoss()
            elif comp_runs == your_runs:
                print ("The Game is a Tie") 
                ascii_banner = pyfiglet.figlet_format(" tie-")
                print(ascii_banner, end="")    
                qtie()   
            else:
                print (f"\n{tchoice} won the Game.\n\n{tchoice} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]",f"\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                print(ascii_banner, end="") 
                cong = ["BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                te = r.choice(cong)
                print(te)
def lose():
        teams = ["RCB","CSK","SRH","RR","DC","PK","MI","KKR"]
        lst2= [1,2,3,4,5,6,7,8,9,10]
        chancese= 20
        no_of_chances_2= 0
        comp_runs= 0
        your_runs= 0
        chances_1= 20
        no_of_chances_1= 0
        lst1 = [1,2,3,4,5,6,7,8,9,10]
        print ("-----------------------------------------------")
        print (f"{tchoice} Batting-\n")
        while no_of_chances_2 < chancese:
            bowl= int(input("Enter Runs for your Bowling Turn: "))
            comp_bat= r.choice(lst2)
            if comp_bat==bowl:
                print (f"{tchoice} Guess: {comp_bat}{teams} Guess: ",bowl)
                print (f"The {tchoice} is Out. {tchoice} Runs= ",comp_runs,"\n")
                break
            else:
                comp_runs= comp_runs+comp_bat
                print (f"{tchoice} Guess: ",comp_bat,"your Guess: ",bowl)
                print (f"{tchoice} Runs: ",comp_runs,"\n")

            if comp_runs > your_runs:
                    break
                
            

        print ("-----------------------------------------------\nyour Batting\n")
        while no_of_chances_1 < chances_1:
            no_of_chances_2= no_of_chances_2+1
            runs= int(input(f"Enter Runs for {myteam} Batting Turn: "))
            comp_bowl= r.choice(lst1)

            if runs==comp_bowl:
                print (f"your Guess: ",runs,f",{tchoice} Guess: ",comp_bowl)
                print (f"{myteam} are Out. your Total Runs= ", your_runs,"\n")
                break
            elif runs>10:
                print ("ALERT!! Support No only till 10\n")
                continue
            else:
                your_runs= your_runs+runs
                print (f"your Guess: {runs},{tchoice} Guess: {comp_bowl}")
                print ("your runs Now are: ",your_runs,"\n")       
            no_of_chances_1= no_of_chances_1 + 1  

        

        print ("\n-----------------------------------------------\nRESULTS: ")

        if comp_runs < your_runs:
                print (f"\n{myteam} won the Game.\n\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]",f"\n{tchoice} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]\n")         
                print("Congrats you have been sent to semi finals")
                ascii_banner = pyfiglet.figlet_format(" Semi finals-")
                print(ascii_banner, end="")
                qtoss()
        elif comp_runs == your_runs:
                print ("The Game is a Tie") 
                ascii_banner = pyfiglet.figlet_format(" tie-")
                print(ascii_banner, end="")    
                qtie()   
        else:
                print (f"\n{tchoice} won the Game.\n\n{tchoice} Total Runs= ",comp_runs,"  [Bowls Taken(Out of 20): ",no_of_chances_2+1,"]",f"\nyour Total Runs= ",your_runs,"  [Bowls taken(Out of 20): ",no_of_chances_1+1,"]\n")
                ascii_banner = pyfiglet.figlet_format(" YOUR ELIMINATED")
                print(ascii_banner, end="") 
                cong = ["BETTER LUCK NEXT TIME","CLOSE BUT NO CIGAR"]
                te = r.choice(cong)
                print(te)
print(f"{tchoice}  VS  {myteam}\n")
choice =  input("Please choose odd(o) or even(e) :- ")
print(f"{tchoice} chose a number")
comp = r.randint(1,10)
your =int(input("Please Enter a Number between 1 and 10 *to determine the toss* : ")); 
tvalue= comp+your
print(f"the {tchoice} chose:- {comp}")
print(f"{myteam} chose:- {your}")
print(f"{comp}+{your}={tvalue}") 
if choice == "e":
    if tvalue%2==0:
        print(f"{myteam} WON") 
        pitch = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2) :- ")) 
        if pitch == "1":
            print(f"{myteam} won the toss and chose to BAT")
            won()
        if pitch == "2":
            print(f"{myteam} won the toss and chose to BALL")
            lose()
    else:  
           print(f"{myteam} LOSE")
           pitch = "2"
           my_list = [won,lose]
           r.choice(my_list)()
if choice == "o":     
        if(tvalue&1==1):
            print(f"{myteam} WON") 
            pitch = str(input("Please choose if u want to BAT🏏(1) or BALL⚾(2)"))
            if pitch == "1":
                print(f"{myteam} won the toss and chose to BAT")
                won()
            if pitch == "2":
                print(f"{myteam} won the toss and chose to BALL")
                lose()
        else:  
                print(f"{myteam} LOSE")
                pitch = "2"
                my_list = [won,lose]
                r.choice(my_list)()