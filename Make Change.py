import copy

def make_change(n, coins):
    count = [[] for i in xrange(n + 1)]
    
    for i in xrange(len(coins)):
        count[coins[i]] = [[coins[i]]]

    for i in xrange(n + 1):
        for j in xrange(len(coins)):
            if i - coins[j] < 0:
                continue
            for sol in count[i - coins[j]]:
                new_sol = copy.copy(sol)
                new_sol.append(coins[j])
                new_sol.sort()
                if new_sol not in count[i]:
                    count[i].append(new_sol)
                    
    return len(count[n])

n = 14
coins = [10, 7, 1]
print make_change(n, coins)

#f(3, [1]) 1
#f(3, [1, 2]) 2
#f(5, [2, 3, 5]) 2
#f(14, [10, 7, 1]) 4
