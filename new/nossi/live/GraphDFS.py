# 2 / 14
# https://leetcode.com/problems/keys-and-rooms/
# DFS => BIG O(V + E) vertex(노드) + edge(간선)

def canVisitAllRooms(rooms):
    visited = []

    def dfs(v):
        visited.append(v)
        for next_v in rooms[v]:
            if next_v not in visited:
                dfs(next_v)

    dfs(0)

    if len(visited) == len(rooms):
        return True
    else:
        return False
    return visited


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if visited[next_v] == False:
                dfs(next_v)

    dfs(0)

    return all(visited)

    if len(visited) == len(rooms):
        return True

    else:
        return False

    # return visited


# def canVisitAllRooms(rooms):
#     visited = [False] * len(rooms)
#
#     def dfs(v):
#         visited[v] = True
#         for next_v in rooms[v]:
#             if visited[next_v] == False:
#                 dfs(next_v)
#
#     dfs(0)
#
#     if len(visited) == len(rooms):
#         return True
#
#     else:
#         return False


# from collections import deque
#
# def canVisitAllRooms(rooms):
#     visited = [False] * len(rooms)
#
#     # v에 연결되어있는 모든 vertex 방문할 것이다.
#
#     def bfs(v):
#         queue = deque()
#         queue.append(v)
#         visited[v] = True
#         while queue:
#             cur_v = queue.popleft()
#             for next_v in rooms[cur_v]:
#                 if visited[next_v] == False:
#                     queue.append(next_v)
#                     visited[next_v] = True
#
#     bfs(0)
#
#     return all(visited)

rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))