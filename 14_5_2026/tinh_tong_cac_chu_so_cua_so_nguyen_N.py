def total(N):

    str_N = str(abs(N))
    
    tong = 0
    for chu_so in str_N:
        tong += int(chu_so)
    return tong


print(total(999))