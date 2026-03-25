def solution(lines):
    s1 = set(range(lines[0][0],lines[0][1]))
    s2 = set(range(lines[1][0],lines[1][1]))
    s3 = set(range(lines[2][0],lines[2][1]))
    overlap = (s1 & s2) | (s2 & s3) | (s1 & s3) 
    return len(overlap)