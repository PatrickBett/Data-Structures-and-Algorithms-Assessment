import re

def word_frequency(sentence):
    # Remove all characters that are not words or whitespaces from the sentence using regex
    clean_sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    
    # Use split to convert cleaned sentence to a list
    sentence_array = clean_sentence.split()

    # map each word and it's frequency in a dict
    word_frequency_dict = dict()
    for word in sentence_array:
        word_frequency_dict[word] = word_frequency_dict.get(word, 0) + 1

    return word_frequency_dict

# Test case
sentence = "This is a test sentence. This sentence is a test. This sentence is a test."
result = word_frequency(sentence)
print(result)     