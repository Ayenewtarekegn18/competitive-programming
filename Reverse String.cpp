class Solution {
public:
    void reverseString(vector<char>& s) {
        int l=0;
        int r=s.size()-1;
        char temp;
        while (l<=r){
            temp=s.at(l);
            s.at(l)=s.at(r);
            s.at(r)=temp;
            l++;
            r--;
        }
    }
};
