# Maciej Kuśnierz
# Julian Kwiatkowski
from numpy import linspace, polyval, polyfit, sqrt, random
from scipy import stats
from pylab import plot, title, show, legend
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Linear regression example with noise and statistics.')

    # defining how to add arguments
    # printf("Nazwy argumentow (wartosc bazowa): --xmin(-5), --xmax(5), --npoints(100), --a(0.8), --b(-4), --c(3)")
    parser.add_argument('--xmin', type=float, default=-5)
    parser.add_argument('--xmax', type=float, default=5)
    parser.add_argument('--npoints', type=int, default=100)
    parser.add_argument('--a', type=float, default=0.8)
    parser.add_argument('--b', type=float, default=-4)
    parser.add_argument('--c', type=float, default=3)

    # defining specific value of verbosity
    parser.add_argument('--verbosity', type=int, default=1, choices=[0, 1, 2])
    return parser.parse_args()

# CLI parametrization for:
# xmin, xmax, npoints, a, b, c;
# plus: verbosity/quiet level(so do not compute stats.linregress(t,xn))

def main():
    try:
        # Loading arguments
        args = parse_args()

        # Parameters
        xmin = args.xmin
        xmax = args.xmax
        npoints = args.npoints
        a = args.a
        b = args.b
        c = args.c
        verbosity = args.verbosity

        # Sample data creation
        # number of points
        n = 100
        t = linspace(-5, 5, n)  # xmin, xmax, npoints, a, b, c
        # parameters
        a = 0.8
        b = -4
        c = 3
        x = polyval([a, b, c], t)
        print(type(x))

        # Add some noise
        xn = x + random.randn(n)

        if verbosity == 2:
            print(f"Generated data (t): {t}")
            print(f"Original values (x): {x}")
            print(f"Noisy values (xn): {xn}")

        # Linear regression - polyfit (polyfit can be used with other order polynomials)
        (ar, br, cr) = polyfit(t, xn, 2)
        xr = polyval([ar, br, cr], t)

        # Compute the mean square error
        err = sqrt(sum((xr - xn) ** 2) / n)

        print('Linear regression using polyfit')
        print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a, b, ar, br, err))

        # Matplotlib plotting
        title('Linear Regression Example')
        plot(t, x, 'bx--')
        plot(t, xn, 'ko')
        plot(t, xr, 'r+')
        legend(['original', 'plus noise', 'regression'])
        show()

        # Linear regression using stats.linregress
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
        (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
        print('Linear regression using stats.linregress')
        print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a, b, a_s, b_s, stderr))

    except Exception as e:
        # If an error occurs
        print(f"Nieoczekiwany błąd: {e}")
    finally:
        print("Program zakończył działanie.")


if __name__ == "__main__":
    main()
