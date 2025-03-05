print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    
''')

print("  Welcome to the Treasure Island.")
print("Your mission is to find the treasure.\n")

print("You have heard about this treasure, hidden in a mysterious pine forest from an old story, told to you by your grandpa...\n")
print("You have decided to go through the tall pine forest.")
print("After a hour of walking, the forest parts its way in two ways... one to the left, the other to the right.\n")
direction = input('Which way will you choose? Type "left" or "right"? \n').lower()
if direction == "left":
    print("You kept walking, until you found a mysterious lake.")
    print("In the middle of the river, you can see a small island.")
    print(r'''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    ''')
    print("You have two options:\n 1) Swim to the island.\n 2) Waist time to craft yourself a small boat so that you can travel safely to the island.\n")
    print("What will be your method of transportation?")
    transportation = input('Type "boat" if you want to build a boat or type "swim" if you are willing to take a risk so that you will be the first to the treasure! ').lower()
    if transportation == "boat":
        print(r'''
     _
    /|\
   /_|_\
 ____|____
 \_o_o_o_/
~~ |     ~~~~~
___t_________ 
        ''')
        print("You have arrived on the island, tired from all the rowing.")
        print("You decide to take a quick nap. That nap turned into a long night of sleep.")
        print(r'''
                              z
                             z
                              Z
                    .--.  Z Z
                   / _(c\   .-.     __
                  | / /  '-;   \'-'`  `\______
                  \_\/'/ __/ )  /  )   |      \--,
                  | \`""`__-/ .'--/   /--------\  \
                   \\`  ///-\/   /   /---;-.    '-'
                                (________\  \
                                          '-'
        ''')
        print("You decide to waste no time anymore. After walking for a bit you see a big mansion.")
        print("You don't know which is the correct entrance, since the mansion has 3 entrances. "
              "A red door, a blue door and a yellow door.")
        door = input('Which door will you choose to enter into? '
                     'Type "red" for the red door, "blue" for the blue door, or "yellow" for the yellow one. '
                     'Choose wisely! ').lower()
        if door == "yellow":
            print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
            ''')
            print("Congratulations, you have found the treasure. Your grandpa will be proud of you!")
        elif door == "red":
            print(r'''  
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
            print("Oh no! You entered the wrong door. The room that you are in is on fire.\n Your progress ends here...")
        elif door == "blue":
            print(r'''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')
            print("Yikes! The room is full of beasts. They started chomping onto you. That is a sad way to lose... \n Progress = rip...")
        else:
            print(r'''
             _                   _     _             
| |                 | |   (_)            
| | __ _ _   _  __ _| |__  _ _ __   __ _ 
| |/ _` | | | |/ _` | '_ \| | '_ \ / _` |
| | (_| | |_| | (_| | | | | | | | | (_| |
|_|\__,_|\__,_|\__, |_| |_|_|_| |_|\__, |
                __/ |               __/ |
               |___/               |___/ 
            ''')
            print("You want to trick the game, huh? You think you are smart by not choosing one of the specified doors?")
            print("No way... Bye! GAME OVER...")
    else:
        print(r'''
                 ___
               /`  _\
               |  / 0|--.
          -   / \_|0`/ /.`'._/)
      - ~ -^_| /-_~ ^- ~_` - -~ _
      -  ~  -| |   - ~ -  ~  -
     jgs     \ \, ~   -   ~
              \_|
        ''')
        print("You didn't even get into the river properly before you were pulled down by an octopus and bitten by piranhas. "
              "Better luck next time!")
else:
    print(r'''
    #======================
      =    SAVE ME!         =
      =             -;  /56 =
      = you are   (* o  "   =
      = already   [ O ;     =
      = dead.      \|/"     =
      = /           #       =
      =             |       =
      =            / \      =
      =            |  |     =
      #=====================#
    ''')
    print("You fell into a trap, a hole covered with leafs.")
    print("Your journey to finding the treasure ends here. \n\n"
          "Good luck next time traveler!")
