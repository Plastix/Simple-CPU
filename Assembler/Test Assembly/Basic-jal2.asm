# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# NOTE: This assumes that your instruction memory starts at address 0!
#
# results:
#	$ra ($15) = 5
#	$1 = 4

addi $1 $0 5
jal 4
addi $1 $0 4
addi $1 $0 6
jal 6
addi $1 $0 2
subi $1 $1 1