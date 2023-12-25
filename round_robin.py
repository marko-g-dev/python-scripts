import random

PRINT_SIZE = 30
BYE = {}

participants = ['1', '2', '3', '4']
random.shuffle(participants)
if len(participants) % 2 != 0:
    participants.insert(0, BYE)
all_matches = []

num_of_participants = len(participants)
first_participant = participants.pop(0)

for i in range(num_of_participants-1):
    round_matches = []
    last_participant = participants.pop()
    round_matches.append([first_participant, last_participant])
   
    beginning_index = 0
    increment = num_of_participants - 3
    while increment > 0:
        round_matches.insert(0, [participants[beginning_index], participants[beginning_index+increment]])
        beginning_index += 1
        increment -= 2
    
    participants.insert(0, last_participant)
    all_matches.insert(0, round_matches)
    
for i, round_matches in enumerate(all_matches):
    print(f'\n{"*"*(PRINT_SIZE+1)} ROUND {i+1} {"*"*PRINT_SIZE}\n')
    for match in round_matches:
        if BYE in match:
            not_playing = f"{match[1]} is not playing!"
            print(f"{not_playing[:PRINT_SIZE*2+14]:^{PRINT_SIZE*2+14}}")
            continue
        first_participant = f"{match[0][:PRINT_SIZE]:^{PRINT_SIZE}}"
        second_participant = f"{match[1][:PRINT_SIZE]:^{PRINT_SIZE}}"
        print(f'\t{first_participant}\tvs.\t{second_participant}')
