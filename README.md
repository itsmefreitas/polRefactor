# polRefactor
This calculator is capable of parsing polynomials from input, dealing with:
  - Integer coefficients and powers in polynomials;
  - Sum and subtraction arithmetic operations;
  - Multivariable expressions;
  - Standalone integer values;
  
Operations performed by polRefactor are:
  - Simplification/factorization of polynomials;
  - Calculation of integrals and derivatives with respect to every variable;
  - Addition of an arbitrary number of polynomials to an expression;
  
The parser contained in polRefactor is handwritten and currently supports inputs of in the language defined as:

S -> '+' | '-'

N -> [0-9]

V -> [a-z]

T -> S? T | N+ | N* V+ N*

E -> T | T S E

so an example of correct input would be: "2x3 - 4z + 3xy + 5 + x3 - 2" that polRefactor would process.
