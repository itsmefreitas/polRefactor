def parser(s):
    x=s.split(' ')
    l=[]
    for i in range(0,len(x)):

        """The simplest of cases: we're now handling a entry in a list where we have a plain number."""
        if x[i].isdigit() and x[i] != '0':

            """If it's the first thing in our list, then we simply add a new tuple representing a positive integer..."""
            if i == 0:
                l.append((int(x[i]),'|',1))

            else:
                """...otherwise, we found it in the midst of other elements, and it can either be positive or negative."""
                if x[i-1] == "-":
                    l.append((int(x[i])*(-1),'|',1))
                else:
                    l.append((int(x[i]),'|',1))

        else:
            """Now we're dealing with an element containing variables."""
            temp = x[i]
            intPart = ""
            letter = ""
            exponent = ""

            """If it's the first in the list, then we have a positive term."""
            if i == 0 and (temp != "-" and temp != "+"):
                """The whole mechanics for this, involve populating the different parts of the term, so we can identify which part we're actually parsing."""
                for j in range (0,len(x[i])):
                    if temp[j].isdigit() and letter == "":
                        """Iff no letter is assigned, then we're still looking at the integer part of the term, before the variable."""
                        intPart += temp[j]
                    elif temp[j].isdigit() and letter != "":
                        """Iff we already got a letter on our hands, then we've passed through the integer part too, then we're ready to interpret the exponent."""
                        exponent += temp[j]
                    else:
                        """If none of the above, then we found a letter for the variable."""
                        letter = temp[j]

                if intPart == "":
                    """If we didn't catch anything before the variable, then the term has a factor of 1*var."""
                    intPart = '1'
                if exponent == "":
                    """If no exponent was caught with the code above, then we know the term is of type: (int)*var^(1)."""
                    exponent = '1'
                if exponent != '0' and intPart != '0' and letter.isalpha():
                    """Iff both numeric parts of the term are nonzero integers, then all is well in the world."""
                    l.append((int(intPart),letter,int(exponent)))
                if exponent == '0' and intPart != '0':
                    """If we are in the presence of something like (int)*var^0, then we know it's equivalent to the tuple: ((int),1,1)."""
                    l.append((int(intPart),'|',1))

            elif i > 0 and i < len(x):
                """Much like in the if statement before, we're dealing with a composite term."""
                for j in range (0,len(x[i])):
                    """Upon parsing this term, cases are analogous to the ones where we have said composite term in the begginning of the list."""
                    if temp[j].isdigit() and letter == "":
                        intPart += temp[j]
                    elif temp[j].isdigit() and letter != "":
                        exponent += temp[j]
                    else:
                        letter = temp[j]

                """Again, checking for term completion..."""
                if intPart == "":
                    intPart = '1'
                if exponent == "":
                    exponent = '1'

                """Here we go again, looking at the operators behind us."""
                if x[i-1] == "+":
                    if exponent != '0' and intPart != '0' and letter.isalpha():
                        """Iff both numeric parts of the term are nonzero integers, then all is well in the world."""
                        l.append((int(intPart), letter, int(exponent)))
                    if exponent == '0' and intPart != '0':
                        """If we are in the presence of something like (int)*var^0, then we know it's equivalent to the tuple: ((int),'|',1)."""
                        l.append((int(intPart),'|',1))
                elif x[i-1] == "-":
                    if exponent != '0' and intPart != '0' and letter.isalpha():
                        """Iff both numeric parts of the term are nonzero integers, then all is well in the world."""
                        l.append((int(intPart)*(-1), letter, int(exponent)))
                    if exponent == '0' and intPart != '0':
                        """If we are in the presence of something like (int)*var^0, then we know it's equivalent to the tuple: ((int),1,1)."""
                        l.append((int(intPart)*(-1),'|',1))

    return l