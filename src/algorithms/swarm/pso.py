#!/usr/bin/env python

"""
Particle Swarm Optimization (PSO)
"""


def objective_function(v):
    return sum(map(lambda x: x**2, v))


def random_vector(min_max):
    from random import random
    #print min_max
    return map(lambda x: x[0] + (x[1]-x[0]) * random(), min_max)


def create_particle(search_space, vel_space):
    particle = {'position': random_vector(search_space)}
    particle['cost'] = objective_function(particle['position'])
    particle['b_position'] = particle['position'][:]
    particle['b_cost'] = particle['cost']
    particle['velocity'] = random_vector(vel_space)
    return particle


def get_global_best(population, current_best=None):
    population.sort(key=lambda x: x['cost'])
    best = population[0]
    if current_best is None or best['cost'] <= current_best['cost']:
        current_best = {
            'position': best['position'][:],
            'cost': best['cost']
        }
    return current_best


def update_velocity(particle, global_best, max_v, c1, c2):
    import random
    for i in xrange(0, len(particle['velocity'])):
        v = particle['velocity'][i]
        v1 = c1 * random.random() * (particle['b_position'][i] - particle['position'][i])
        v2 = c2 * random.random() * (global_best['position'][i] - particle['position'][i])
        particle['velocity'][i] = v + v1 + v2
        if particle['velocity'][i] > max_v:
            particle['velocity'][i] = max_v
        if particle['velocity'][i] < -max_v:
            particle['velocity'][i] = -max_v


def update_position(part, bounds):
    for i in xrange(0, len(part['position'])):
        v = part['position'][i]
        part['position'][i] = v + part['velocity'][i]
        if part['position'][i] > bounds[i][1]:
            part['position'][i] = bounds[i][1] - abs(part['position'][i] - bounds[i][1])
            part['velocity'][i] *= -1.0
        elif part['position'][i] < bounds[i][0]:
            part['position'][i] = bounds[i][0] - abs(part['position'][i] - bounds[i][0])
            part['velocity'][i] *= -1.0


def update_best_position(particle):
    if particle['cost'] > particle['b_cost']:
        return
    particle['b_cost'] = particle['cost']
    particle['b_position'] = particle['position'][:]


def search(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2):
    pop = [create_particle(search_space, vel_space) for i in xrange(pop_size)]
    global_best = get_global_best(pop)
    for gen in xrange(0, max_gens):
        for particle in pop:
            update_velocity(particle, global_best, max_vel, c1, c2)
            update_position(particle, search_space)
            particle['cost'] = objective_function(particle['position'])
            update_best_position(particle)
        global_best = get_global_best(pop, global_best)
        print " > gen %d, fitness=%f" % (gen + 1, global_best['cost'])
    return global_best


def main():
    # problem configuration
    problem_size = 2
    search_space = [[-5, 5]] * problem_size
    # algorithm configuration
    vel_space = [[-1, 1]] * problem_size
    max_gens = 100
    pop_size = 50
    max_vel = 100.0
    c1, c2 = 2.0, 2.0
    # execute the algorithm
    best = search(max_gens, search_space, vel_space, pop_size, max_vel, c1, c2)
    print 'Done. Best Solution: c=%f, v=%s' % (best['cost'], str(best['position']))


if __name__ == "__main__":
    main()
