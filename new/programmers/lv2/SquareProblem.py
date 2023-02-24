def solution(w,h):
    w_list = []
    h_list = []
    for i in range(1, w+1):
        if w % i == 0:
            w_list.append(i)
    for i in range(1, h+1):
        if h%i == 0:
            h_list.append(i)
    hw_list = set(w_list).intersection(h_list)
    return w*h - (w+h-max(hw_list))