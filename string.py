
# This program is finding the most common letter.


A = 'abcaddeffgiiaddca'
B = 'fghijklmmnoppqqfffgiii'
C = 'lmnoopmqzzzzzza'
strings = [A,B,C]



def mkdict():
    """ This function is creating a dictionary of letters and their frequency."""
    final = {}
    for string in strings:
        for letter in string:
            if letter in final:
                final[letter] += 1
            else:
                final[letter] = 1
    return final


# Finding the largest number
def findlarg():
    """ This function is iterating through the final dictionary and finding the largers value."""
    final = mkdict()
    common_num = final.itervalues().next()
    for let in final:
        if final[let]>common_num:
            common_num = final[let]
            return common_num


# Prints the largest value(s)
for let in mkdict().iteritems():
    if let[1] == findlarg():
        print let




