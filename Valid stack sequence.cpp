class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> order ;   
        int x = 0;
        for(int i= 0; i<pushed.size(); i++)
        {
            order.push(pushed[i]);
            
			for(int i= 0; i<pushed.size(); i++)       
            while(!order.empty() && order.top() == popped[x])
            {
                order.pop();
                ++x;
            }
        }
		
        return order.empty();
    }
};
