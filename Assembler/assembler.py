# CSC 270 Final Project
#
# Super Basic Assembler
# It ain't pretty but it works!
#
# Aidan Pieper
# 

import sys
from hf import *

RGSTR_LEN = 4
IMM_LEN = 8
J_IMM_LEN = 16
INSTR_LEN = 20

opcodeDict = {
		'add':  '0000',
		'and':  '0000',
		'or':   '0000',
		'sub':  '0000',
		'addi': '0001',
		'andi': '0010',
		'ori':  '0011',
		'subi': '0100',
		'lw':   '0101',
		'sw':   '0110',
		'beq':  '0111',
		'bne':  '1000',
		'j':    '1001',
		'slt':  '0000',
		'sgt':	'0000',
		'jal':  '1010',
		'jr':   '1011',
		}

funcDict = {
	'add': '$0',
	'and': '$1',
	'or':  '$2',
	'sub': '$3',
	'slt': '$4',
	'sgt': '$5',
}

llist = {
	'addi',
	'andi',
	'ori',
	'subi',
}

def ConvertAssemblyToMachineCode(inline):
	'''given a string corresponding to a line of assembly,
	convert it into a string of binary values'''

	outstring = ''
	words = inline.split() #assuming syntax words are separated by space, not comma
	operation = words[0]
	operands = words[1:]

	updateOperands(operation, operands)

	outstring += opcodeDict[operation]
	for oprand in operands:
		if oprand[0] == '$':
			outstring += int2bs(oprand[1:],RGSTR_LEN)
		else:
			outstring += int2bs(oprand, J_IMM_LEN if operation == 'j' or operation == 'jal' else IMM_LEN)
	return outstring	


def updateOperands(operation, operands):
	'''
	updates assembly operands to match the instruction word format
	'''

	# R-Type
	# Move rd operand to second to last spot
	# Add funct operand to end
	if operation in funcDict.keys():
		operands.append(operands.pop(0))
		operands.append(funcDict[operation])

	# I-Type
	# Move destination register to rt
	if operation in llist:
		operands.insert(1,operands.pop(0))

	# SW/LW
	# Set immediate offset to end
	# Move base register to rs
	# (destination register rt)
	if operation == 'lw' or operation == 'sw':
		w = operands[1]
		p = w.find('(')
		operands[1] = w[:p]
		operands.insert(0, w[p+1:p+3])

	# JR
	# JR only uses rs
	# Pad with $0 operands to fill instruction word
	if operation == 'jr':
		operands.append("$0")
		operands.append("$0")
		operands.append("$0")

def parsePseudoInstructions(lines):
	l = []
	for line in lines:
		words = line.split()
		operation = words[0]
		operands = words[1:]

		if(operation == 'bge'):
			l.append('slt $14 ' + operands[0] + " " + operands[1])
			l.append('beq $14 $0 ' + operands[2])
		else:
			l.append(line)
	return l

 		

def AssemblyToHex(infilename,outfilename):
	'''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
	then save that machinecode to an outputfile'''
	with open(infilename) as f:
		with open(outfilename,'w') as of:
			of.write("v2.0 raw\n")      # Header for Logism

			lines = [line.rstrip() for line in f.readlines()] # read assembly and strip whitespace
			lines = [line[:line.find('#')] if line.find('#') != -1 else line for line in lines ] # strip comments
			lines = [line for line in lines if line != '']
			lines = parsePseudoInstructions(lines)

			for outline in (bs2hex(l, INSTR_LEN) for l in 
									(ConvertAssemblyToMachineCode(curline) for curline in lines)):
				of.write(outline)
				of.write("\n")
		of.close()		
	f.close()
	
if __name__ == "__main__":
	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler
	#print 'Number of arguments:', len(sys.argv), 'arguments.'
	#print 'Argument List:', str(sys.argv)

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args	
	if (len(sys.argv) != 3):
		print('usage: python skeleton-assembler.py inputfile.asm outputfile.hex')
		exit(0)

	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	AssemblyToHex(inputfile,outputfile)
