import sys
import random


def get_attr(filename):

    clauses = []
    for line in open(filename):

        if line[0] == 'c':
            continue
        if line[0] == 'p':
            nuber_symbols = int(line.split()[2])
            number_clauses =int(line.split()[3])
            continue

        clause = []
        for literal in line.split()[:-1]:
            literal = int(literal)
            clause.append(literal)

        clauses.append(clause)

    return clauses, nuber_symbols,number_clauses

def initialize_symbols(number_symbols):
    symbols = [i if random.random()<0.5 else -i for i in range(number_symbols+1)]
    return symbols

def get_clauses_value(clauses,symbols):
    #Intialize all clauses to false
    truth_val_clauses = [0 for i in range(len(clauses))]
    for index,clause in enumerate(clauses):
        for literal in clause:
            if symbols[abs(literal)] == literal:
                #EVEN IF ONE LITERAL IN A CLAUSE IS TRUE THAT CLAUSE IS TRUE
                truth_val_clauses[index] = 1
                break

    return truth_val_clauses

def check_model(val_clauses):
    if sum(val_clauses) == len(val_clauses):
        return True
    else:
        return False

def choose_best_symbol(clauses,symbols):
    max = -1
    max_benefit_symbol = []
    temp_symbols = symbols

    for i in range(1,len(symbols)):
        temp_symbols[i] *= -1
        truth_val_clauses = get_clauses_value(clauses,temp_symbols)
        if sum(truth_val_clauses) > max:
            max = sum(truth_val_clauses)
            max_benefit_symbol = []
            max_benefit_symbol.append(i)

        elif sum(truth_val_clauses) == max:
            max_benefit_symbol.append(i)
        temp_symbols[i] *= -1
    return random.choice(max_benefit_symbol)

def walkSAT(clauses , number_symbols , number_clauses , probability = 0.5 , max_flips =1000):
    '''
    This return the symbols that will satify the given CNF
    '''
    symbols = initialize_symbols(number_symbols)
    print(symbols)
    val_clauses = get_clauses_value(clauses,symbols)
    print(val_clauses)
    solved = False
    for i in range(max_flips):
        # if solved is True then the problem is satisfiable
        solved = check_model(val_clauses)
        print(solved)

        if solved:
            return True,symbols,i

        false_clauses_index = []
        for index,val in enumerate(val_clauses):
            if val ==0:
                false_clauses_index.append(index)
        print("false clause index:",false_clauses_index)
        # Choose a random clause from false_clauses and then flip random symbol
        random_false_clause_index = random.choice(false_clauses_index)
        random_false_clause = clauses[random_false_clause_index]
        print("random false clause",random_false_clause)
        if (random.random() < probability):
            random_symbol = abs(random.choice(random_false_clause))
            symbols[random_symbol] *= -1
        else:
            best_symbol = choose_best_symbol(clauses,symbols)
            print(best_symbol)
            symbols[best_symbol] *= -1
        print(clauses)
        print("symbols",symbols)
    return False,symbols,max_flips




if __name__ == "__main__":

    filename = sys.argv[1]

    clauses , n , m = get_attr(filename)
    print(n," ",m," ",clauses)
    prob = 0.5
    max_flips = 1000

    satifiable,model,num_iter = walkSAT(clauses,n,m,prob,max_flips)

    if satifiable:
        print(model[1:])
    else:
        print("Increase MAX")
