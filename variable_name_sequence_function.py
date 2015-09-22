"""
A simple function that converts a variable star name to a sequential number.

Variable star names are created per the following specification:
https://en.wikipedia.org/wiki/Variable_star_designation

"Variable stars are designated using a variation on the Bayer 
designation format of an identifying label (as described below) 
combined with the Latin genitive of the name of the constellation 
in which the star lies. 

The current naming system is:

* Stars with existing Greek letter Bayer designations are not 
  given new designations.
* Otherwise, start with the letter R and go through Z.
* Continue with RR...RZ, then use SS...SZ, TT...TZ and so on 
  until ZZ.
* Use AA...AZ, BB...BZ, CC...CZ and so on until reaching QZ, 
  omitting J in both the first and second positions.
* Abandon the Latin script after 334 combinations of letters and 
  start naming stars with V335, V336, and so on.

The second letter is never nearer the beginning of the alphabet than the first, e.g., no star can be BA, CA, CB, DA and so on.

Examples are R Coronae Borealis, YZ Ceti, V603 Aquilae.

"""

from __future__ import division


def variable_name_sequencer(name):
    """ Sequence number for a given variable designation. """

    try:
        sequence_name, constellation_name = name.split(' ')
    except:
        raise ValueError("Couldn't parse name")

    # these are the stars R thru Z; relatively simple
    if len(sequence_name) == 1:
        return ord(sequence_name.upper()) - ord('Q')

    elif len(sequence_name) == 2:
        initial_R = 9 # temporary hack! we'll have to figure out a better way for this to work...
        return ord(sequence_name[1]) - ord('Q') + initial_R
    else:
        raise ValueError("Couldn't parse name")


def _first_letter_sequence_value(letter):
    """ Determines the sequence value of the first letter. """

    # R= 9 - it's the number of letters between R and Z, inclusive aka (Q, Z]

def _second_letter_sequence_value(first_letter, second_letter):

    # generally, just the distance between the first & second letter plus one

    return 1 + ord(second_letter.upper()) - ord(first_letter.upper())

