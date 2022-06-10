def search_for_number(lst, query):
    # freq_arr = [0] * max(query) + 1

    lst.reverse()
    
    for item in query:
        if item not in lst:
            idx = -1
        else:
            idx = len(lst) - lst.index(item) -1
        print("query ", item, " answer is ", idx)



lst = list(map(int, input().split()))
query = list(map(int, input().split()))
search_for_number(lst, query)