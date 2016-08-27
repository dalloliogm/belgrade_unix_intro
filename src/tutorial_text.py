

class TutorialMessage:
    '''
    Define a tutorial message

    Using a class is a bit more organized than a dictionary,
    because we make sure that each element has the same structure
    '''
    def __init__(self, label, filename, text, minline=0, maxline=None):
        self.label      = label
        self.filename   = filename
        self.text       = text
        self.minline    = minline
        self.maxline    = maxline

tutorial_messages = [
        TutorialMessage(['start', ' start ', ' start', 'start '], 'data/exercise1_grep.txt', """
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



The command grep allows to search
for a pattern in a text file.

It will print all the matching 
lines to the screen.

=================
Next Exercise
=================

In the next exercise we will see 
how to access grep's documentation.

Grep the following word to continue:
  _            _        
 | |          | |       
 | |__    ___ | | _ __  
 | '_ \  / _ \| || '_ \ 
 | | | ||  __/| || |_) |
 |_| |_| \___||_|| .__/ 
                 | |    
                 |_|  

"""),
    TutorialMessage('help', 'data/exercise1_grep.txt', """
The documentation for grep can 
be accessed through man:

    $: man grep

Scroll down to see all the 
parameters for grep and their description.

Use / to search for text.
Press the q key to exit.



==============
Next exercise
==============

For the next exercise, you will need to open 
grep's documentation and identify two options:

- the option for case-insensitive searches
- the option for counting 
  the number of matching lines, 
  instead of printing them to the screen.

Once you have identified these options, 
do a case-insensitive search on this file for the word 
"ignorecase", then count the number of lines.

    """, minline=27, maxline = 78
    ),
    TutorialMessage('ignorecase', 'data/exercises1.grep', '''
        
Remember that, to continue with the exercise, 
you need to do a case-insensitive search for the word''', maxline=20),
    TutorialMessage(['ignOrecase', 'ignorecase', 'IgnorEcase', 'IGNORECASE'], 'data/exercises1.grep', '''
 _____________
/ Good Job!   \ 
| You did a   |
| case-insens |
| itive       |
\ search      /
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\ 
                ||----w |
                ||     ||


    ''', minline=80),
    TutorialMessage('21', 'data/exercises1.grep', '''

    Regular Expressions

    '''), 
    TutorialMessage('multiple files', 'data/exercises1.grep', '''

    Multiple files

    ''')
    ]

