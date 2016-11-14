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

    dictA = letterFrequency(a)
    print(dictA)
    dictB = letterFrequency(b)
    print(dictB)

makingAnagrams("abbc", "cde")
