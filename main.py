from defen import setka, take_input, wins_combo

def main():
    counter = 0  # Отвечает за нумерацию хода
    while True:
        setka()  # Печатаем сетку
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = wins_combo()
            if winner:
                setka()
                print('Игрок, играющий за', winner, 'выиграл')
                break
        counter += 1
        if counter > 8:
            setka()
            print('Ничья!')
            break


main()
