import string,random
import re


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

    message_l = message.splitlines()
    output = inputtext.splitlines()

    newlines_index = sorted(random.sample(range(len(output)), len(message_l)))

    for msg in message_l:
        baseline = random_string(40) + '    ' + random_string(35) + '\n'
        marker_index = random.randint(0, 40-len(marker))
        newline = baseline[0:marker_index] + marker + baseline[marker_index+len(marker):40] + '    ' + msg
        output.insert(0, newline)

    output = '\n'.join(output)
    return output

if __name__ == '__main__':
    file1 = generate_basefile()
    print(hide_message(file1, "hello\nworld", "MRK1"))

