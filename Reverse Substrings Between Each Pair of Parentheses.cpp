class Solution {
public:
    string reverseParentheses(string s) {
        
        stack<string> st;
        st.push("");
        for(int i= 0;i<s.size();i++){
            string temp="";
            if(s[i]=='(')
                st.push("");
            else if(s[i]==')'){
                string first= st.top();
                reverse(first.begin(),first.end());
                st.pop();
                string second= st.top();
                st.pop();
                second +=first;
                st.push(second);
            }
            else{
                string first= st.top();
                first+=s[i];
                st.pop();
                st.push(first);
            }
            
        }
        string ans = st.top();
        
        return ans;
    }
};
