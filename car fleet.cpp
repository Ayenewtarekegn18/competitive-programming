class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed)
    {
        vector<pair<int,float>> cars;
        for(int i=0;i<position.size();i++)
        {  
            float time;
            int dist=target-position[i];
            time=(float)dist/speed[i];
            cars.push_back(make_pair(position[i],time));
        }
        sort(cars.begin(),cars.end());
        reverse(cars.begin(),cars.end());
        stack<pair<int,float>> st;
        for(int i=0;i<cars.size();i++)
        {
            if(st.empty()){
                st.push(cars[i]);
            }
            else if(!st.empty())
            {   
                float topval=st.top().second;
                if(cars[i].second<=topval)
                {
    
                    continue;
                }
                else
                {
                    st.push(cars[i]);
                }
            }
        }
        return st.size();
    }
};
