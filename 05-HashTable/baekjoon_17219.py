from sys import stdin

class Solution:
    def findPassword(self):   #비밀번호 찾기

        input = stdin.readline

        N, M = map(int, input().split())
        add = {}

        for _ in range(N):
            site, ps = input().split()
            add[site] = ps

        for _ in range(M):
            print(add[input().rstrip()])


if __name__ == "__main__":
    s = Solution()

    s.findPassword()

# 16 4
# noj.am IU
# acmicpc.net UAENA
# startlink.io THEKINGOD
# google.com ZEZE
# nate.com VOICEMAIL
# naver.com REDQUEEN
# daum.net MODERNTIMES
# utube.com BLACKOUT
# zum.com LASTFANTASY
# dreamwiz.com RAINDROP
# hanyang.ac.kr SOMEDAY
# dhlottery.co.kr BOO
# duksoo.hs.kr HAVANA
# hanyang-u.ms.kr OBLIVIATE
# yd.es.kr LOVEATTACK
# mcc.hanyang.ac.kr ADREAMER
# startlink.io
# acmicpc.net
# noj.am
# mcc.hanyang.ac.kr

