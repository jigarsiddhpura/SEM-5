import random
 
gene = ['01101','11000','01000','10011']
# gene = ['000000','111111','101011','110110']

def selection(gene):
    x = [int(x,2) for x in gene]
    fx = [int(x)*int(x) for x in x]
    fx_sum = sum(fx)
    fx_avg = fx_sum//len(fx)
    excepted_count = [round((i/fx_avg),4) for i in fx]
    actual_count = [round(i) for i in excepted_count]
    mate_pool = []
    for i,j in zip(actual_count,gene):
        if i:
            for c in range(i):
                mate_pool.append(j)
    return x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool

def generate_mate(size,mate_element_size):
    if size % 2 != 0:
        return -1

    available_positions = list(range(size))
    random.shuffle(available_positions)

    mate = [-1] * size
    crossover =[-1] * size
    
    for i in range(size):
        if mate[i] == -1:
            j = random.choice(available_positions)
            while mate[j] != -1 or j == i:
                j = random.choice(available_positions)
            mate[i] = j
            mate[j] = i
            available_positions.remove(i)
            available_positions.remove(j)
    for i in mate:
        if crossover.count(-1) != 0:
            crossover[i] = crossover[mate[i]] = random.randint(1,mate_element_size-1)
    return mate,crossover

def crossover(mate_pool):
    mate, crossover_points = generate_mate(len(mate_pool),len(mate_pool[0]))
    new_poplu = [-1]*len(mate_pool)
    for i in mate:
        new_poplu[i] = mate_pool[i][:crossover_points[i]] + mate_pool[mate[i]][crossover_points[i]:]
        
    x = [int(x,2) for x in new_poplu]
    fx = [int(x)*int(x) for x in x]
    
        
    return mate_pool,new_poplu,mate,crossover_points,x, fx
    

def GA(gene,iter,n):
    if iter == 0:
        return
    
    x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool = selection(gene)
    if sum(actual_count)!=len(gene):
        print("Error dont know what to do at this situation ")
        return 
    print(f"\n------------------------------------------------- GENERATION {n} --------------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value( f(x) )\tProbability(Expected Count)\tActual Count")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{gene[i]}\t\t\t{x[i]}\t\t{fx[i]}\t\t\t{excepted_count[i]}\t\t\t\t{actual_count[i]}")
    mate_pool,new_poplu,mate,crossover_points,x, fx = crossover(mate_pool)
    print(f"\n----------------------------------------------- New Population {n} ------------------------------------------------")
    print("Mate Pool\tMate\t\tCrossover Points\tNew Population\t\tx value\t\tf(x)")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{mate_pool[i]}\t\t{mate[i]}\t\t{crossover_points[i]}\t\t\t{new_poplu[i]}\t\t\t{x[i]}\t\t{fx[i]}")

    GA(new_poplu,iter-1,n+1)

GA(gene,4,0)    