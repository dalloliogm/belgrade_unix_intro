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
        output += random_string(56) + '    ' + random_string(20) + '\n'

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

    message_l = re.findall("\n", message)
    

if __name__ == '__main__':
    print(generate_basefile())

