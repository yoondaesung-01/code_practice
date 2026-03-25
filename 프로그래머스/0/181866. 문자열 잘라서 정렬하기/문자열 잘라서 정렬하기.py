def solution(myString):
    split_list = myString.split("x")
    answer = [s for s in split_list if s != ""]
    return sorted(answer)