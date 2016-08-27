import string,random
import re
from tutorial_text import *
#from src.tutorial_text import *


def random_string(length=80):
    """
    Generate a random string, to create the base file
    """
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + ' ') for _ in range(length))

def generate_basefile(lines=100):
    """
    Generate a base file, filled with random characters, in two columns
    """

    output = ""

    for x in range(lines):
        output += random_string(40) + '    ' + random_string(35) + '\n'

    return output

def hide_message(inputtext, message = '', marker = 'MRK1'):
    """
    Given an input text (from a file) and a marker keyword, hide a message in it.

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

    newlines_index = sorted(random.sample(range(len(output)), len(message_l)))

    counter = 0
    for msg in message_l:
        baseline = random_string(40) + '    ' + random_string(35) + '\n'
        marker_index = random.randint(0, 40-len(marker))
        newline = baseline[0:marker_index] + marker + baseline[marker_index+len(marker):40] + '    ' + msg
        
        current_newline_index = newlines_index[counter]
        counter += 1
        output.insert(current_newline_index, newline)

    output = '\n'.join(output)
    return output


def generate_tutorial(tutorial_messages):
#    outputfiles = [generate_basefile() for x in range(2)]
    outputfile = generate_basefile()

    for x in range(len(tutorial_messages)):
        current_message = tutorial_messages[x]
        if type(current_message.label) == type([]):
            label = random.choice(current_message.label)[0]
        else:
            label = current_message.label
        
        outputfile = hide_message(outputfile, current_message.text, label)

    f = open('data/exercise1_grep.txt', 'w')
    f.write(outputfile)
    f.close()


if __name__ == '__main__':
    generate_tutorial(tutorial_messages)

