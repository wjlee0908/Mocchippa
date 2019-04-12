import random

def check_win(player, opponent):
    # player가 이기면 1, 비기면 0, opponent가 이기면 -1 반환
    # int보단 이름 붙인 열거형(enum) 반환하는 게 더 명확함
    if (player=='묵' and opponent=='찌') or \
        (player=='찌' and opponent=='빠') or \
            (player=='빠' and opponent=='묵'):
            return 1
    elif (player=='묵' and opponent=='빠') or \
        (player=='찌' and opponent=='묵') or \
            (player=='빠' and opponent=='찌'):
            return -1
    else:
        return 0

def input_rps():
    player_result['user'] = input('user: ')
    player_result['computer'] = random.choice(rps_list)
    print('computer:', player_result['computer'])


rps_list = ['묵', '찌', '빠']
player_result = {'user':'','computer':''}
turn = ''

# 최초 가위바위보
while turn == '':
    print('묵 찌 빠!')
    input_rps()

    rps_result = check_win(player_result['user'], player_result['computer'])

    if rps_result == 0:
        turn = ''
        print('비김! 다시')
    elif rps_result < 0:
        turn = 'computer'
    else:
        turn = 'user'

# 묵찌빠 게임 반복
while True:
    print("{0}: {1}에 {1}에...".format(turn, player_result[turn]))
    input_rps()
    
    rps_result = check_win(player_result['user'], player_result['computer'])

    # 비기면 현재 턴인 사람 승리
    if rps_result == 0:
        print("---------------------")
        print("{0} 승리!".format(turn))
        break
    elif rps_result == 1:
        turn = 'user'
    else:
        turn = 'computer' 