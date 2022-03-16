'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한사항:
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.

입출력예시:
phone_book : ["119", "97674223", "1195524421"]
return : false

'''

# 리스트 내의 전화번호들 중, [어떤 번호가 다른 번호의 접두사인 경우]가 있는지를 확인하는 문제이다.
# 즉, 어떤 번호가 어떤 번호의 앞쪽 부분집합인지 아닌지 확인하라는 뜻이다.
# 주어지는 배열의 길이가 최대 1,000,000이므로 조회 과정에서 해시를 사용하지 않으면 효율적으로 풀 수 없다.

# 짧은 번호의 접두 부분부터 확인하는 것이 효율적이므로, 전화번호부를 번호 길이 순으로 오름차순 정렬한다.
# 반복문을 통해 접두부를 만들어보면서 그 접두부가 해시화한 전화번호부에 존재하는 Key인지 확인한다.

import collections

def solution(phone_book) :
    #없는 key를 조회해도 오류가 나지 않도록 defaultdict 사용
    phone_dict = collections.defaultdict(int)
    
    #전화번호부의 번호들을 phone_dict에 저장
    for num in phone_book :
        phone_dict[num] = 1

    #전화번호부 배열을 길이가 짧은 순서대로 나열
    phone_book = sorted(phone_book, key=len)

    #접두부를 만들어가면서 딕셔너리에서 조회
    for num in phone_book : 
        jubdoo = ''
        for d in range(len(num)-1) :
            jubdoo += num[d]
            if jubdoo in phone_dict :
                return False

    #모든 과정을 거칠때가지 false가 아니면 true
    return True