""" 3:18 """
def solution(bridge_length, weight, truck_weights):
    time = 0
    boolean = True
    bridge = []
    truck_bridge = []
    com = []
    num = len(truck_weights)
    while(len(com) != num):
        if len(truck_weights) > 0 and sum(bridge) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            truck_bridge.append(bridge_length)
        time += 1
        if truck_bridge[0] - 1 == 0:
            com.append(bridge.pop(0))
            truck_bridge.pop(0)
        truck_bridge = [i - 1 for i in truck_bridge]
    return time + 1
solution(2,10,[7,4,5,6])
