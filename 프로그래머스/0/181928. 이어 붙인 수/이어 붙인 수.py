def solution(num_list):
    odd_sum = ''
    even_sum = ''
    for i in num_list:
        if i % 2 == 0:
            even_sum+=str(i)
        else:
            odd_sum+=str(i)
    return int(even_sum)+int(odd_sum)