def sort_last(*tuples):

    '''Given a list of non-empty tuples, return a list sorted in increasing
    order by the last element in each tuple'''

    l = list(tuples)
    d = {}
    for i in l:


    # l1 = sorted(l.)
    print(d)

z = sort_last((1, 3), (3, 2), (2, 1))
#      [(2, 1), (3, 2), (1, 3)])
# test(sort_last([(2, 3), (1, 2), (3, 1)]),
#      [(3, 1), (1, 2), (2, 3)])
# test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
#      [(2, 2), (1, 3), (3, 4, 5), (1, 7)])