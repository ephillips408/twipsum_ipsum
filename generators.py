from random import randint

def num_of_sentences(int):
    lengths = []
    for sentences in range (0, int):
        lengths.append(randint(14,22)) # Average length of US English sentence is 20 words according to Google
    # \/ A list of random numbers from 14 through 22, and len(lengths) is the int in the input.
    return lengths
