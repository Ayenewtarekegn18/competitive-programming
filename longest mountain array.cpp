class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int Mount = 0,n = arr.size(),i= 1, x = 0,y = 0;
        while (i< n)
        {
            while(i < n && arr[i - 1] == arr[i])
                ++i;
                 x = 0;
            while(i< n && arr[i - 1] < arr[i])
                ++x,++i;
                 y= 0;
            while(i < n && arr[i- 1] > arr[i])
                ++y,++i;
            if(x && y)  
                Mount = max(Mount, x + y + 1);
        }
        return Mount;
    }
};
