import collections
def solution(gems):
    answer = [0,0] #구간 저장
    sH = collections.defaultdict(int) #카운팅을 위한 딕셔너리
    k = len(set(gems)) #중복을 제거한 후의 보석의 종류(보석의 길이), 사야하는 보석의 길이
    lt = 0
    maxL = 1000000 #구간의 길이가 가장 작은 것을 찾아야 되기 때문에 큰 수로 잡아놓은것

    for rt in range(len(gems)):
        sH[gems[rt]]+=1 #해당 보석의 갯수를 카운팅
        while(len(sH) == k):#lt ~ rt 까지의 길이
            if rt - lt + 1 < maxL:#해당 구간의 길이
                maxL = rt - lt + 1
                answer = [lt+1, rt+1]#인덱스가 0부터 시작해서 +1 시킴
            sH[gems[lt]] -=1
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]
            lt += 1
    return answer
