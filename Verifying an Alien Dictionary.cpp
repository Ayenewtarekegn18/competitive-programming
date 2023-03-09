class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
       map <char,int> temp;
       int j;
        for(int i=0;i<order.size();i++)
        {
            temp[order[i]]=i;
        }

        for( int i=0;i<words.size()-1;i++)
        {
            j=0;
            while(j<words[i].size() && j<words[i+1].size())
            {
                if(temp[words[i][j]] < temp[words[i+1][j]]) 
                break;
                if(temp[words[i][j]] > temp[words[i+1][j]] )
                return false;

                j++;
            }

            if(j==words[i+1].size() && j<words[i].size()) 
            return false; 
        }        

        return true; 
    }   
};
