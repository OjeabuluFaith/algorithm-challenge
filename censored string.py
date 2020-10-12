def uncensor(string, vowels):
    new_ = ""
    counter = 0
    for i in range(len(string)):
        if string[i] == "*":
            new_ += vowels[counter]
            counter += 1
        else:
            new_ += string[i]
    return new_



# a shorter way
def uncensor(txt, vowels):
    	txt = txt.replace('*', '{}')
	return txt.format(*vowels)