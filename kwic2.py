#!/usr/bin/env python3

import sys
import fileinput
import string


def main():
	keys = list()
	phrases = list()
	capitals = list()
	buildLists(keys, phrases, capitals)
	finalList = list()
	caps = {}
	refineLists(keys, capitals, caps)
	print(caps.items())
	print()
	sortDict(caps, finalList)
	finalFormat(caps, finalList)

	
def buildLists(keys, phrases, capitals):
	allFile = list()
	for line in fileinput.input():
		allFile.append(line.strip())
	phraseStart=allFile[2:].index("::")+2
	for x in allFile[2:phraseStart]:
		keys.append(x)
	for x in allFile[phraseStart+1:]:
		phrases.append(x)
	for x in phrases:
		capitals.append(x.split())


def refineLists(keys, capitals, caps):
	listIt = list()
	finalPhrase = ''
	for phraseLine in capitals:
		for phraseWord in phraseLine:
			if(checks(phraseWord.lower(), keys)):
				temp2 = phraseWord
				temp = phraseWord.upper()
				phraseLine[:] = [temp if m==phraseWord else m for m in phraseLine]
				finalPhrase = " ".join(phraseWord for phraseWord in phraseLine)
				listIt.append(finalPhrase)
				if temp in caps:
					caps[temp].extend(listIt)
				else:
					caps[temp] = listIt
				phraseLine[:] = [temp2 if m==temp else m for m in phraseLine]
				listIt = []
			#print(caps.get(phraseWord.upper()))
				
def checks(y, keys):
	for z in keys:
		if(y == z):
			return False
	return True

	
def sortDict(caps, finalList):
	keylist = list()
	for x in caps:
		keylist.append(x)
	keylist.sort()
	for key in keylist:
		finalList.append(caps[key])
	
	
def finalFormat(caps, finalList):
	count = 0
	numDone = list()
	cutList = list()
	for part in finalList:
		for sentance in part:
			for letter in sentance:
				#print("HI")
				#print(caps.get(letter))
				if(letter in numDone):
					continue
				else:
					#
					#
					#change to comprehension that checks the whole word? instead of just the characters?
					#
					#
					if(letter.isupper() or letter.isdigit()):
						if(sentance[sentance.index(letter)+1].isupper() or sentance[sentance.index(letter)].isdigit()):
							count = sentance.index(letter)
							if(letter.isdigit()):
								for i in sentance[count:]:
									numDone.extend(i)
									if(i == ' '):
										numDone.append("")
										break
							#print("count: "),
							#print(count)
							if(count>20):
								cutList.append(9*" "+sentance[count-20:count+31])
								
								start = sentance.find(" ", count-21)
								end = sentance.rfind(" ", 0, count+32)
								if len(sentance)-count > 31:
									print(" "*(29-count+start)+sentance[start:end])
								else:
									print(" "*(29-count+start)+sentance[start:])
							else:
								spaces = 29-count
								end = sentance.rfind(" ", 0, count+32)
								#print("spaces; "),
								#print(spaces)
								if len(sentance)-count > 31:
									print(spaces*" " + sentance[:end])
								else:
									print(spaces*" " + sentance[:])
							break
						count = count+1
	
def printTest(array):
	for x in array:
		print(x)

		
if __name__ == '__main__':
	main()