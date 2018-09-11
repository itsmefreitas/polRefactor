from utils import *
from algebra import *
from io import *

def main():

    showMenu()
    option = input(">>> ")

    while True:
        if option == 1:
            clear()
            pol_string = raw_input("Polynomial to simplify: ")
            print ""
            pol = parser(pol_string)
            pol = sorted(pol, key=lambda x: (x[1], -x[2]))
            pol = simplipy(pol)
            showPol(pol)
            print ""

            a = ""

            option = cont(a)

        elif option == 2:
            clear()
            n = input("How many polynomials do you wish to add? ")
            pols = [None] * n
            pol_string = ""
            print ""
            if n > 1:
                for i in range(0,n):
                    if i == 0:
                        pol_string = raw_input("Polynomial #"+str((i+1))+": ")
                    else:
                        pol_string += " + "
                        pol_string += raw_input("Polynomial #"+str((i+1))+": ")

                pol = parser(pol_string)
                pol = sorted(pol, key=lambda x: (x[1], -x[2]))
                pol = simplipy(pol)
                showPol(pol)
                print ""
            else:
                print "You must add more than one polynomial"

            a = ""

            option = cont(a)

        elif option == 3 or option == 4:
            clear()
            if option == 3:
                pol_string = raw_input("Polynomial to derivate: ")
            elif option == 4:
                pol_string = raw_input("Polynomial to integrate: ")

            print ""
            pol = parser(pol_string)
            pol = sorted(pol, key=lambda x: (x[1], -x[2]))
            pol = simplipy(pol)

            varlist = getVars(pol)

            for v in varlist:
                if option == 3:
                    print("*** Derivative for " + v + " ***")
                    showPol(derivative(pol, v))
                elif option == 4:
                    print("*** Integral for " + v + " ***")
                    showPol(integral(pol, v))

            print ""

            a = ""

            option = cont(a)

        elif option == 5:
            clear()
            print "*** Goodbye! ***"
            quit()


main()