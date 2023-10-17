from mendeleev import element
from getIsotope import getIsotope
import sys
import argparse

parser = argparse.ArgumentParser(description='finds the results and energy of specified decay')
parser.add_argument('decay', help="decay type")
parser.add_argument('nucleons', help="number of nucleons")
parser.add_argument('protons', help="number of protons")
parser.add_argument('--m1', help="Mass of initial element")
parser.add_argument('--m2', help="Mass of resultant element")
parser.add_argument('--mhe', help="Mass of He-4")
parser.add_argument('--me', help="Mass of electron")
parser.add_argument('--u', help="u to MeV/c^2 conversion")
parser.add_argument('--p', help="Precision")
args = parser.parse_args()

nuc = int(args.nucleons)
protons = int(args.protons)
decay = args.decay

el = element(protons)

if args.m1:
    m1 = float(args.m1)
else:
    iso = getIsotope(el, nuc)
    if iso == None:
        print("Unstable initial isotope! Please provide isotope masses!")
    m1 = iso.mass

if args.me:
    me = float(args.me)
else:
    me = .0005486

if args.u:
    u = float(args.u)
else:
    u = 931.494

if decay == "alpha":
    rNuc = nuc - 4
    rProtons = protons - 2
    rEl = element(rProtons)
    initMass = m1
    results = str(rNuc) + " " + str(rProtons) + " " + rEl.symbol + " + 4 2 He"

elif decay == "beta-":
    rNuc = nuc
    rProtons = protons + 1
    rEl = element(rProtons)
    initMass = m1
    results = str(rNuc) + " " + str(rProtons) + " " + rEl.symbol + " + anti electron neutrino + electron" 

elif decay == "beta+":
    rNuc = nuc
    rProtons = protons - 1
    rEl = element(rProtons)
    initMass = (m1 - (protons * me))
    results = str(rNuc) + " " + str(rProtons) + " " + rEl.symbol + " + electron neutrino + positron" 

elif decay == "ec":
    rNuc = nuc
    rProtons = protons - 1
    rEl = element(rProtons)
    initMass = m1
    results = str(rNuc) + " " + str(rProtons) + " " + rEl.symbol + " + electron neutrino" 


if args.m2:
    m2 = float(args.m2)
else:
    rIso = getIsotope(rEl, nuc)
    if rIso == None:
        print("Unstable result isotope! Please provide isotope masses!")
    m2 = rIso.mass


if decay == "alpha":
    if args.mhe:
        fMass = float(args.mhe) + m2
    else:
        fMass = element(2).mass + m2

elif decay == "beta-" or decay == "ec":
    fMass = m2

elif decay == "beta+":
    fMass = ((m2 - (rProtons*me)) + me)


deltaM = initMass - fMass 

if args.p:
    p = int(args.p)
else:
    p = 5

energy = round((initMass-fMass)* u, p)


print("The", decay, "decay resulted in", results, "releasing", energy, "MeV of energy")

