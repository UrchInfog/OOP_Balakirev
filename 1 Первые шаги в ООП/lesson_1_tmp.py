import itertools
import sys


def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None

# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns.
# ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.
# With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].
#######################################################################################################################

# from itertools import combinations
#
# def choose_best_sum(t, k, ls):
#     return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)

#######################################################################################################################

# from itertools import combinations
#
# def choose_best_sum(t, k, ls):
#     return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)

#######################################################################################################################

# def choose_best(t,k,ls):
#     if k == 0: return 0
#     best = -1
#     for i, v in enumerate(ls):
#         if v > t: continue
#         b = choose_best(t - v, k - 1, ls[i+1:])
#         if b < 0: continue
#         b += v
#         if b > best and b <= t:
#             best = b
#     return best
#
# def choose_best_sum(t, k, ls):
#     c = choose_best(t,k,ls)
#     if c <= 0 : return None
#     return c
