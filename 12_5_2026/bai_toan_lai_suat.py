so_tien_ban_dau = 10000000
lai_suat = 0.051


def so_tien_sau_10_nam():
    
    so_tien = so_tien_ban_dau
    
    for _ in range(10):
        so_tien = so_tien + (so_tien * lai_suat)
    return so_tien

print('Sau 10 năm có %d VNĐ' %so_tien_sau_10_nam())



def co_it_nhat_50_trieu():
    
    so_tien = so_tien_ban_dau
    so_nam = 0
    
    while so_tien < 50000000:
        so_tien = so_tien + (so_tien * lai_suat)
        so_nam += 1
    return so_nam

print('Có ít nhất 50000000 VNĐ sau %d năm' %co_it_nhat_50_trieu())
        
        