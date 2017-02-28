# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# NOTE: This assumes that your return address register is $15!!!
#
# results: 
#	$1 = 4
# 	$2 = 4
#	$3 = 9

addi $1 $0 4
addi $2 $0 4
jal 5
addi $3 $3 1
j 7
add $3 $1 $2
jr $15