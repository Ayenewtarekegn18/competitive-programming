class MyQueue
{
  public:
stack <int> first ;
stack<int> last;
MyQueue() {
;
}

void push(int x) {
    first.push(x);
}

int pop() {
    if(first.empty() and last.empty())
        return -1;
    if(last.empty())
    {
        while(!first.empty())
        {
            int x=first.top();
            first.pop();
            last.push(x);
        }
    }
    int y=last.top();
    last.pop();
    return y;
}

int peek() {
    if(last.empty())
    {
        while(!first.empty())
        {
     last.push(first.top());
            first.pop();
        }
    }
        return last.top();
    
}

bool empty() {
    if(first.empty() && last.empty())
        return true;
    else
    return false;
}
};
