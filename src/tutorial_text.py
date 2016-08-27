

class TutorialMessage:
    '''
    Define a tutorial message

    Using a class is a bit more organized than a dictionary,
    because we make sure that each element has the same structure
    '''
    def __init__(self, index, label, filename, text):
        self.label      = label
        self.filename   = filename
        self.text       = text
        self.index      = index

tutorial_messages = [
        TutorialMessage(0, 'start', 'data/exercise1_grep.txt', """
 ______________________________
/ Congrats!                    \ 
|  You've used grep correctly, |
\  and found a cow.            /
 ------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||



    The command grep allows to search for a pattern in a text file.
    It will print all the matching lines to the screen.

    =================
    Next Exercise
    =================

    In the next exercise we will see how to access grep's documentation.

    Grep the following word to continue:

                 | |                  
               __| |  ___    ___  ___ 
              / _` | / _ \  / __|/ __|
             | (_| || (_) || (__ \__ \ 
              \__,_| \___/  \___||___/

"""),
    TutorialMessage(1, 'docs', 'data/exercise1_grep.txt', """
    The documentation for grep can be accessed through man:

        $: man grep
    
    Scroll down to see all the parameters for grep and their description.

    Use / to search for text.
    Press the q key to exit.



    ==============
    Next exercise
    ==============

    There is an option in grep to do case-insensitive searches.

    Grep this document again, searching for the long form of that option.

    Note that you will need to quote it using single quotes, e.g.:

        $: grep '--my-option' data/exercise1_grep.txt

    """
    ),
    TutorialMessage(2, '--ignore-case', 'data/exercises1.grep', '''
        
    Case insensitive

    ''')
    ]

