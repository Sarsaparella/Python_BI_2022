# List of dictionaries for translating sequences #

complement_dna = {'A':'T', 'T':'A', 'G':'C', 'C':'G',
                  'a':'t', 't':'a', 'g':'c', 'c':'g'}

complement_rna = {'A':'U', 'U':'A', 'G':'C', 'C':'G',
                  'a':'u', 'u':'a', 'g':'c', 'c':'g'}

transcribe_dna_to_rna = {'A':'A', 'T':'U', 'G':'G', 'C':'C',
                         'a':'a', 't':'u', 'g':'g', 'c':'c'}

transcribe_rna_to_dna = {'A':'T', 'U':'A', 'G':'C', 'C':'G',
                         'a':'t', 'u':'a', 'g':'c', 'c':'g'}

allowed_symbols = ['A', 'T', 'G', 'C', 'U',
                   'a', 't', 'g', 'c', 'u']

# List of commands #

def complement(sequence):
    if any(U in sequence for U in ['U', 'u']):
        for nucleotide in sequence:
            decoded.append(complement_rna[nucleotide])
    else:
        for nucleotide in sequence:
            decoded.append(complement_dna[nucleotide])
    return(''.join(decoded))

def transcribe(sequence):
    if any(U in sequence for U in ['U', 'u']):
        print('Warning: This is RNA! Transcribing RNA to DNA!')
        for nucleotide in sequence:
            decoded.append(transcribe_rna_to_dna[nucleotide])
    else:
        for nucleotide in sequence:
            decoded.append(transcribe_dna_to_rna[nucleotide])
    return(''.join(decoded))

def reverse(sequence):
    reversed = sequence[::-1]
    return(''.join(reversed))

def reverse_complement(sequence):
    reversed = reverse(sequence)
    reversed_n_complemented = complement(reversed)
    return(reversed_n_complemented)

help_txt = """List of commands:
◉ complement - complements your sequence
◉ transcribe - transcribes your DNA into RNA and RNA into DNA
◉ reverse - reverses your sequence
◉ reverse complement - reverses and complements your sequence
◉ exit - exit from script
◉ help - shows you list of commands"""

allowed_commands = {'complement':complement,
                    'transcribe':transcribe,
                    'reverse':reverse,
                    'reverse complement':reverse_complement,
                    'help':help}


# Script #

command = input('Hello! Type your command here (づ◡﹏◡)づ ')
while command != 'exit':
    decoded =[]                                                                 
    if command == 'help':
        print(help_txt)
        command = input('Type your command here (づ◡﹏◡)づ ')
        continue
    if command not in allowed_commands:
        print('╮( ˘_˘ )╭ \n Wrong command! Try again or type help for list of commands')
        command = input('Type your command here (づ◡﹏◡)づ ')
        continue
    else:                                                                       
        sequence = input('Enter sequence (づ◡﹏◡)づ ')
        sequence = [x for x in sequence]
        if not all(nucleotide in allowed_symbols for nucleotide in sequence):
            print('╮( ˘_˘ )╭ \nThis is not nucleotide sequence. Try again.')
            continue
        if ('U' in sequence or 'u' in sequence) and ('T' in sequence or 't' in sequence):
            print('╮( ˘_˘ )╭ \nThis is impossible. Sequnce can not have U and T nucleotides simultaneously.')
        else:
            print(allowed_commands[command](sequence))
            command = input('Type your command here (づ◡﹏◡)づ ')
            continue

print('Bye-bye!')
