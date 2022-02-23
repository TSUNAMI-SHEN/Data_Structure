class Solution:
    def isHappy(self, n: int) -> bool:
        def cal_happy(num):
            sum_ = 0
            while num:
                sum_ += (num % 10) * (num % 10)
                num = num // 10
            return sum_
        
        record = set()

        while True:
            n = cal_happy(n)

            if n == 1:
                return True
            
            if n in record:     # 当集合中出现重复元素，说明经过n次循环后有重复了，即不可能是快乐数
                return False
            
            record.add(n)
