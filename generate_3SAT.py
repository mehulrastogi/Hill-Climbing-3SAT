import sys
import random

class Clause(object):
    """A Boolean clause randomly generated"""

    def __init__(self, num_vars, clause_length):
        """
		Initialization
		length: Clause length
		lits: List of literals
		"""
        self.length = clause_length
        self.lits = None
        self.gen_random_clause(num_vars)

    def gen_random_clause(self, num_vars):
        self.lits = []
        while len(self.lits) < self.length:  # Set the variables of the clause
            new_lit = random.randint(1, num_vars)  # New random variable
            if new_lit not in self.lits:  # If the variable is not already in the clause
                self.lits.append(new_lit)  # Add it to the clause
        for i in range(len(self.lits)):  # Sets a negative sense with a 50% probability
            if random.random() < 0.5:
                self.lits[i] *= -1  # Change the sense of the literal

    def show(self):
        """Prints a clause to the stdout"""

        sys.stdout.write("%s 0\n" % " ".join(map(str, self.lits)))
    def write(self,file):
        file.write("%s 0\n" % " ".join(map(str, self.lits)))


class CNF(object):
    """A CNF formula randomly generated"""

    def __init__(self, num_vars, num_clauses, clause_length):
        """
		Initialization
		num_vars: Number of variables
		num_clauses: Number of clauses
		clause_length: Length of the clauses
		clauses: List of clauses
		"""
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        self.clause_length = clause_length
        self.clauses = None
        self.gen_random_clauses()

    def gen_random_clauses(self):
        self.clauses = []
        for _ in range(self.num_clauses):
            clause = Clause(self.num_vars, self.clause_length)
            self.clauses.append(clause)

    def show(self):
        """Prints the formula to the stdout"""

        sys.stdout.write("c Random CNF formula\n")
        sys.stdout.write("p cnf %d %d\n" % (self.num_vars, self.num_clauses))
        for clause in self.clauses:
            clause.show()

    def write(self,filename):
        import sys
        file = open(filename, 'w')
        file.write("c Random CNF formula\n")
        file.write("p cnf %d %d\n" % (self.num_vars, self.num_clauses))
        for clause in self.clauses:
            clause.write(file)
        file.close()



if __name__ == "__main__":

    no_symbols = int(sys.argv[1])
    no_clauses = int(sys.argv[2])
    clause_length = int(sys.argv[3])

    # Create a solver instance with the problem to solve
    cnf_formula = CNF(no_symbols, no_clauses, clause_length)
    # Show formula
    cnf_formula.show()
