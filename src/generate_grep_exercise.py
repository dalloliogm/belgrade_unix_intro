import string,random
import re
from tutorial_text import *
#from src.tutorial_text import *


def random_string(length=80):
    """
    Generate a random string, to create the base file
    """
    return ''.join(random.SystemRandom().choice(string.ascii_letters + '013456789' + ' ') for _ in range(length))

def generate_basefile(lines=100):
    """
    Generate a base file, filled with random characters, in two columns
    """

    output = ""

    for x in range(lines):
        output += random_string(40) + '    ' + random_string(35) + '\n'

    return output

def hide_message(inputtext, message = '', label = 'MRK1', minline=0, maxline=None):
    """
    Given an input text (from a file) and a label keyword, hide a message in it.

    >>> import random
    >>> random.seed(0)
    >>> inputtext = 'dasdasdaxczfdasdas\nddPddasdasdasxczndsadasdas\nfsdfsddasdasdasddPf'

    >>> hide_message (inputtext, "hello\nworld", "MRK1")
    dasdasdaxczfd asda sdsadasdas
    ddPddasdasdAasxc zndsadasdas2
    dasdadaMRK1s zewrfzddas hello
    fsdfsddasdasdsa D12 dadasddPf
    dasd dqw d213 asddaas1e world
    
    Grep this file for the word "MRK1" to get the message
    """

    message_l = re.split('\n', message)
    output = re.split('\n', inputtext)

    if maxline is None:
        maxline = len(output)
    
    newlines_index = sorted(random.sample(range(minline, maxline), len(message_l)))
#    print label, newlines_index

    counter = 0
    for msg in message_l:

        if type(label) == type([]): # Multiple label messages (e.g. IgnoRecAse)
            current_label = random.choice(label)
        else:
            current_label = label
#        print current_label

        baseline = random_string(40) + '    ' + random_string(35) + '\n'
        label_index = random.randint(0, 40-len(current_label))
        newline = baseline[0:label_index] + current_label + baseline[label_index+len(current_label):40] + '    ' + msg
        
        current_newline_index = newlines_index[counter]
        counter += 1
        output.insert(current_newline_index, newline)

    output = '\n'.join(output)
    return output

def generate_multiplefiles():
    """
    Generate multiple files for the grep * exercise.
    """
    for n in range(50):
        f = generate_basefile(lines=200)
        if n == 32:
            print

def generate_tutorial(tutorial_messages, outputfile='data/exercise1_grep.txt'):
#    outputfiles = [generate_basefile() for x in range(2)]
    output = generate_basefile()

    for x in range(len(tutorial_messages)):
        current_message = tutorial_messages[x]
        output = hide_message(output, current_message.text, 
                current_message.label, current_message.minline, current_message.maxline)

    f = open(outputfile, 'w')
    f.write(output)
    f.close()


if __name__ == '__main__':
    generate_tutorial(tutorial_messages)

