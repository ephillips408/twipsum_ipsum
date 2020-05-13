import itertools
from random import randint

def format_text(text_data):
    # This function splits the text data into a list of words.
    for tweet_number in range(0, len(text_data)):
        text_data[tweet_number]['text'] = text_data[tweet_number]['text'].split(' ')
        # del text_data[tweet_number]['text'][-1] This line was originally test with the TheAtantic account. Not needed for others
    return text_data

def create_words_list(text_data):
    # This function creates a list of the words that are present in the tweets
    word_list = []
    for tweet in range(0, len(text_data)):
        word_list.append(text_data[tweet].values()) # The text data is a list of dicts, and the vals are a list of words.
    word_list = list(itertools.chain.from_iterable(word_list)) # This flattens the dictvalues to a list of lists
    word_list = list(itertools.chain.from_iterable(word_list)) # This flattens the lists of lists to a list of the words
    return word_list

def remove_links(list_of_words):
    # Remove the links from the words list instead. This accounts for a very large number of sentences, and removes nested loops.
    # Iterate over the list in reverse order to prevent skipping issues.
    for word in range(len(list_of_words) - 1, -1, -1):
        if list_of_words[word][0:8] == "https://": del list_of_words[word]
    return list_of_words

def word_selection(sen_lengths, words):
    ipsum_sentences = [ [] for i in range(len(sen_lengths)) ] # Creates a list of empty lists of len(sen_lengths)
    for sents in range(len(ipsum_sentences)):
        for rand_words in range(sen_lengths[sents]): # sen_lengths[sents] is the sentence length provided by num_of_sentences list
            ipsum_sentences[sents].append(words[randint(0, len(words) - 1)])
            # /\ This appends each list in ipsum_sentences with a random word from words.
    # print (ipsum_sentences)
    return ipsum_sentences

def make_sentences(list_of_sentences):
    for sentence_num in range(len(list_of_sentences)):
        list_of_sentences[sentence_num][0] = list_of_sentences[sentence_num][0].capitalize()
        #\/ Adds a period at the end of every sentence.
        list_of_sentences[sentence_num][len(list_of_sentences[sentence_num]) - 1] = list_of_sentences[sentence_num][len(list_of_sentences[sentence_num]) - 1] + '. '
        list_of_sentences[sentence_num] = ' '.join(list_of_sentences[sentence_num]) # Makes the individual words in each list into one string
    list_of_sentences = ''.join(list_of_sentences) # Makes the list one string
    return list_of_sentences
