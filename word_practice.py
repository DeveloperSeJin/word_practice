import pandas as pd
import argparse
import os
import platform

def practice(df, cl):
    review_index = []

    for idx, row in df.iterrows():
        os.system(cl)
        print('[' + str(idx+1) + '] '+ row['단어'])
        word = [row['뜻1'],row['뜻2'],row['뜻3'],row['뜻4'],row['그외']]
        means = input('뜻을 입력: ')
        print()
        print([ w for w in word if str(w) != ''])
        print(means)
        while True:
            try:
                answer = input('맞았습니까?(0/1/종료=q): ')
                if answer == 'q':
                    return review_index
                elif int(answer) == 1 or int(answer) == 0:
                    if not int(answer):
                        review_index.append(idx)
                    break
                else:
                    raise
            except:
                print('0또는 1을 입력하시오.')
                continue
        print()
        print()

    os.system(cl)
    if len(review_index) == 0:
        print('모든 단어를 맞췄습니다.')
    else:
        print('맞은 개수: ', (len(df)-len(review_index)))
        print('틀은 개수: ', len(review_index))
        print(df.loc[review_index])
    print()
    print()

    return review_index

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='파일의 경로를 적으시오')
    parser.add_argument('Day', help='공부할 일차를 적으시오')
    args = parser.parse_args()
    
    match platform.system():
        case 'Windows':
            clear = 'cls'
        case 'Linux':
            clear = 'clear'
            
    words = pd.read_excel(args.path, engine='openpyxl', sheet_name=args.Day)
    words = words.fillna('')
    idx = practice(words, clear)

    while True:
        try:
            if len(idx) == 0:
                retry = int(input('종료/처음부터(0/1): '))
                match retry:
                    case 0:
                        break
                    case 1:
                        idx = practice(words, clear)
                    case _:
                        print('0/1 중 하나를 입력하시오.')
            else:
                retry = int(input('종료/처음부터/틀린 단어 복습(0/1/2): '))
                match retry:
                    case 0:
                        break
                    case 1:
                        idx = practice(words, clear)
                    case 2:
                        idx = practice(words.loc[idx], clear)
                    case _:
                        print('0/1/2 중 하나를 입력하시오.')
        except:
            print('숫자를 입력하시오.')
        print()
        print()