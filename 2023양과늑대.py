import numpy as np

def solution(info, edges):
    N = len(info)
    visited = np.zeros(N, dtype=int)  # 노드 방문 여부를 저장하는 배열 (0: 미방문, 1: 방문)
    visited[0] = 1  # 루트 노드는 항상 방문으로 설정
    answer = []  # 최대 양의 개수를 저장할 리스트

    def dfs(sheep, wolf):
        if sheep > wolf:  # 현재 양의 개수가 늑대의 개수보다 많은 경우
            answer.append(sheep)  # 최대 양의 개수를 갱신
        else:
            return  # 양이 늑대보다 적거나 같은 경우, 더 이상 진행하지 않음

        for i in range(len(edges)):  
            parent, child = edges[i]  # 부모와 자식 노드를 가져옴
            isWolf = info[child]  # 현재 자식 노드가 늑대인지 양인지 확인

            # 부모 노드는 이미 방문했고 자식 노드는 방문하지 않은 경우에만 진행
            if visited[parent] and not visited[child]:
                visited[child] = 1  # 자식 노드를 방문으로 설정
                dfs(sheep + (isWolf == 0), wolf + (isWolf == 1))  
                visited[child] = 0  # 재귀 호출이 끝나면 다시 방문하지 않은 상태로 변경

    dfs(1, 0)  # 루트 노드에서 DFS 시작
    return max(answer)  # 최대 양의 개수 반환
