'''For a list of words, print out each word on a separate line, but in all uppercase'''
words = list(['python' , 'is', 'awesome'])

for word in words:
    print(word.upper())

####################################################

'''Turn that into a function, print_upper_words'''

def print_upper_words(words):
    '''this function prints words in uppercase letters'''

    words = list(['python' , 'is', 'awesome'])

    for word in words:
        print(word.upper())

##################################################

'''Change that function so that it only prints words that start with the letter ‘e’'''
def starts_with(words):
    '''this function will only print words that start with the letter 'e' (either upper or lowercase)'''
    words = ['explore', 'Excellent', 'moon']

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

####################################################

'''Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.'''

def print_upper_words2(words, starts_with):
    '''this funtion uppercased words that starts with the letters passed in'''

    words = ["hello", "hey", "goodbye", "yo", "yes"]

    for word in words:
        for letters in starts_with:
            if word.startswith(letters):
                print(word.upper())
                break

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"],
                   starts_with={"h", "y"})



