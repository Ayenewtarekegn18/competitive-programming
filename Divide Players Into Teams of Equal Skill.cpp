class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
    sort(skill.begin(),skill.end());
    int i=0;
    int j=skill.size()-1;
    int ans=skill[i] + skill[j];
    long long chemistry= skill[i] * skill[j];
    i=1;
    j-=1;
    while(i<j){
     
        if (skill[i] + skill[j]!=ans)
          return -1;
        else
          chemistry=chemistry+(skill[i] * skill[j]); 
    i++;
    j--;
    }
        
    return chemistry;
   }
    
};
