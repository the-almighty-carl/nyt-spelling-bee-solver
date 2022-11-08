# main.py
# script for solving New York Times "spelling bee" puzzles
# made by elliott black (@demonpuncher on repl.it) ~2018

with open("words.txt") as word_file:
    actual_words = set(word.strip().lower() for word in word_file)
    # reads words.txt and makes a table out of it


# cheating_time - this actually does the solving
# inputs:
#   wordset - table, preferably of words
#   letterset - letters in outer ring of puzzle
#   centerLetter - exactly what it sounds like
def cheating_time(wordset, letterset, centerLetter):
    junk = set()  # temporary holding zone
    output = set()  # exactly what it sounds like
    for word in wordset:
        tempset = set(word)  # turn word into set
        if tempset - letterset == set() and len(word) >= 5:
            junk.add(word)
            # add to temporary set if letters and length are valid
    for thing in junk:
        tempset2 = set(thing)  # yep, we're doing this again
        if centerLetter in tempset2:
            output.add(thing)
            # add to output set if center letter is present
    finalWordDump = ', '.join(output)
    print("Finished! Words found: ", finalWordDump)
    # makes the set of output words pretty and prints it


# interface_handler - handles interaction with user
# inputs:
#   wordset - set made from words.txt
def interface_handler(wordset):
    letterSet = set()
    print("NYTSBPS Loaded. Ready to solve.")
    print("NYTSBPS Awaiting inputs...")  # flair for user
    centerLetter = input("Center Letter: ").lower()[0]
    otherLetters = input("Outer Letters: ").lower()
    i = 0  # controls below while loop
    while i < 6:
        for letter in otherLetters:
            if i >= 6:
                break  # exits if more than six letters are read
            elif letter != "," and letter != " ":
                letterSet.add(letter)  # does what it says
                i = i + 1
            print(i, " ", letter)
    print("Running NYTSBPS for letters: ", ", ".join(letterSet),
          "with center letter ", centerLetter)
    letterSet.add(centerLetter)
    print("Solving...")  # see last comment
    cheating_time(wordset, letterSet, centerLetter)
    print("\n\n")
    loopControl = input("Solve another? (y/n): ").lower()[0]
    if loopControl == "y":  # this controls whether or not
        print("Reloading NYTSBPS...")  # main runs this again
    elif loopControl == "n":
        print("Exiting NYTSBPS...")
    else:
        print("PEBKAC Error! Exiting NYTSBPS...")
        return "n"
    return loopControl


# main - exactly what it sounds like
#inputs:
# words - word list
def main(words):
    foo = "bar"  # controls main program loop
    print("Loading NYTSBPS...")
    while foo == "bar":
        controller = interface_handler(words)
        if controller == "n":
            foo = "spam and eggs"
    print("NYTSBPS exited. You may close this window.")


main(actual_words)
