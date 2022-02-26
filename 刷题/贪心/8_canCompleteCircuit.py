class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 确保能跑完的情况下，各个站点的剩油量一定是大于等于0的
        # 局部最优：当前累加rest[j]的curSum一旦小于0，说明起始位置为j开始是不行的（因为每到一个加油站其油量要大于0），所以起始位置推到j+1
        # 全局最优：找到可以跑一圈的起始位置
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start
