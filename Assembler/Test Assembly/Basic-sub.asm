# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# NOTE: This assumes that your instruction memory starts at address 0!
#
# results: The value 2 should be in register 1

addi $1 $0 1
addi $2 $0 2
sub $3 $1 $2