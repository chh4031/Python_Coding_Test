import collections # 딕셔너리 자료구조 사용
def solution(id_list, report, k):
    answer=[]
    report = list(set(report)) #set는 중복을 허용하지 않는 자료구조, list로 다시 리스트로 변경
    #print(report)
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int) #기본은 0 초기값

    for i in report:
        user, userp = i.split(' ') #문자열을 분리시키는 부분, user는 앞쪽, userp는 뒤쪽 split 활용은 알고 있었으나 분리해서 어떻게 저장하는지에 대해서 몰랐음. 기억
        reportHash[user].add(userp)
        stoped[userp] += 1
    #print(reportHash)
    for name in id_list:
        mail_count = 0
        for user in reportHash[name]:#reportHash의 name키의 값에 해당하는 데이터가 하나씩 user로 들어감
            if stoped[user] >= k: #신고당한 값은 stoped에 있음. 그래서 그거랑 k값 비교
                mail_count+=1
        answer.append(mail_count)# name이 받는 mail_count의 값이 나옴.

    return answer
    
