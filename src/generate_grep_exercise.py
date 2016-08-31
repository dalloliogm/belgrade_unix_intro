import string,random
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
try: 
    from tutorial_text import *
except ImportError:
    from src.tutorial_text import *


def random_string(length=80, alphabet='chars'):
    """
    Generate a random string, to create the base file

    @alphabet: 
        'chars': random letters and numbers (excluding number 2)
        'dna' : 'ACTGN'

    """
    if alphabet == 'chars':
        characters = string.ascii_letters + '013456789' + ' '
    else:
        characters = 'ACTGN'
    return ''.join(random.SystemRandom().choice(characters) for _ in range(length))

def random_sequences(nseqs=50, message = 'this\nis\na\ntest\nmessage', label='AAACTTT'):
    """
    Generate random fasta sequence records, and add an hidden message at a given position
    """
    seq_len = 30
    seqs = [SeqRecord(
        Seq(random_string(seq_len, 'dna'), alphabet=generic_dna), 
        id='seq{0:03}'.format(i), name='seq{0:03}'.format(i), 
        description = 'sequence description') for i in range(nseqs)]

    # TODO: include hidden message
    print('dasda')
    message_l = message.split()

    newlines_index = sorted(random.sample(range(2, len(seqs)), len(message_l)))
    counter = 0
    for msg_line in message_l:
        if type(label) == type([]): # Multiple label messages (e.g. IgnoRecAse)
            current_label = random.choice(label)
        else:
            current_label = label
#        print current_label

        current_seq = seqs[newlines_index[counter]]
        counter += 1
        print (current_seq)
        desc = current_seq.description
        seq = current_seq.seq
        new_desc = desc + '      ' + msg_line
        label_index = random.randint(0, seq_len - len(current_label))
        new_seq = seq[0:label_index] + current_label + seq[label_index+len(current_label):]

        current_seq.seq = new_seq
        current_seq.description = new_desc

#    print (newlines_index)

#    SeqIO.write(seqs, open('data/sequences.fasta', 'w'), format='fasta')
    
    return seqs



def generate_basefile(lines=400):
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
    for msg_line in message_l:

        if type(label) == type([]): # Multiple label messages (e.g. IgnoRecAse)
            current_label = random.choice(label)
        else:
            current_label = label
#        print current_label

        baseline = random_string(40) + '    ' + random_string(35) + '\n'
        label_index = random.randint(0, 40-len(current_label))
        newline = baseline[0:label_index] + current_label + baseline[label_index+len(current_label):40] + '    ' + msg_line
        
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
        output = generate_basefile(lines=40)
        if n == 32:
            output = hide_message(output, multiplefiles_message.text,
                    multiplefiles_message.label, 0, 30)
        f = open("data/multiplefiles/file" + str(n) + '.txt', 'w')
        f.write(output)
        f.close()

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
    print ("generating main tutorial")
    generate_tutorial(tutorial_messages)
#    print ("generating grep * exercise")
#    generate_multiplefiles()
    print ("generating random fasta sequences")
    random_sequences()

