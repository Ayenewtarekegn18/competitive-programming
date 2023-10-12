class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        int i=0,j=plants.size()-1,A=capacityA,B=capacityB,count=0;

        while(i<j) 
        {
                if (plants[i]>A)
                {
                    count++;
                    A=capacityA;
                } 
                if (plants[j]>B)
                {
                    count++;
                    B=capacityB;
                } 
                A-=plants[i];
                B-=plants[j];
                i++;
                j--; 
            }
        
            if (plants[i]> A && plants[j]> B  && i==j)
                { 
                    count++;
                    
                }
                    
         
        return count;
    }
};
