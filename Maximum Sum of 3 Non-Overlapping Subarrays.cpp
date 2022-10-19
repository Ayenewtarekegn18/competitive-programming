class Solution {
public:
     vector<int> maxSumOfThreeSubarrays(vector<int>& a, int k) {
        int n = a.size();
        vector<int> c[3], m(3); 
        vector<int> b(n);
        int sm = 0;
        for (int i = 0; i < n; ++i) {
            sm += a[i];
            if (i >=k-1) {
                b[i] = sm;
                sm -= a[i-k+1];
                if (i >= 3 * k-1) {
                    if (b[i-k-k] > m[0]) { 
                        m[0] = b[i-k-k];
                        c[0] = {i-k-k};
                    }
                    if (b[i-k] + m[0] > m[1]) { 
                        m[1] = b[i-k] + m[0];
                        c[1] = {c[0][0], i-k};
                    }
                    if (b[i] + m[1] > m[2]) { 
                        m[2] = m[1] + b[i];
                        c[2] = {c[1][0], c[1][1], i};
                    }
                }
            }
        }
        
        return {c[2][0]-k + 1,c[2][1]-k+1,c[2][2]-k+1};
     }
};
