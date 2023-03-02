class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> temp;
        int n=arr.size();
        for(int i=0;i<arr.size();i++){
            if (arr[i]==0)
            {
            temp.push_back(arr[i]);
            temp.push_back(0);
            arr.pop_back();
            }
            else
            temp.push_back(arr[i]);

        }
        while(temp.size()>n)
        temp.pop_back();

        arr=temp;
           }
}
