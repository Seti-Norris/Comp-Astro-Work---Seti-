import argparse
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as c
def main():
    parser = argparse.ArgumentParser(description = 'Using the Newton method, the distance from the center of the Earth to L1 (the Earth-moon lagrange point) is estimated in meters. Can also be displayed in miles for the imperially inclined.')
    parser.add_argument("--guess", type=float,default=3.5e8*u.m,help="A suitable starting value of r for the Newton's method calculation. Determined by the plot")
    parser.add_argument("--accuracy", type=float,default=1e-4,help="The accuracy limit for r before Newton's method stops. We want at least 4 significant figures here, so the default is 1e-4 meters. ")
    parser.add_argument("--show_plot", type=bool,default=False,help="If True, a plot will be displayed of the equation of motion as a function of r. Is False no plot is  displayed (Default).")
    parser.add_argument("--miles", type=bool,default=False,help="If True, answer will be displayed in miles instead of meters.")
    args = parser.parse_args()
    #defining the constants
    G = c.G
    m_Earth = c.M_earth
    m_Moon = 7.348e22*u.kg
    omega = 2.662e-6*u.s**-1
    R = 3.844e8*u.m
    
    func_lagrange1 = lambda r: ((G*m_Earth)/(r**2))-((G*(m_Moon))/(((R-r))**2))-(((omega)**2)*r)
    
    func_lagrange1_derivative =  lambda r: ((-2*G*m_Moon))/(((R-r)**3)) - ((2*(G*m_Earth))/(r**3)) - (omega**2)

    
    def newton_method(accuracy,guess):
        delta = 100 * u.kg # a mostly arbitrary value so the while loop can get started
        while np.abs(delta.value) > accuracy:
            delta = func_lagrange1(guess)/func_lagrange1_derivative(guess)
            guess = guess - delta
        if args.miles:
         print(f"The distance from the center of the Earth to the L1 Point is {guess.value/1609:.4e} miles.")

        else:
            print(f"The distance from the center of the Earth to the L1 Point is {guess:.4e}.")
    newton_method(args.accuracy,args.guess)
    newton_array = []
    for i in np.linspace(2e8,3.5e8,10000)*u.m:
        newton_array.append(func_lagrange1(i).value)
    
    if args.show_plot:
        plt.plot(np.linspace(2e8,3.5e8,10000),np.array(newton_array))
        plt.grid()
        plt.axhline(y=0, color="red", linestyle="--")
        plt.xlabel("Distance From Earth (meters)")
        plt.ylabel("d(r)")
        equation = (r'$d(r) = \frac{GM}{r^2} - \frac{Gm}{(R-r)^2} -\omega^2r$')
        plt.text(2.5e8,.008,equation, fontsize=16,c='red')
        plt.show()

 
if __name__ == "__main__":
    main()
