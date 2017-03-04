# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# results: 
#	$1 = -1
#	$2 = -1
#	$3 = 3

addi $1 $0 2
addi $2 $0 -1
bge $1 $2 1
addi $3 $0 1
addi $3 $0 2
addi $1 $0 -1
bge $1 $2 1
addi $3 $0 5
addi $3 $3 1