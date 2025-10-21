# Wordlist file taken from https://github.com/emadshanab/WordLists-20111129/blob/master/Directories_All.wordlist


def wordlist_function(filename):
    wordlist_file = open(filename,'r')
    wordlist = []
    for lines in wordlist_file:
        wordlist.append(lines.strip())
    return wordlist

