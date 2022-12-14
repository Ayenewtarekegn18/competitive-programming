class Solution {
public:
bool isValid(string s) {

    if(s.size() == 1)
        return false;
    
    stack<char> stack;
    
    int i=0;
    while(i < s.size()){
        if(s[i] == '(' || 
           s[i] == '{' ||
           s[i] == '['   ){
            
            stack.push(s[i]);
            i++;
        }
        else {
            
            if(s[i] == ')'){
                
                if(!stack.empty() && stack.top() == '('){
                    stack.pop();
                    i++;}
                
                else return false;
                
            }
            if(s[i] == ']'){
                
                if(!stack.empty() && stack.top() == '[' ){
                    stack.pop();
                    i++;}
                
                else return false;
                
            }  
            if(s[i] == '}'){
                
                if(!stack.empty() && stack.top() == '{'){
                    stack.pop();
                    i++;}
                
                else return false;
            }
        }
    }
    if(stack.empty())
        return true;
    else return false;
}
};
