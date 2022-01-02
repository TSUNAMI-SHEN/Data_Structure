//用两个栈实现队列，栈：先进后出；队列：先进先出
//stack_in：元素先进入stack_in栈中，判断stack_out是否为空，若为空，则删除时先将stack_in内的元素出栈并压入stack_out中，完成顺序颠倒，若stack_out不为空，即将栈顶元素pop
class CQueue {
    stack<int> stack_in, stack_out;
public:
    CQueue() {
        while(!stack_in.empty()){
            stack_in.pop();
        }
        while(!stack_out.empty()){
            stack_out.pop();
        }
    }
    
    void appendTail(int value) {
        stack_in.push(value);
    }
    
    int deleteHead() {
        if(stack_out.empty()){
            while(!stack_in.empty())
            {
                stack_out.push(stack_in.top());
                stack_in.pop();
            }
        }
        if(stack_out.empty()){
            return -1;
        }
        else {
            int deleteItem = stack_out.top();
            stack_out.pop();
            return deleteItem;
        }
    }
};
