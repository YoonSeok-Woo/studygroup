def pcheck(pat):
    s, e = 0, len(pat) - 1
    while s <= e:
        if pat[s] == pat[e] or (pat[s] == '?' or pat[e] == '?'):
            s += 1
            e -= 1
        else:
            return 'Not exist'
    return 'Exist'

T = int(input())
for tc in range(T):
    print(f'#{tc + 1} {pcheck(input())}')


# T = int(input())
# for tc in range(T):
#     answer = 'Exist'
#     pat = input()
#     s, e = 0, len(pat) - 1
#     while s <= e:
#         if pat[s] == pat[e] or (pat[s] == '?' or pat[e] == '?'):
#             s += 1
#             e -= 1
#         else:
#             answer = 'Not exist'
#             break

#     print(f'#{tc + 1} {answer}')