def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        current_idx = player_dict[calling]
        
        prev_idx = current_idx - 1
        prev_player = players[prev_idx]
        
        players[prev_idx], players[current_idx] = players[current_idx], players[prev_idx]
        
        player_dict[calling] = prev_idx
        player_dict[prev_player] = current_idx
        
    return players