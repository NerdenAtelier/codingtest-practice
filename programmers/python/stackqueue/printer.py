'''
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항:
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

입출력:
priorities: [2, 1, 3, 2]
location: 2
return: 1
'''
# 특정한 작업(인덱스로 주어지는)이 몇 번째로 인쇄되는지 확인하고 싶다 = 대기 Queue에서 언제 빠져나가는지 알고 싶다.
# 현재 Queue의 가장 앞에 있는 작업에게는 선택지가 두 가지 있다.
# (1) 전체에서 우선순위가 가장 높은 값일 경우 : 인쇄가 된다 (= Queue에서 제거된다)
# (2) 우선순위가 더 높은 다른 작업이 있을 경우 : Queue의 가장 뒤로 다시 줄을 선다.
# 여기서 중요한 점은 어떤 선택지를 택하더라도, 작업의 '우선순위'와 '고유번호(인덱스)'를 유지한 채로 움직여야 한다는 것이다.
# 따라서 우선순위와 고유번호를 Queue에 값으로 담아 확인하면서 값을 제거 혹은 다시 대기열에 편입시켜야 한다.
# 두 값을 페어로 묶어 하나의 Queue를 만들 수도 있겠으나, 나의 경우는 각각을 관리하는 Queue를 하나씩 만들어 동시에 같은 방식으로 동작하도록 하였다.

import collections

def solution(priorities, location):
    answer = 0

	#효율적인 자료형 deque를 사용
	#priority를 관리하는 deque와 index를 관리하는 deque
    p_deque = collections.deque()
    i_deque = collections.deque()

    for i in range(len(priorities)) :
        p_deque.append(priorities[i])
        i_deque.append(i)

	#현재 남은 작업들 사이의 가장 높은 우선순위 값
    p_max = max(p_deque)
    	#인쇄된 작업의 수
    count = 0

    while p_deque :
    	#현재 가장 앞의 작업이 우선순위가 가장 높은 작업이면 인쇄
        if p_deque[0] == p_max :
        #그 때, 그게 우리가 원하는 값이면 인쇄 후 종료
            if i_deque[0] == location :
                count += 1
                answer = count
                break
            count += 1
            p_deque.popleft()
            i_deque.popleft()
            p_max = max(p_deque)
        #우선순위가 가장 높지 않다면 나중으로 미룸
        else :
            p_deque.append(p_deque.popleft())
            i_deque.append(i_deque.popleft())

    return answer