# 가장큰수 - 못품
# 1
def solution(numbers):
    answer = ''
    char_numbers = []  # 문자열로 바꾼 배열
    len_ori = 0  # 원래 자릿수 계산용

    # 0 ~ 1000까지 이므로 3번 반복
    for i in numbers:
        char_numbers.append(str(i) * 3)

    # 내림차순 정렬
    char_numbers.sort(reverse=True)

    # 원래 자릿수로 돌려준다
    for idx in range(0, len(char_numbers)):
        len_ori = len(char_numbers[idx]) // 3
        char_numbers[idx] = char_numbers[idx][0:len_ori]

    # 문자열 리스트 하나로 합쳐서 answer에 넣기
    answer = "".join(char_numbers)

    # [0,0,0,0,...] 일 경우 예외처리
    if answer[:1] == '0':
        answer = '0'


# 2
def solution(numbers):
    return str(int("".join((sorted(list(map(str, numbers)), key=lambda x: list(map(int, x)) * 3, reverse=True)))))