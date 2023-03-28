import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь       2, 26, 50, 75, 100
    count = 0
    predict = 0
    predict_zero = 0
    info_range = 0
    
    if type(number) != int:
        print()
    while True:     #Определяем квартель, в которм число
        if count == 0:
            predict = 50
            count = count+1
            if predict == number:
                break
        elif predict > number and count < 4:
            predict_zero = predict
            predict = predict - 25
            count = count + 1
            if predict == number:
                break
        elif predict < number and count <= 3:
            predict_zero = predict
            predict = predict + 25
            count = count + 1
            if predict == number:
                break
        if count > 3:
            break
                

        #определяем число 
            
    if predict_zero > predict: #Если число меньше 50
            info_range = predict + abs(predict_zero - predict)//2
    if predict_zero < predict: #Если число больше 50
            info_range = predict_zero + abs(predict - predict_zero)//2
    for i in range(abs((predict - predict_zero)//2)):
        if info_range < number:
            #predict == info_range
            info_range = info_range + 1
            count = count + 1
            
        if info_range > number:
            #predict == info_range
            info_range = info_range - 1
            count = count + 1

        if info_range == number:
            break

     # Ваш код заканчивается здесь
    return count

def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)