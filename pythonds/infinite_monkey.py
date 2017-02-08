# https://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
#  Self Check
# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
#
# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.
#
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.
#
# Self Check Challenge
# See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.

import string
import random

chars = list(string.ascii_lowercase)
chars.append(' ')

def generate_sentence(n, matchedChars, bestMatch):
    for i in range(n):
        if matchedChars[i] == 0:
            bestMatch[i] = random.choice(chars)
            break
    sentence = ''.join(bestMatch)
    print(sentence)
    return sentence


def calculate_score(originalSentence, matchedChars, bestMatch):
    generatedSentence = generate_sentence(len(originalSentence), matchedChars, bestMatch)
    score = 0

    for i in range(len(originalSentence)):
        if generatedSentence[i] == originalSentence[i]:
            score += 1
            matchedChars[i] = 1

    score = score / len(originalSentence)
    results = {'score': score, 'generatedSentence': generatedSentence}
    return results

def get_match(originalSentence):
    print("Original Sentence: "+originalSentence)
    score = 0.0
    bestScore = 0.0
    i = 1
    bestMatch = [random.choice(chars)] * len(originalSentence)
    matchedChars = [0] * len(originalSentence)
    while score < 1:
        results = calculate_score(originalSentence, matchedChars, bestMatch)
        score = results['score']
        if score > bestScore:
            bestScore = score
            bestMatch = list(results['generatedSentence'])
        if (i % 1000) == 0:
            print(str(i)+". try, best string so far: "+str(bestMatch)+", match score: "+str(bestScore))
        i += 1

    print("Match found in "+str(i)+". try")
    # Match found in 34. try

originalSentence = "test"
get_match(originalSentence)