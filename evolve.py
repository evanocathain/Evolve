#!/usr/local/opt/python@3.9/bin/python3.9

## Import various important packages
#from sympy import *
import numpy as np
import scipy as sp
from scipy.stats import skew
#import matplotlib.pylab as plt
import argparse
import sys

## Parse command line arguments & set default values
parser = argparse.ArgumentParser()
parser.add_argument('-K', type=float, dest='K', help='Potential law scale factor, in units of 1.0e-28 (default: 1.0)', default=1.0)
parser.add_argument('-p0', type=float, dest='period', help='set the birth period in ms (default: 1.0)', default=1.0)
parser.add_argument('-pdot0', type=float, dest='pdot', help='set the birth period derivative in unites of 1.0-13 (default: 1.0)', default=1.0)
parser.add_argument('-tstep', type=float, dest='tstep_yrs', help='set the time step for the simulation in years (default: 10.0)', default=10.0)
parser.add_argument('-outf', dest='outf', help='set the output file name (default: outf)', default='outf')
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
args = parser.parse_args()
## Set some values
K=args.K*1.0e-28            # 
period = args.period*0.001  # in s
pdot   = args.pdot*1.0e-13  # in s/s
tstep_yrs = args.tstep_yrs  # in years

#K = 4.0e-29

def get_force(period):
    force = -K/(period**2)  # An inverse-square law type potential. Need the 1.0e-30 factor so that kinetic and potential energy bits are not of completely different order.
    return(force)

tstep = 86400.0*365*tstep_yrs    # in seconds
#period = 0.01             # in seconds, can be choosing a period from a distribution
#pdot   = 1.0e-13          # in s/s, can be choosing a period from a distribution
pddot = get_force(period)

freq   = 1.0/period
fdot   = -pdot/(period**2)

#pot    = potential(period)
#energy = 0.5*pdot**2 + potential(period)
#print(energy)
print(period, pdot)


# get initial value of Pddot
pddot = get_force(period) 

# evolve through P-Pdot space
for i in range(1,1000000):
    # Here, we will do a kick-drift-kick, 
    # i.e. a simplectic integration
    #
    # Kick
    pdot = pdot + 0.5*pddot*tstep
    # Drift
    period = period + pdot*tstep
    # Kick
    ppdot = get_force(period)
    pdot = pdot + 0.5*pddot*tstep
    print(period, pdot, pddot, i*tstep/86400.0/365)















