# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Иван")
default mood = False
default health = True
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "Дзынь, дзынь..."
    me "Черт, уже..."
    me "Ай, как башка трещит..."
    me "Где эта банка с огурцами"
    menu:
        "Пойти за огурцами":
            jump crash
        "Забить":
            jump notCrash
    label crash:
        $ mood = False
        $ health = True
        "Ты споткулся об кота"
        "Настроение испортилось, но, найдя огурцы, ты вылечил голову"
    label notCrash:
        $ mood = False 
        $ health = False
        me "Эх, тяжело будет"
    # This ends the game.




    return
