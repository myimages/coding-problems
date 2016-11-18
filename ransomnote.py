def key_to_index(key, M):
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
    for c in key:
        hash_index = (31 * hash_index + ord(c)) % M

    return(hash_index)

#def ransom_note(magazine, ransom):

print(hash_string("hello", 1009f))

