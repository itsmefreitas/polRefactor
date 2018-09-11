import os
def clear():
    os.system('clear')

def showMenu():
    print ("*** Welcome to CAS ***")
    print ""
    print ("1) simplify polynomial;")
    print ("2) add polynomials;")
    print ("3) derivate;")
    print ("4) integrate;")
    print ("5) quit.")
    print ""

def cont(a):
    while (a != "N" or a != "n") or (a != "Y" or a != "y"):
        a = raw_input("*** Do you wish to continue [Y/N]? ")
        if a == "Y" or a == "y":
            clear()
            showMenu()
            option = input(">>> ")
            break
        elif a == "N" or a == "n":
            clear()
            quit()
    return option

def showPol(p):

    out_string = ""

    for t in range(0,len(p)):

        if t == 0:
            if p[t][1] == '|':
                if p[t][0] < 0:
                    out_string = "- "+str((p[t][0]*(-1)))
                else:
                    out_string = str(p[t][0])
            else:
                if p[t][0] < 0:
                    if abs(p[t][0]) != 1:
                        if p[t][2] != 1:
                            out_string = "- "+str((p[t][0]*(-1)))+p[t][1]+str(p[t][2])
                        else:
                            out_string = "- " + str((p[t][0]*(-1)))+p[t][1]
                    else:
                        if p[t][2] != 1:
                            out_string = "- "+p[t][1]+str(p[t][2])
                        else:
                            out_string = "- "+p[t][1]
                else:
                    if p[t][2] > 1:
                        if abs(p[t][0]) != 1:
                            out_string = str(p[t][0])+p[t][1]+str(p[t][2])
                        else:
                            out_string = p[t][1]+str(p[t][2])
                    else:
                        if abs(p[t][0]) != 1:
                            out_string = str(p[t][0])+p[t][1]
                        else:
                            out_string = p[t][1]

        else:
            if p[t][1] == '|':
                if p[t][0] < 0:
                    out_string += " - "+str((p[t][0]*(-1)))
                else:
                    out_string += " + "+str(p[t][0])
            else:
                if p[t][0] < 0:
                    if p[t][2] > 1:
                        if abs(p[t][0]) != 1:
                            out_string += " - "+str((p[t][0]*(-1)))+p[t][1]+str(p[t][2])
                        else:
                            out_string += " - "+p[t][1]+str(p[t][2])
                    else:
                        if abs(p[t][0]) != 1:
                            out_string += " - "+str((p[t][0]*(-1)))+p[t][1]
                        else:
                            out_string += " - "+p[t][1]
                else:
                    if p[t][2] > 1:
                        if abs(p[t][0]) != 1:
                            out_string += " + "+str(p[t][0])+p[t][1]+str(p[t][2])
                        else:
                            out_string += " + "+p[t][1]+str(p[t][2])
                    else:
                        if abs(p[t][0]) != 1:
                            out_string += " + "+str(p[t][0])+p[t][1]
                        else:
                            out_string += " + "+p[t][1]


    print("= "+out_string)