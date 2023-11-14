play_data = {
    'resutlt' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 17
}

# keys()
for key in play_data.keys():
    print(key)
    
# values()
for value in play_data.values():
    print(value)
    
# items()
for key, value in play_data.items():
    print(key, value)