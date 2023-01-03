# boj 2386
# 문자열 / 브루트포스 알고리즘

# 현재 스크립트 파일이 실행되는 상태 => name 변수가 main 이면 아래 코드 실행하라
# __name__ 변수의 값이 __main__인지 확인하는 코드는 현내 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업
# 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도
# 모듈에 if __name__=='__main__'이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것으로 생각하면 쉬울 것이다.

if __name__ == '__main__':
    while True:
        question = input()
        if question == '#':
            break
        alphabet, sentence = question[0], question[1:].lower()
        print(alphabet, sentence.count(alphabet))