import re

bww = open("siege.bww", "r")
notes = bww.read()
notes = notes[notes.find('&'):] #removes preamble
notes = re.sub(r'(l|r)', '', notes).split()
#print(*notes, sep = '\n'+',')
#print(notes)

pitchMatrix = []
lengthMatrix = []

pitchDict = {'LG':0, 'LA':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'HG':7, 'HA':8}
lengthDict = {'32':.5, '16':1, '8':2, '4':4, '2':8, '1':16}

measure = []
part = []
tune = []

"""
for substr in notes:
	if substr[0].isupper() and 'I' not in substr:
		pitchMatrix.append(pitchDict[substr.split('_')[0]])
		lengthMatrix.append(lengthDict[substr.split('_')[1]])
	if substr[0] == '\'':
		lengthMatrix[-1]*=1.5
"""
for substr in notes:
	if substr[0].isupper() and 'I' not in substr:
		measure.append([pitchDict[substr.split('_')[0]], lengthDict[substr.split('_')[1]]])
	if substr[0] == '\'':
		measure[-1][1]*=1.5
	if substr[0] == '!':
		part.append(measure)
		measure = []
	if substr == '\'\'!I':
		tune.append(part)
		part = []
#tune[part][measure][note][pitch/duration]
print(tune[0][0])
print(tune[0][1])
print(tune[0])
#print(pitchMatrix)
#print(lengthMatrix)
