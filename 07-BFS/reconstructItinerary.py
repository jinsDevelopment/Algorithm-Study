from typing import List
from collections import defaultdict

class Solution:
    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:

        # defaultdict 써준 이유 ?
        # value가 없으면 key가 생성이 안되서 추가로 key가 없을 때라는 if절을 추가 해야 한다.

        dic = defaultdict(list)

        # 그래프를 역순으로 구성
        for a, b in sorted(tickets, reverse=True):
            dic[a].append(b)

        route = []

        def dfs(a):
            # 마지막 값을 읽어 어휘 순으로 목적지 방문
            while dic[a]:
                pop = dic[a].pop() # 시간복잡도 pop() -> O(1), pop(0) -> O(N)
                dfs(pop)

            route.append(a)

        dfs("JFK")
        #다시 뒤집어 어휘 순 결과로 -> stack 형태로 데이터가 거꾸로 쌓인다.

        return route[::-1]


    def findItineraryStack(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']

        while stack:

            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:

                # print(f'graph[stack[-1]]: {graph[stack[-1]]}')
                stack.append(graph[stack[-1]].pop(0))
                # print(f'stack : {stack}')

            # print(f'route : {route}')
            route.append(stack.pop())
            # print(route)
        # 다시 뒤집어 어휘 순 결과로

        return route[::-1]



if __name__ == "__main__":

    s = Solution()

    # tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

    assert s.findItineraryDFS((tickets)) == ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']

    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

    assert s.findItineraryStack(tickets) == ['JFK', 'NRT', 'JFK', 'KUL']

