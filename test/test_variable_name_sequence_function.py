""" 
Tests for variable_name_sequence_function.py 

should run with py.test 

"""

from numpy.testing import assert_raises

from ..variable_name_sequence_function import (
    variable_name_sequencer,
    _second_letter_sequence_value,
    _first_letter_sequence_value)

assert variable_name_sequencer("R CrA") == 1
assert variable_name_sequencer("S Ori") == 2
assert variable_name_sequencer("RR Lyr") == 10
assert variable_name_sequencer("AA Tau") == 55
# assert variable_name_sequencer("QZ And") == 334
assert_raises(ValueError, variable_name_sequencer, 'A Tau')
assert_raises(ValueError, variable_name_sequencer, 'AJ And')
assert_raises(ValueError, variable_name_sequencer, 'JT And')
assert_raises(ValueError, variable_name_sequencer, 'CA Dra')

assert _second_letter_sequence_value('R', 'R') == 1
assert _second_letter_sequence_value('R', 'S') == 2
assert _second_letter_sequence_value('S', 'S') == 1
assert _second_letter_sequence_value('A', 'A') == 1
assert _second_letter_sequence_value('A', 'I') == 9
assert _second_letter_sequence_value('A', 'K') == 10


assert _first_letter_sequence_value("R") == 9
assert _first_letter_sequence_value("S") == 18
assert _first_letter_sequence_value("T") == 26

assert _first_letter_sequence_value("A") == 54
# assert _first_letter_sequence_value("B") == 79
