//实现在栈中找到最小元素的min函数
//借助辅助栈，用来存储最小值
class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> A, B;
    MinStack() {

    }
    
    //push，栈A正常插入元素，B中若为空或者新插入元素小于B的top元素，则插入B中
    void push(int x) {
        A.push(x);
        if(B.empty() || B.top() >= x){
            B.push(x);
        }
    }
  
    //pop，A中的栈顶元素出栈，若出栈元素与B的栈顶元素相等，则B中的栈顶元素也出栈，保持元素相同
    void pop() {
        if(A.top()==B.top()){
            B.pop();
        }
        A.pop();
    }
    
    //取A的栈顶元素
    int top() {
        return A.top();
    }
    
    //取B的栈顶元素
    int min() {
        return B.top();
    }
};
