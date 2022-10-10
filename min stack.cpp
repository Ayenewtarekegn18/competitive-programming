class MinStack {

private:
    stack<int>first;
    stack<int>last;
public:

MinStack() {
    
}

void push(int val) {
    
    if(first.empty())
    {
        last.push(val);
        first.push(val);
        
        return ;
    }
        
    
       first.push(val);
    
    if(last.top() >= first.top())
        last.push(val);
    
}

void pop() {
    
    if(last.top() == first.top())
        last.pop();
    
       first.pop();
}

int top() {
    
    return first.top();
}

int getMin() {
    
    return last.top();
}
};
