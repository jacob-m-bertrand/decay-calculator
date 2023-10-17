# Decay Calculator

A simple calculator script which simulates isotope decays, and gives details on the decay, its byproducts, and the energy released.

# Usage

This script was intended to be used from the command line like so:

atomic.py [decay type] [nucleon count] [proton count] {--m1} {--m2} {--mhe} {--me} {--u} {--p}

--m1: sets the mass of the initial element
--m2: sets the mass of the resulting element
--mhe: sets the mass of He-4 (which forms the baseline of the calculations)
--me: sets the mass of an electron
--u: sets the u to MeV/c^2 conversion
--p: sets the precision of the calculations

The above flags are intended to be used in university settings where custom approximations are used. Standard values are given by default.
