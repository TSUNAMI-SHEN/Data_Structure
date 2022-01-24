//数据流中的中位数
//建立小顶堆（保存较大的一半元素）A & 大顶堆（保存较小的一半元素）B，中位数即可以从A的堆顶元素获得
class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<int, vector<int>, greater<int>> A;
    priority_queue<int, vector<int>, less<int>> B;
    MedianFinder() {

    }
    
    void addNum(int num) {
        if (A.size() != B.size()){
            A.push(num);
            B.push(A.top());
            A.pop();
        }
        else {
            B.push(num);
            A.push(B.top());
            B.pop();
        }
    }
    
    double findMedian() {
        return A.size() != B.size() ? A.top() : (A.top() + B.top()) / 2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
