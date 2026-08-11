from itertools import permutations
def total_cost(a,c):
    return sum(c[i][a[i]] for i in range(len(a)))
def assignment_problem(c):
    best=float("inf")
    best_a=None
    for a in permutations(range(len(c))):
        cost=total_cost(a,c)
        if cost<best:
            best=cost
            best_a=a
    return best_a,best
c=eval(input("Enter cost matrix: "))
a,cost=assignment_problem(c)
print("Optimal Assignment:",[(i+1,a[i]+1) for i in range(len(a))])
print("Total Cost:",cost)
