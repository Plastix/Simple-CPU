# Author: Aidan Pieper
#
# Tests whether writing to the zero register actually works
#
# Note: this assumes your processor can handle 3-bit signed immediates.  If it can’t, you’ll need to modify this code.
#
# results:
#	$0 = $0

addi $0 $0 10
addi $0 $0 15
