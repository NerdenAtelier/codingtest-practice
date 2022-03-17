'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항:
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력:
prices = [1, 2, 3, 2, 3]
return = [4, 3, 1, 1, 0]
'''
#양쪽에서 입출력이 되는 데크를 사용한다.
#앞쪽에서 값을 꺼내, 뒤에 있는 값들과 차례로 비교하여 더 커질 경우 break
#그렇게 측정한 duration 값을 return 값에 입력해준다.
#마지막 값은 뒤에 값이 없으므로 duration이 0이 되어야 함.

import collections

def solution(prices):
    answer = []

    p_deque = collections.deque()
    for p in prices :
        p_deque.append(p)

    while p_deque :
        a = p_deque.popleft()

        if not p_deque :
            answer.append(0)
            break
    
        duration = 0

        for p in p_deque :
            duration += 1
            if p < a :
                break

        answer.append(duration)
    
    return answer