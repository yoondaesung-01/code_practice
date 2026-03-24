def solution(keyinput, board):
    x_point = 0
    y_point = 0
    x_limit = board[0]//2
    y_limit = board[1]//2
    for i in keyinput:
        if i == "up":
            if y_point < y_limit:
                y_point+=1 
        elif i == "down":
            if y_point + y_limit > 0 :
                y_point-=1
        elif i == "left":
            if x_point + x_limit > 0:
                x_point-=1
        else: # i == "right"
            if x_point < x_limit:
                x_point+=1 
    return [x_point,y_point]