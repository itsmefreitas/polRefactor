def simplipy(p):
    symPol = []
    used = []
    """For every tuple in the list of tuples (polynomial), do..."""
    for t in range(0,len(p)):
        tup1 = (p[t][1], p[t][2])

        flag = 0
        res = p[t][0]
        for t2 in range(t+1, len(p)):

            tup2 = (p[t2][1], p[t2][2])

            """If the exponent and the letter is equal in both tuples, then we can perform a sum/subtraction in order to simplpy"""
            if tup1 == tup2:
                res = res + int(p[t2][0])
                flag = 1
                used.append(t2)
        if t not in used and res != 0:
            if flag==1: symPol.append((res,p[t][1],p[t][2]))
            elif flag == 0: symPol.append((res,p[t][1],p[t][2]))
    return symPol

"""In order to add two user-input polynomials, we parse the respective strings, then simplify the resulting list of tuples, deriving from that."""
def addPol(p1, p2):
    pcomp_string = p1 + ' + ' + p2
    p3 = parser(pcomp_string)
    return simplipy(p3)

"""To calculate the derivative of a polynomial, we get it's tuples, then the variable for which we are derivating."""
def derivative(p, ord):
    p_dOrd = []
    for t in range (0,len(p)):
        intt = p[t][0]
        vart = p[t][1]
        expt = p[t][2]
        if vart == ord:
            if expt == 1:
                p_dOrd.append((intt,'|',1))
            elif expt > 1:
                p_dOrd.append((intt*expt,vart,expt-1))

    p_dOrd = sorted(p_dOrd,key=lambda x: (x[1],-x[2]))
    return simplipy(p_dOrd)

def integral(p, ord):
    p_iOrd = []
    for t in range (0,len(p)):
        intt = p[t][0]
        vart = p[t][1]
        expt = p[t][2]

        if vart == "|":
            p_iOrd.append((intt,ord,expt))

        elif vart == ord:
            n_part = float(intt) / float((expt + 1))
            n_part = '%.2f' % n_part
            p_iOrd.append((float(n_part),vart,expt+1))

        elif vart != ord:
            n_part = float(intt)
            n_part = '%.2f' % n_part
            p_iOrd.append((float(n_part),ord+vart,expt))

    p_iOrd = sorted(p_iOrd,key=lambda x: (x[1],-x[2]))
    return simplipy(p_iOrd)

def getVars(p):
    vars=[]

    for t in range(0,len(p)):
        vart = p[t][1]
        if vart not in vars and vart != '|':
            vars.append(vart)

    return vars