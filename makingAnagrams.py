def letterFrequency(s):
    """"
    Given a string, s, returns a dictionary that asseses the letter frequencies in that string in a case-insensitive manner.

    Parameters
    s: String, alphabet letters only

    Returns
    dictS: Dictionary which records all of the letters contained in s, with their frequencies of occurrences in a case-insensitive manner
    """
    s = s.lower()
    uniqueS = set()
    dictS = {}
    # Make a set of the characters in the string with duplicates removed
    # So that we can iterate through the set and count the frequencies of each character, without redoing the count
    for c in s:
        uniqueS.add(c)
    # dictS contains the character frequencies
    for c in uniqueS:
        count = s.count(c)
        dictS[c] = count
    return(dictS)



def makingAnagrams (a, b):
    """
    Given two strings, a and b, determines the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

    Parameters
    a: String, Consists of lowercase English alphabetic letters
    b: String, Consists of lowercase English alphabetic letters

    Returns
    n: Integer, The number of characters you must delete to make the two strings anagrams of each other
    """

    # Returns a dictionary which records the letter frequency of the string
    dictA = letterFrequency(a)
    dictB = letterFrequency(b)
    keysA = set(dictA.keys())
    keysB = set(dictB.keys())
    # Letters in A but not in B
    aKeysOnly = keysA - keysB
    # Letters in B but not in A
    bKeysOnly = keysB - keysA
    # Letters in both a and b
    bothKeys = keysA & keysB

    minForAnagram = 0
    # If the letter only appears in a or b, then it has to be removed for them to be anagrams.
    for aKey in aKeysOnly:
        minForAnagram += dictA[aKey]
    for bKey in bKeysOnly:
        minForAnagram += dictB[bKey]

    # If the letter appears in both a and b, it must appear the same number of times in both
    # If it doesn't, then it must be removed from the string it appears most in, until the strings share an equal frequency
    for abKey in bothKeys:
        if (dictA[abKey] != dictB[abKey]):
            minForAnagram += max(dictA[abKey], dictB[abKey]) - min(dictA[abKey], dictB[abKey])
    return(minForAnagram)

print(makingAnagrams("cde", "abc"))
