

from Homework_8.example import get_data_from_json

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)



def take_input_for_x(player_token):
    array_from = get_data_from_json('x_file.json')
    for i in range(len(array_from)):
        valid = False
        while not valid:
            player_answer = array_from[i]

            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(board[player_answer - 1]) not in "XO"):
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
                    break
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")

def take_input_for_y(player_token):
    array_from = get_data_from_json('y_file.json')
    for i in range(len(array_from)):
        valid = False
        while not valid:
            player_answer = array_from[i]

            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(board[player_answer - 1]) not in "XO"):
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
                    break
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")



def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    input("Нажмите enter для старта")
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input_for_y("O")
        else:
            take_input_for_x("X")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")

if __name__ == "__main__":
    main()
