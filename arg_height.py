import argparse
import numpy as np
parser = argparse.ArgumentParser(description =  "Find the time in seconds, minutes and hours it takes for a ball dropped from rest to hit the ground. Ignoring air resistance.")
parser.add_argument('h',type=float,help='height of object above ground in meters')
parser.add_argument('g',type=float,help='acceleration due to gravity in meters per squared second')
args=parser.parse_args()
secs = (np.sqrt(2*args.h/args.g))
mins = secs/60
hrs = secs/3600

print("The ball will take" + " " + str(secs) + " "  "seconds to hit the ground." + " " + "That's" + " " + str(mins) + " " + "minutes." + " " + "Or" + " " + str(hrs) + " " + "hours.")
if args.g>10 or args.g<9.8:
    print("Looks like your not on Earth anymore.")
    if args.g>10:
        print("Maybe a gas giant like Jupiter?")
    else:
        print("Maybe a smaller planet like Mercury?")


