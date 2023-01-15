class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int>v;
        
        for(int i=0;i<nums1.size();i++){
            
            int j=0;
            
            for(j=0;j<nums2.size();j++){
                
                if(nums2[j]==nums1[i]){
                    
                    break;   
                }
                
            }
            
            int len=v.size();
            
            for(int k=j+1;k<nums2.size();k++){
                
                    if(nums2[j]<nums2[k]){
                        
                        v.push_back(nums2[k]);
                        
                        break;
                    }
                   
                }
            
                if(len==v.size()) v.push_back(-1);
        }
  return v;  }
        
        
        };
