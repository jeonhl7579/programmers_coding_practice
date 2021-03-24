def solution(n, lost, reserve):
    d_reserve=[i for i in reserve if i not in lost]
    d_lost=[i for i in lost if i not in reserve]
    
    for i in d_reserve:
        if i-1 in d_lost:
            d_lost.remove(i-1)
        elif i+1 in d_lost:
            d_lost.remove(i+1)
    return n-len(d_lost)