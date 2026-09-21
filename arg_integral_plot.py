import argparse
import numpy as np
import matplotlib.pyplot as plt
def main():
    parser = argparse.ArgumentParser(description = 'Using the Trapezioid and Simpson methods, integrates the function e^(-t^2) from a specified lower to upper bound and number of steps.')
    func = lambda t: np.exp(-t**2)
    parser.add_argument('--a',type=int,help='lower bound of integral')
    parser.add_argument('--b',type=int,help='upper bound of integral')
    parser.add_argument('--n',type=int,help='number of slices')
    parser.add_argument("--homework", help="sets lower bound to 0, upper to 3, steps to 20 and plots both integrals as a function of the upper bound from 0-3 in steps of .1")
    args = parser.parse_args()
    def python_trapezoid(f, a, b, n):
        delta = (b - a) / n
        integral_sum = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            integral_sum += f(a + i * delta)
            
        return (integral_sum) * delta
    def python_simpson(f, a, b, n):
        delta = (b - a) / n
        integral_sum = (f(a) + f(b))
        for i in range(1, int(n/2)):
            integral_sum += 4*(f(a + ((2*i-1) * delta)))
        for i in range(1, int(n/2)-1):
            integral_sum += 2*(f(a + ((2*i * delta))))
            
        return (integral_sum) * (delta/3)

    if args.homework:
        a = 0
        b = 3
        n = 20
        print("The trapezoid method gives a value of " + ' ' + f'{python_trapezoid(func, a, b, n):.4f}' + ' ' "and the Simpson method gives a value of " + ' ' + f'{python_simpson(func,a,b,n):.4f}')


        trap_array = []
        for k in np.linspace(0,3,31):
            trap_array.append(python_trapezoid(func,0,k,20))
        simp_array = []
        for k in np.linspace(0,3,31):
            simp_array.append(python_simpson(func,0,k,20))
        plt.scatter(np.linspace(0,3,31),np.array(trap_array),c='blue',label='Trapezoid Integral')
        plt.plot(np.linspace(0,3,31),np.array(simp_array),c='r',label='Simpson Integral')
        plt.xlabel("Upper Bound (Lower Bound = 0)")
        plt.ylabel("Integral of e^(-t^2)")
        plt.title("Integral of e^(-t^2) as a function of upper bound")
        plt.legend()
        plt.xlim(-.5,4)
        plt.ylim(-.25,1.5)
        plt.show()

    if args.homework is None:
        #parser.add_argument('a',type=int,help='lower bound of integral')
        #parser.add_argument('b',type=int,help='upper bound of integral')
        #parser.add_argument('n',type=int,help='number of slices')
        #args = parser.parse_args()
        if [args.a,args.b,args.n] == [None,None,None]:
            raise ValueError("Please add lower bound (--a), upper bound (--b), and number of slices (--n).")
        a = args.a
        b = args.b
        n = args.n
        #args.a = 0
        #args.b = 1
        #args.c = 0

        print("The trapezoid method gives a value of " + ' ' + str(python_trapezoid(func, a, b, n)) + ' ' "and the Simpson method gives a value of " + ' ' + str(python_simpson(func,a,b,n)))
if __name__ == "__main__":
    main()


