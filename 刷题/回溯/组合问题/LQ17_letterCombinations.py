class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.answer: str = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits:
            return []
        self.backtracking(digits, 0)
        return self.answers
    

    # 确定回溯的参数
    # 1.digits-题目给的字符串；2.index-记录遍历第几个数字&树的深度
    def backtracking(self, digits: str, index: int) -> None:
        # 2.确定终止条件，当遍历的数字等于长度结束
        if index == len(digits):
            self.answers.append(self.answer)
            return
        
        # 3.处理单层逻辑
        letters: str =  self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter   # 处理
            self.backtracking(digits, index+1)  # 递归到下一层
            self.answer = self.answer[:-1]  # 回溯
        
    
