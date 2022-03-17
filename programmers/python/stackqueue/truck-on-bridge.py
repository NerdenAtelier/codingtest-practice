'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한조건:
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

입출력:
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
return = 8
'''
# 다리 역할을 하는 데크를 만든다. 
# 여기서 핵심은 다리의 길이를 구현하기 위해 0으로 채워서 초기화를 해야 한다는 것이다.
# 다리에 진입하는 차는 다리 데크에 들어가고, 다리에서 나오는 차는 다리 데크에서 나온다.
# 다리 위에 있는 차의 무게를 항상 관찰하여 상황에 맞게 차를 진입시키거나, 진행만 시킨다.
# 시간 카운트를 증가시키다가 도착한 차의 수를 관찰하여 처음 차들의 수와 같아지면 종료.

import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
   
    bridge_deque = collections.deque()

    truck_weights.reverse()

    for i in range(bridge_length) :
        bridge_deque.append(0)

    #트래킹해야하는 요소들을 변수로 선언
    time = 0
    onbridge = 0
    arrived = []
    nums_of_trucks = len(truck_weights)

    while len(arrived) < nums_of_trucks :
        a = bridge_deque.popleft()
        if a != 0 :
            arrived.append(a)
            onbridge -= a
        time += 1
        if truck_weights and weight - onbridge >= truck_weights[-1] :
            b = truck_weights.pop()
            bridge_deque.append(b)
            onbridge += b
        else :
            bridge_deque.append(0)

    answer = time

    return answer