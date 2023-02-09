class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int first = 0;
        int last = 0; 
        int max_len = 0;
        unordered_set<char> char_set;

    while (last < s.length())
     {
        if (char_set.find(s[last]) == char_set.end())
         {
            char_set.insert(s[last]);
            last++;
            max_len = max(max_len, last - first);
        } 
        else {
            char_set.erase(s[first]);
            first++;
        }
    }

    return max_len;
    }
};
