print("\nFou were digging a hove in your yard and accidently you stumble upon an old box.")
a = int(input("What will you do. press \n1.Open the box.\n2.Ignor the box.\n"))
if a==1 :
    print("\nYou decided to open the box. In the box you found a map that indicates a treasure.")
    a = int(input("What will you do \n1.Follow the map and find the treasure.\n2.Throw away the map.\n"))
    if a ==1:
        print("\nYou decided to follow the map.\nYou reached to the landmarks indicated in the map. The treasure in the old ruins to which no we comes. It is suranded by the water. To reach the ruins you have to cross the road.")
        a = int(input("How will you cross the water.\n1.Take the boat at the bank.\n2.Swim to the ruins\n"))
        if a == 2:
            print("\nYou successfully reached the ruins. You enter the ruins from a norrow path which is made of tiles. The tiles look suspecious.")
            a = int(input("What will you do\n1.Run straight through the path.\n2.Check for the trapes.\n"))
            if a==2:
                print("\nYou Decided to check for the trapes and found that the tiles are just a trap. You started looking for a different path. You saw a liver on the wall.")
                a = int(input("What will you do\n1.Ignore the liver and search for a differnt option.\n2.Pull the liver\n"))
                if a ==1:
                    print("\nYou decided to not pull the liver and check for the other clues. After not finding another clue you decided to give up on serching another clue and pull the liver.\nWith disappointment you lean on the wall. The wall in that placed moved in just as if it was a button.")
                    a = int(input("What will you do.\n1.Press the button.\n2.Pull the liver.\n"))
                    if a == 1:
                        print("\nYou decided to push the button. The walls moved and opened a new path. you moved on the path and saw the treasure box. But the box is on a piller which emerges from a deep dark pit and there is no way to get their. You decided to look for a clue to get there. You stumble uppon a liver.")
                        a = int(input("What will you do\n1.Ignore the liver and search for a differnt option.\n2.Pull the liver\n"))
                        if a == 1:
                            print("\nYou decided to ignore the liver as this might be a trap and looked for some other clue's. You searched for some time and were not able to find anything. You got frustreted after being unable to find any other clue and in frustration you threw the stone towards the treasure box. After that you tried to destrou a statue on your side. As you hit the statue it fell and reveled a hidden liver. This time you decided to press it. A sudden rumbling started to occur and suprisingly a path appered to the chest.")
                            a = int(input("What will you do.\n1.Go on the path.\n2.Check weather its a trap.\n"))
                            if a == 1:
                                print("\nYou decided to go on the path and successfully reached to the treasure box. Finally you got the treause.\nThe End.")
                            else:
                                print("\nYou decided to check if its another trap but this time it's not a trap. So you finally decided to go on the path and successfully reached to the treasure box. Finally you got the treause.\nThe End")
                        else : 
                            print("\nYou decided to pull the liver. You hear some rumbleling you decided to go after the voice. But it turns out that the noise was from the wild animels that come in the ruind because the liver opened the dor. You tried to run away but you were't fast enough. The wild animals caught you and killed you.\nThe End.")
                    else : 
                        print("\nYou decided to pull the liver only to find out that it was another trap. The ground below opened and you died form fall.\nThe End")
                else : 
                    print("\nYou decided to pull the liver only to find out that it was another trap. The ground below opened and you died form fall.\nThe End")
            else : 
                print("\nYou decided to run through the path and triggered one of the trapes. You got killed by the arrows.\nThe End.")
        else : 
            print("\nYou decided to take the boat. You entered in the boat and got bitten by a very poisonous snake. There was no one to help and you died in the boat.\nThe End.")
    else:
        print("\nYou decided to throw the map and a person passing by found's the map. He followed the map and got the treasure. You came to find out about and now you regrate throwing the map.\nThe End.")
else : 
    print("\nYou decided to ignore the box and went to your daily routine.\nThe End.")
