#!/usr/bin/env python

def objective_function(v):
    return sum(map(lambda x : x**2, v))

def random_vector(minmax):
    import random
    return map(lambda x : x[0] + (x[1]-x[0]) * random.random(), minmax)

def de_rand_1_bin(p0, p1, p2, p3, f, cr, search_space):
	pass

def select_parents(pop, current):
	pass

def create_children(pop, minmax, f, cr):
	pass

def select_population(parents, children):
	pass

def search(max_gens, search_space, pop_size, f, cr):
	return { 'cost' : 0, 'vector' : [] }

def main():
    # problem configuration
    problem_size = 3
    search_space = [[-5, +5]] * problem_size
    # algorithm configuration
    max_gens = 200
    pop_size = 10*problem_size
    weightf = 0.8
    crossf = 0.9
    # execute the algorithm
    best = search(max_gens, search_space, pop_size, weightf, crossf)
    print "done! Solution: f=%f, s=%s"% (best['cost'], str(best['vector']))

if __name__ == "__main__":
    main()

