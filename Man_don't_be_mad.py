from random import randint

def game(length, output=True):
    if length < 2:
        print('Please write a value higher than or equal to 2')
        output = False
        return None
    
    position = 1
    dice_count = []    
    counter = 0
    
    while position != length:
        random_throw = randint(1,6)
        dice_count.append(random_throw)
        
        if random_throw == 6:
            continue
        elif random_throw == 5:
            position -= sum(dice_count)
            
        position += sum(dice_count)
        
        if position > length:
            position -= sum(dice_count)
            dice_count.clear()
            continue    
            
        if output:
            print(f'{counter + 1}. round:', end=' ')
            print(*dice_count, end=' ')
            print(f'-> New position: {position}')
        
        dice_count.clear()
        counter += 1

    if output:
        print(f'Game ended in {counter}. round.') 
    return counter

# Analyzes the average length of the game
def game_analysis(length, count):
    analysis_length = 0
    
    for _ in range(count):
        analysis_length += game(length, False)
    return analysis_length / count
 
# the average length of the game for sizes 2-50 
def game_average_length(count) -> None:
    for i in range(2, 51):
        average_length = game_analysis(i, count)
        print(f'Plan with length: {i}  ->  {average_length}')
        
if __name__ == '__main__':
    game(170)
    print('The average length of the game:',game_analysis(40, 20))
    game_average_length(20)
    pass