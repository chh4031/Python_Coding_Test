import math
def solution(fees, records):
    answer = []
    inTime = [0]*10000#들어온시간기록
    isIn = [0] * 10000#차량이 있는지 없는지 기록
    sumT = [0] * 10000#누적 시간
    # 리스트가 3개 필요하다.

    for record in records:
        a, b, c = record.split( )#데이터를 공백을 기준으로 3개로 분리시킴
        #print(a, b, c)
        h, m = a.split(":")#시간을 다시 공백을 기준으로 분리시킴
        #print(h, m)
        if c == "IN":
            inTime[int(b)] = int(h)*60+int(m)
            isIn[int(b)] = 1
        else:
            sumT[int(b)] += (int(h)*60+int(m))-inTime[int(b)]
            isIn[int(b)]=0
    for i in range(10000):
        if isIn[i] == 1:
            sumT[i] += (23*60+59)-inTime[i]
    for i in range(10000):
            if sumT[i] > 0:
                answer.append(fees[1] + max(math.ceil((sumT[i]-fees[0])/fees[2]), 0)* fees[3])
    return answer
