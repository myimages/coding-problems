class hash_table:

    def __init__(self):
        """"
        Initializes a hash table. Size of hash table (currently 1009) must be a prime number.
        """
        self.table = [None] * 1009

    def key_to_index(self, key, M):
        """
        Converts a string key into an array index for an array of size M.

        PARAMETERS
        key: String, alphabet only, case-sensitive, no space
        M: Int
        RETURNS
        hash_index: Int, an index into the hash table based on the key
        """
        hash_index = 0
        # 31 can be changed for another small, prime number
        # Formula for conversion of a string of characters into an index into a hash table.
        # i ensures that anagrams don't all map to the same index by giving each letter a positional weight.
        i = 1
        for c in key:
            hash_index = hash_index*i + ord(c)
            i += 1
        assert hash_index >= 1
        return(hash_index % M)

    def add_word(self, word):
        """
        Adds a word to the hash table
        PARAMETERS
        word: String, alphabet only, case-sensitive, no space
        """
        hash_index = self.key_to_index(word, len(self.table))
        assert hash_index <= len(self.table)
        # If there currently isn't a word located at that hash index, create a new list to place in that index.
        if self.table[hash_index] is None:
            l = []
            l.append(word)
            self.table[hash_index] = l
        else:
            assert type(self.table[hash_index]) is list
            self.table[hash_index].append(word)

    def add_sentence(self, sentence):
        """
        Takes a sentence either in the form of a list or string and ensures each word (separated by spaces) is added to the hash table.
        PARAMETERS
        sentence: String, alphanumeric, words spaced out with " " OR list with 1 word in each cell.
        """
        if (type(sentence) is str):
            words = sentence.split(" ")
        else:
            words = sentence
        for word in words:
            self.add_word(word)

    def search_for_word(self, word):
        """
        Searches if a word is in the hash map. If so, removes the word from the hash map.
        PARAMETERS
        word: String, alphanumeric, no " "
        RETURNS
        True: If word is contained in the hash map, then removes the word from the hash map
        FALSE: If word is not contained in the hash map
        """
        hash_index = self.key_to_index(word, len(self.table))
        # hash_index contains the key to which the word would be located if it did exist
        # If it doesn't, the array at that location will be set to None
        assert hash_index <= len(self.table)

        if self.table[hash_index] is None:
            return False
        else:
            for item in self.table[hash_index]:
                if word == item:
                    # Remove item from hash table
                    # This is because once we use a word for our ransom note, we can't use it again.
                    # I tested to make sure that if there are duplicates of a string in a list .remove will only remove a single version of the item
                    if len(self.table[hash_index]) == 1:
                        self.table[hash_index] = None
                    else:
                        self.table[hash_index].remove(item)
                    return True
            return False

    def search_for_sentence(self, sentence):
        """
        Takes a sentence and checks whether each word in that sentence is located in the hash map
        PARAMETERS
        sentence: Either a String with the words spaced by " " or a list with one word per cell
        RETURNS
        True: If each word in the sentence is located in the hash map. If there are two copies of the word in the sentence, there must be two copies in the hash map.
        False: If there is at least one word in the sentence which isn't located in the hash map.
        """
        if (type(sentence) is str):
            words = sentence.split(" ")
        else:
            words = sentence
            for word in words:
                isThere = self.search_for_word(word)
                if isThere == False:
                    return False
            return True

    def print_table(self):
        print(self.table)


def ransom_note(magazine, ransom):
    """"
    Assesses if we can take a subset of the words in magazine in order to build ransom. Uses a hash map to accomplish this.
    PARAMETERS
    magazine: A string of words separated by " "  or a list where each cell contains one word. We use the words in magazine to build the string ransom.
    ransom: A string words separated by " " or a list where each cell contains one word
    RETURNS
    True: If each word in ransom appears exactly once in magazine.
    False: If there's at least one word in ransom which does not appear in magazine.
    """
    h_table = hash_table()
    h_table.add_sentence(magazine)
    return(h_table.search_for_sentence(ransom))

answer = ransom_note("o l x imjaw bee khmla v o v o imjaw l khmla imjaw x", "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o")
if (answer):
    print("Yes")
else:
    print("No")
