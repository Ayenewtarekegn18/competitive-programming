class Solution {
public:
    int maxArea(vector<int>& height) {
      
        int beg = 0, last = height.size()-1;
        
        int maxArea = 0;
        for (int i=0;i<height.size();i++)
    {
        if (beg < last)
        {
            maxArea = max(min(height[beg], height[last]) * (last-beg),
                          maxArea);
            
            if (height[beg] < height[last])
            {
                beg++;
            }
            else 
                last--;
        }
    }  
        return maxArea;
    };
    };
