# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# NOTE: You need a working BEQ for this to work
#
# NOTE: This assumes that your instruction memory starts at address 0!
#
# results: The value 15 should be in register 3. This is the result of summing
# the numbers 1-5.

addi $1 $0 1
addi $2 $0 6
beq  $1 $2 3
add  $3 $3 $1
addi $1 $1 1
j 2