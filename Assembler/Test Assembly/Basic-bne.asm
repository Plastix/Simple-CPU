# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# results: 
#	$1 = 2
#	$2 = 6
#	$3 = 4

addi $1 $0 2
addi $2 $0 6
bne  $1 $1 0
bne  $1 $2 1
add  $2 $1 $2
addi $3 $0 4 

