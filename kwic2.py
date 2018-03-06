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
	sortDict(caps, finalList)
	finalFormat(caps, finalList)
	#printTest(finalList)

	
def buildLists(keys, phrases, capitals):
	allFile = list()
	for line in fileinput.input():
		allFile.append(line.strip())
	phraseStart=allFile[2:].index("::")+2
	for x in allFile[2:phraseStart]:
		keys.append(x)
	#printTest(keys)
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
				temp = phraseWord.upper()
				phraseLine[:] = [temp if m==phraseWord else m for m in phraseLine]
				finalPhrase = " ".join(phraseWord for phraseWord in phraseLine)
				listIt.append(finalPhrase)
				if temp in caps:
					caps[temp].extend(listIt)
				else:
					caps[temp] = listIt
				temp2 = phraseWord.lower()
				phraseLine[:] = [temp2 if m==temp else m for m in phraseLine]
				listIt = []

				
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
			#print("sentance: " + sentance)
			for letter in sentance:
				#print("letter: " + letter)
				if(letter in numDone):
					continue
				else:
					if(letter.isupper() or letter.isdigit()):
						if(sentance[sentance.index(letter)+1].isupper() or sentance[sentance.index(letter)].isdigit()):
							count = sentance.index(letter)
							if(letter.isdigit()):
								for i in sentance[count:]:
									numDone.extend(i)
									if(i == ' '):
										numDone.append("")
										break
							if(count>20):
								cutList.append(9*" "+sentance[count-20:count+31])
								
								start = sentance.find(" ", count-21)
								end = sentance.rfind(" ", count+32)
								if len(sentance) > 31:
									print(" "*(29-count+start)+sentance[start:])
								else:
									print(" "*(29-count+start)+sentance[start:end])
							else:
								spaces = 29-count
								end = sentance[:count+32].rfind(" ")
								if len(sentance) > 31:
									print(spaces*" " + sentance[:end])
								else:
									print(spaces*" " + sentance[:])
							break
						count = count+1
	
	
	
	
	#printTest(cutList)
	print()
	#finalPrint(cutList)
	
	
def finalPrint(cutList):
#	for sentance in cutList:
#		if(sentance[0]!=' '):
#			start = sentance[:].find(" ")
#			sentance = ' '*(start)+sentance[start:]
#		else:
#			sentance = sentance[1:]
#		if(sentance[len(sentance)-1]!=' '):
#			end = sentance[:].rfind(" ")
#			sentance = sentance[:end]
#		else:
#			sentance = sentance[:len(sentance)-1]
#	printTest(cutList)


	pleaseWork = list()
	for sentance in cutList:
		if(sentance[0]!=' '):
			start = sentance[:].find(" ")
			pleaseWork.append(' '*(start)+sentance[start+1:])
		else:
			pleaseWork.append(sentance[1:])
	pleaseWork2 = list()
	for sentance in pleaseWork:
		if(sentance[len(sentance)-1]!=' '):
			end = sentance[:].rfind(" ")
			pleaseWork2.append(sentance[:end])
		else:
			pleaseWork2.append(sentance[:len(sentance)-2])
	printTest(pleaseWork2)		
	
	
def printTest(array):
	for x in array:
		print(x)

		
if __name__ == '__main__':
	main()