def solution(routes):
    answer = 1
    routes.sort(key = lambda x : x[1]) #그리드를 쓰기위해 먼저 정렬부터 해야함.
    #print(routes)

    point = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > point: #설치한 포인터 지점과 카메라가 만나는지 확
            point = routes[i][1]
            answer += 1
    return answer
