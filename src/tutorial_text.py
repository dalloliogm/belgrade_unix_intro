

class TutorialMessage:
    '''
    Define a tutorial message

    Using a class is a bit more organized than a dictionary,
    because we make sure that each element has the same structure
    '''
    def __init__(self, label, text, minline=12, maxline=None):
        self.label      = label
        self.text       = text
        self.minline    = minline
        self.maxline    = maxline

tutorial_messages = [
        TutorialMessage(['start', ' start ', ' start', 'start '], """
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
    TutorialMessage('help', """
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

    """, minline=57, maxline = 178
    ),
    TutorialMessage('ignorecase', '''
        
Remember that, to continue with the exercise, 
you need to do a case-insensitive search for the word''', maxline=20),
    TutorialMessage(['ignOrecase', 'ignorecase', 'IgnorEcase', 'IGNORECASE'], '''
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


    ''', minline=185),
    TutorialMessage('21', '''

Searching in multiple files

Grep can search the same pattern
in more than one file at the same time.

The folder data/multiplefiles/ contains hundreds of different files.

Can you identify the file containing the word "regex"?

    '''), 
    TutorialMessage('regex', '''

Regular Expressions allow to identify complex pattern.

The folder data/fasta/ contains some sequence files.
You can open one of them with less, or do head data/fasta/* to see their contents.

Can you use grep to identify 
all the sequence lines containing 
the nucleotides AAA, followed by any character, and then TTT?

==============
Next Exercise
==============

Use the -B option of grep to identify all the
    ''')
    ]

multiplefiles_message = TutorialMessage('regex', '''

Good! You've found the 
file containing the word "regex"

To continue, 
grep file32.txt data/exercise1_grep.txt

''')
