# dmoj ecoo19r2p1

def clean(address):
# +, @ 사이에 문자열을 제거하는 코드
    plus_loc = address.index('+')
    gol_loc = address.index('@')
    email = address[:plus_loc]+address[gol_loc+1:]
    print('ok')

clean('gg+....@gmail.com')
