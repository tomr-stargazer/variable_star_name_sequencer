""" 
Tests for variable_name_sequence_function.py 

should run with py.test 

"""

from ..variable_name_sequence_function import variable_name_sequencer, _second_letter_sequence_value

assert variable_name_sequencer("R CrA") == 1
assert variable_name_sequencer("S Ori") == 2
assert variable_name_sequencer("RR Lyr") == 10
# assert variable_name_sequencer("QZ And") == 334

assert _second_letter_sequence_value('R', 'R') == 1
assert _second_letter_sequence_value('R', 'S') == 2
assert _second_letter_sequence_value('S', 'S') == 1
