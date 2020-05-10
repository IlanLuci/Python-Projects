"""
Name: MadLibs game

Purpose: Users choose words and the words are inserted into a story. 
Then the user sees the story.
"""

def getKeys(story):
    count = story.count("{")
    end = 0
    keys = []
    for x in range(count):
        start = story.find("{", end) + 1
        end = story.find("}", start)
        word = story[start:end]
        keys.append(word)
    return keys

def userInput(keysResult):
    words = dict()
    for x in keysResult:
        userResponse = input("Input a {} ".format(x))
        words[x] = userResponse
    return words

def main():
    story = """Little {name} fell off her {noun} while attempting to avoid
    a trail of ants {verb} the bike path. Once her tears had subsided
    and the cut on her knee ceased bleeding, she {adverb} got back on
    her bike. She then used the anthill as a bike ramp until the {secondNoun}
    collapsed; her revenge complete, she {secondVerb} home happily."""
    
    keysResult = getKeys(story)

    userResult = userInput(keysResult)

    finalstory = story.format(**userResult)

    print(finalstory)

main()