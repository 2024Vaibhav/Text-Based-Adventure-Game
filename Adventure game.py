print("Hi, welcome to my new Adventure Game.")
print("This is a story based game which will thrill you all at every moment.")
print("Just imagine the story in your mind and Play it.")
print("In this game you are  travelling in the jungle and suddenly you lost in jungle, and After moving around for 3 hours you felt hungry and there is nothing to eat in that jungle. ")
print("Then you feels like it is  hunted jungle because the behavior of your surrounding is not good at all. And it is going to be evening very soon.")
print("And then after some time you suddenly  see a  bungalow in between the jungle. But the Bungalow is not giving you that good vibe.") 
print("But you don’t have any other choice from entering the house.")
print("After you enter the house you feel that the house is empty from many years but then you see three doors in the hall.")
print("The three doors look like new but the whole bungalow  is looking very poor from outside.")
print("You are very hungry and you have to enter in any one room because there was nothing in that entire house except those three room.")
print("And now its your turn to Choose the room to Enter-")
print("1. Frist Room \n2. Second Room \n3. Third Room")
RoomChoice = input(">  ")
if(RoomChoice == "1"):
    print("As you selected the First Room.\nYou've entered in the bedroom.\nThere is  only one bed and one almirah in that room and the door is lock from outside. ")
    print("So now you have only two Option-\nA..Sleep on that bed.\nB.Open Almirah and find Jungle map!")
    Select = input(">  ")
    if(Select=="A"):
        print("As you choose to sleep on bed.\nNow you will sleep and die from hunger because door is locked permanently.")
        print("OOPS!\nYOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
    elif(Select == "B"):
       print("Now you are going to open the almirah and find the MAP inside.\nAs you open the almirah you find that  there is a body of a child in  which is  two pieces and the child still moving.\nSo you understand that the chil is ghost.\nAnd you are dead now .\nThe ghost killed you.")
       print("YOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
    else:
       print(" YOU HAVE CHOOSEN THE WRONG OPTION!!. CHOOSE THE ABOVE OPTION CAREFULLY .")
elif(RoomChoice == "2"):
    print("As you selected the Second Room.\nYou've entered in the kitchen.\nIn kitchen there was a Fridge and some Utensils and a Small Door.\nNow you have two option-\nA.Open the Fridge to find something to eat.\nB.Open that small door and go inside.")
    Option = input(">  ")
    if(Option == "A"):
        print("Now you are going to open that Fridge.\nThe Fridge have some bodyparts of a different people. and now you understand that someting is wrong in that place.\nAnd the kitchen door is locked from outside.\n So now you have only two option-\n.A.Open that small door and go inside.\nB.Wait in that kitchen and die with hunger.")
        Select = input(">  ")
        if(Select == "A"):
           print("when you go inside the small door you will find that there was a cannibal sleeping.\nAnd after you enter in  his room he woke up.\nNow he will cut you into small peices and eat you.")
           print("YOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
        elif(Select == "B"):
           print("As you  wanted to wait inside the kitchen.\nAnd now you will be die with hunger.")
           print("YOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
        else:
           print(" YOU HAVE CHOOSEN THE WRONG OPTION!!. CHOOSE THE ABOVE OPTION CAREFULLY .")
    elif(Option == "B"):
       print("when you go inside the small door you will find that there was a cannibal sleeping.\nAnd after you enter in  his room he woke up.\nNow he will cut you into small peices and eat you.")
       print("YOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
    else:
        print(" YOU HAVE CHOOSEN THE WRONG OPTION!!. CHOOSE THE ABOVE OPTION CAREFULLY .")
elif(RoomChoice == "3"):
   print("As you selected the thrid room.\nYou've entered in the store room.\nThere is a table and some useless things in the store room.\nThere are some books, file and some Maps on that table but also a Pitbull Dog is Sleeping Under the Table.\nAnd the Door is locked from outside So you can't leave the room.")
   print("So Now you have only two option-\nA. Go near the table and find the Map.\nB. Kill your self before the Pitbull Wakes up.")
   Option = input(">  ")
   if(Option == "A"):
      print("Go near the table and Find the map Silently before the Pitbull Woke up.")
      print("Hurray!! you found the Map of Jungle.")
      print("YOU WON THE GAME !! ")
   elif(Option == "B"):
      print("As you choose to kill yourself.\nNow you are dead.\nSo Now the Dog will enjoy his meal!")
      print("YOU LOST THE GAME!\nBETTER LUCK NEXT TIME!!")
   else:
      print(" YOU HAVE CHOOSEN THE WRONG OPTION!!. CHOOSE THE ABOVE OPTION CAREFULLY .")
else:
 print("Invalid Choice Please select from 1,2,3")