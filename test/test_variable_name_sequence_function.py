""" 
Tests for variable_name_sequence_function.py 

should run with py.test 

"""

from ..variable_name_sequence_function import variable_name_sequencer

assert variable_name_sequencer("R CrA") == 1
assert variable_name_sequencer("S Ori") == 2
assert variable_name_sequencer("RR Lyr") == 10
# assert variable_name_sequencer("QZ And") == 334