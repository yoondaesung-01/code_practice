def solution(code):
    ret = ''
    code_list = list(code)
    mode = 0
    for i in range(len(code_list)):
        if mode == 0:
            if code_list[i] == "1":
                mode = 1
            else:
                if i % 2 ==0:
                    ret+= code_list[i]
        else:
            if code_list[i] == "1":
                mode = 0
            else:
                if i % 2 == 1:
                    ret+= code_list[i]
    return ret if ret else "EMPTY"