//求1+2+...+n
//使用逻辑运算中的短路效应来产生递归的终止条件
class Solution {
public:
    int sumNums(int n) {
        n > 1 && (n += sumNums(n-1));   # 只有两个同时成立才会执行
        return n;
    }
};
