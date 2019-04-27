# NYT spelling bee puzzle solver
# made by taargle with love
# and annyoance
with open("words.txt") as word_file:
    actual_words = set(word.strip().lower() for word in word_file)
    # takes the word document and turns it into a set to use

validLetters = set()


def cheating_time(wordset, letterset, centerLetter):
    shit = set()
    output = set()
    for word in wordset:
        tempset = set(word)
        if tempset - letterset == set() and len(word) >= 5:
            shit.add(word)
            # makes sure word can be made and is 5+ letters long
    for thing in shit:
        tempset2 = set(thing)
        if centerLetter in tempset2:
            output.add(thing)
            # makes sure the center letter is in there too
    finalWordBarf = ', '.join(output)
    # final word barf is exactly what it says
    print("Finished! Words found: ", finalWordBarf)


print("Welcome to the NYT Spelling Bee Solver, fellow cheater.")
print("What letters 'ya got? (lowercase please)")

LCEN = input("Center Letter: ")
validLetters.add(LCEN)
validLetters.add(input("Letter One: "))
validLetters.add(input("Letter Two: "))
validLetters.add(input("Letter Three: "))
validLetters.add(input("Letter Four: "))
validLetters.add(input("Letter Five: "))
validLetters.add(input("Letter Six: "))
# asks for the letters and adds them to the set which we're about to use to run through the english language as of 2004

print("Your set of letters is: ", validLetters)
print("Now solving... (this might take an entire hour!)")

cheating_time(actual_words, validLetters, LCEN)