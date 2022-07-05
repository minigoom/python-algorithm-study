password = input()
password = list(password)
len_password = len(password)
    
lower = 0
upper = 0
dig = 0
for i in password:
    if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        lower += 1
        
    elif i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        upper += 1
    elif i in ['0','1','2','3','4','5','6','7','8','9']:
        dig += 1
if lower >= 3 and upper>=2 and dig >=1 and len_password>=8 and len_password<=12:
    print('Valid')
else:
    print('Invalid')