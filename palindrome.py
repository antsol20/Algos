def firstNonRepeatingCharacter(string):
    for idx, char in enumerate(string):
        if not isDuplicated(char, string):
            return idx

    return -1


def isDuplicated(char, string):
    counter = 0
    for letter in string:
        if letter == char:
            counter += 1

    if counter > 1:
        return True
    else:
        return False


string = 'abcdcaf'
print(firstNonRepeatingCharacter(string))