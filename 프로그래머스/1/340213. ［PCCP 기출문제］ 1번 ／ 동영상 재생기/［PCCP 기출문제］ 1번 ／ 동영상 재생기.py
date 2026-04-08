def solution(video_len, pos, op_start, op_end, commands):
    def trans_seconds(list):
        list = list.split(":")
        seconds = int(list[0]) * 60 + int(list[1])
        return seconds
    def to_string(total_seconds):
        mm = total_seconds//60
        ss = total_seconds%60
        return f"{mm:02d}:{ss:02d}"
    video_len = trans_seconds(video_len)
    pos = trans_seconds(pos)
    op_start = trans_seconds(op_start)
    op_end = trans_seconds(op_end)
    if op_start <= pos <= op_end:
            pos = op_end
    for i in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if i == "prev":
            pos = max(0, pos-10)
        else:
            pos = min(video_len, pos+10)
        if op_start <= pos <= op_end:
            pos = op_end
    
    return to_string(pos)