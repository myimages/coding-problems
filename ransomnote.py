class hash_table:

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

        return(hash_index % M)

    def add_word(self, word):
        hash_index = self.key_to_index(word, len(self.table))
        if self.table[hash_index] is None:
            l = []
            l.append(word)
            self.table[hash_index] = l
        else:
            self.table[hash_index].append(word)

    def add_sentence(self, sentence):
        words = sentence.split(" ")
        for word in words:
            self.add_word(word)

    def search_for_word(self, word):
        hash_index = self.key_to_index(word, len(self.table))

        if self.table[hash_index] is None:
            return False
        else:
            for item in self.table[hash_index]:
                if word == item:
                    return True
            return False

    def search_for_sentence(self, sentence):
        words = sentence.split(" ")
        for word in words:
            isThere = self.search_for_word(word)
            if isThere == False:
                return "No"
        return "Yes"

    def print_table(self):
        print(self.table)

    def __init__(self):
        self.table = [None] * 1009

#def ransom_note(magazine, ransom):


h_table = hash_table()
h_table.add_sentence("give me one grand today tonight")
print(h_table.search_for_sentence("give one grand"))
print(h_table.search_for_sentence("lawl give"))
