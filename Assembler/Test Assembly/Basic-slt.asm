# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# results: 
#	$3 = 1
#	$4 = 0
#	$5 = 0

addi $1 $0 -1
addi $2 $0 6
slt  $3 $1 $2
slt  $4 $1 $1
slt  $5 $2 $1
