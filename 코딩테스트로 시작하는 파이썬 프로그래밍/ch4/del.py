new_id = "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    ok_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','-','_','.']
    # step 1
    new_id = new_id.lower
    # step 2
    new_id_2 = ""
    for i in new_id:
        if i in ok_list:
            new_id_2 = new_id_2 + i
    print(new_id)

solution("...!@BaT#*..y.abcdefghijklm")