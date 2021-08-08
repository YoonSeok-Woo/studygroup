def solution(files):
    answer=[]
    str=[]
#solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])

    for s in files:
        #print(s)    #img12.png  img10.png   img02.png   img1.png    IMG01.GIF   img2.JPG
                    #F-5 Freedom Fighter    B-50 Superfortress      A-10 Thunderbolt II     F-14 Tomcat

        #HEAD
        HEAD=''
        for char in s:  #s: #img12.png   img10.png   img02.png   img1.png    IMG01.GIF   img2.JPG
            if char.isdigit() == True:      #"if char.isdigit()"로도 쓸 수 있음.
                                            #char이 각각의 s에 대해 1  1  0  1  0  2 일때 break
                break
            else:
                HEAD += char            #각각의 s에서 1 1 0 1 0 2가 되기 전까지는 HEAD에 각 문자열 'i' 'm' 'g' 등이 더해짐

        # NUMBER
        NUMBER=''        
        for char in s[len(HEAD):]:  #원본 s에서 위에서 구한 HEAD를 자른 이후부터 #len(HEAD) : 3 // \i\m\g\[3]\12.png
            if char.isdigit() == False: #"if not char.isdigit()"로도 쓸 수 있음.
                                        #HEAD를 제외한 남은 문자열에서 digit이 아닌 문자(여기선 . . . . . 을 만나면) break / 만나기 전까지의 digit들은 NUMBER에 스트링으로 더해줌
                break
            else:
                NUMBER+=char


        #HEAD,NUMBER,s(원본)
        str.append([HEAD.lower(),int(NUMBER),s])        #여기서 str[]의 의도는? / 빈 리스트에 이 위치에서, 지금까지 값이 다 나온 3개의 인자를 추가
        print(str)                                      #단, HEAD부분은 모두 소문자로 바꿔서 넣어줌. (대소문자 간 정렬 레벨차이 없으므로)
                                                        #여기서는 빈 리스트 안에 리스트 자체를 어펜드해버림 (최초값도 같이 보기 위해 s도 함께 어펜드). 
                                                        #[['img', 12, 'img12.png'], ['img', 10, 'img10.png'], ['img', 2, 'img02.png'], ['img', 1, 'img1.png'], ['img', 1, 'IMG01.GIF'], ['img', 2, 'img2.JPG']...]
    
    
    s_list = sorted(str, key=lambda x:(x[0],x[1]))    #새로운 리스트(s_list)로 sorted된 리스트 할당. / 첫번째 자리수 기준 --> 두번째 자리수 기준 
    for indiv_list in s_list:                         #정렬된 리스트(s-list)안의 각각 리스트인자들(indiv_list)를 for문으로 돌림
        answer.append(indiv_list[2])                  #s_list안의 개별 indiv_list의 2번째값(s)를 출력

    print(answer)
    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])



#알게된 점:isdigit()함수 사용법, lambda 사용.
#head에 대해, head가 아닌 부분에 대해 isdigit()을 이용.
#조건에 따라 정렬
#참조: https://ariz1623.tistory.com/281
#lower() : 
#--------------------------------------------------------------------

# def solution(files):
#     answer = []
#     useless = ['.', '-', ' ']
#     str_num = ['0','1','2','3','4','5','6','7','8','9']
#     #.나 '-'나 ' '은 무시하면 좋을 것 같으니. 일단 있으면 빼주자
#     for elem in files:
#         a = []
#         for punct in useless:
#             if punct in elem:
#                 a = elem.replace(punct, '')     #. - ' '을 빼고 붙여버리기  #이런 결과는 어디에 붙어야 하나?
#             #print(a)                                    #틀린 이유, replace는 원본값을 바꾸지 않음 / a라는 다른 변수를 만들어 거기에 할당하여 a를 출력
#         #print(a)    #"img12png" "img10png" "img02png" "img1png" "IMG01GIF" "img2JPG"
# """        b_front = []
#         b_end = []
#         for num in str_num:
#             if num in a:
#                 #슬라이싱
#                 b_front.append(a[:a.index(num)])
#                 b_end.append(a[a.index(num):])
#                 break       #한번만 슬라이싱 되면 그만두기
#         print(b_front)  #['img']
#         print(b_end)    #['12png']"""       #이렇게 하면 안되는게.. str_list

                



        #이제 여기서 str(숫자)가 걸리는 기준으로 a문자열을 슬라이싱.
        
        #그 후 1. 앞부분(문자)인 영문 대소문자를 모두 small or large case로 바꿔서 한번에 비교 --> 다음에는 이어서 숫자를 비교 --> 다음에는 이어서 파일형식 문자를 비교


        #생각해볼 점. .txt등 형식이 붙는 파일과 빈 문자열 간의 비교.


    
    # return answer


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])


# 입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# 입력: ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]