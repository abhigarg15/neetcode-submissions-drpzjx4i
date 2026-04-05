class MinStack {

private:
    std::stack<long> minVal;
    std::stack<long> stack;
public:
    MinStack() {
    }
    
    void push(int val) {
        long longVal = static_cast<long>(val);
        if (stack.empty()){
            stack.push(longVal);
            minVal.push(longVal);
        }
        else{
            stack.push(longVal);
            long minv = std::min(minVal.top(), longVal);
            minVal.push(minv);
        }
    }
    
    void pop() {
        stack.pop();
        minVal.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return minVal.top();
    }
};
