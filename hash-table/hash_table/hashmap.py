from hash_table.hashtable import HashTable
import re

def repeated_word(text):
    """
        A function that accepts a string, and returns the first word that occurs more than once.
        Args:
            text (str): Any string.
        Returns:
            str: The first word that is repeated in among the words found in the passed string.
    """
    ht = HashTable()
    words = list(map(lambda word : word.lower(), re.findall(r"\w+", text)))
    if len(list(words)) <= 1:
        raise Exception("String provided contains an invalid number of keys.")
    for word in words:
        if ht.contains(word):
            return word
        ht.set(word, None)
    return 

if __name__=="__main__":

    text1 = "Once upon a time, there was a brave princess who..."
    text2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    text3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(repeated_word(text1))
    print(repeated_word(text2))
    print(repeated_word(text3))