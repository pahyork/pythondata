# 커피자판기
# 1. 커피자판기 2. 메뉴추가 3. 메뉴삭제 4. 메뉴목록 5. 종료
# - 프로그램이 시작될 때 필요한 정보를 읽어서 시작합니다
# - 커피자판기: 무한반복하면서 돈을 입력받아 메뉴를 선택해서 처리
# - 메뉴추가: 자판가에서 판매하는 메뉴를 추가하는 기능(메뉴명, 가격)
# - 메뉴삭제: 전체 목록을 보여주고 삭제하고자 하는 항목을 선택하도록 해서 삭제 처리
# - 메뉴목록: 메뉴이름순, 메뉴가격순으로 정렬하여 출력
# - 종료: 저장할 정보가 있으면 저장하고 종료

import json

def data_load(path):
    f = open(path,'r')
    data = json.load(f)
    f.close()
    return data

def data_save(path,data):
    f = open(path,'w')
    json.dump(data,f)
    f.close()

def choice_menu(item):
    while True:
        for k,v in item.items():
            print(f'{k}: {v:,}원 ', end = ' ')
        print()
        choice = input('(종료: enter)메뉴선택 >>>')
        if choice == '':
            break
        money = ''
        while not money.isdigit():
            money = input('금액 투입 >>>')
        money = int(money)
        if choice in item.keys():
            if money >= item[choice]:
                money -= item[choice]
                print(f'{choice} 서비스합니다 거스름돈은 {money}원~')
            else:
                print('금액이 부족합니다')
        else:
            print('해당 메뉴가 없습니다')

def add_menu(item):
    menu_name = input('메뉴이름 >>>')
    menu_price = ''
    while not menu_price.isdigit():
        menu_price = input('메뉴가격 >>>')
    menu_price = int(menu_price)
    
    if menu_name in item.keys():
        print(f'{menu_name} 메뉴가 있습니다')
    else:
        print(f'{menu_name} 메뉴를 추가합니다')
    item[menu_name] = menu_price
    print(item)

def del_menu(item):
    menu_name = input('삭제하려는 메뉴이름 >>>')
    if menu_name in item.keys():
        print(f'{item.pop(menu_name)} 메뉴를 삭제합니다')
        del item[menu_name]
    else:
        print(f'{menu_name} 메뉴가 없습니다')
    print(item)

def show_list(item):
    menu_1 = input('1. 이름순 2. 가격순 >>>')
    if menu_1 == '1':
        for k,v in sorted(item.items(),key = lambda x : x[0]):
            print(f'{k:>25} : {v:10,}원')
    elif menu_1 == '2':
        for k,v in sorted(item.items(),key = lambda x : x[0]):
            print(f'{k:>25} : {v:10,}원')