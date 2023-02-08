import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_to_pokemon = dict()

for i in range(1, N+1):
    num_to_pokemon[i] = input().rstrip()

pokemon_to_num = dict(zip(num_to_pokemon.values(), num_to_pokemon.keys()))
# pokemon_to_num = {x:y for y, x in num_to_pokemon.items()}

for _ in range(M):
    question = input().rstrip()
    
    if question.isdigit():
        print(num_to_pokemon[int(question)])
    else:
        print(pokemon_to_num[question])