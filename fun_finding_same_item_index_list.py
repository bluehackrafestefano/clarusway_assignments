def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

source = "ABABDBAAEDSBQEWBAFLSAFB"
print(list_duplicates_of(source, 'B'))
Prints:

[1, 3, 5, 11, 15, 22]