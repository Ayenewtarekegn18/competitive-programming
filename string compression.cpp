class Solution {
public:
    int compress(vector<char>& chars) 
    {
        vector <char> vec ;
        long long ans=0;
            for (int i=0;i<chars.size();i++)
            {
                vec.push_back(chars[i]);
                int j=i;
            while (j<chars.size()&&chars[i]==chars[j])
            {
                 j++;
            }
            if (j-i>=10)
            {
                int n=j-i;
              string f= to_string(n);
                 for (int i=0;i<f.size();i++)
                {
                    vec.push_back(f[i]);
                    ans++;
                 }
                 ans++;

            }
        else if (j-i==1)
        {
        ans++;
        }
        else
        {
        ans+=2;
        vec.push_back((j-i)+'0');
        }

        i=j-1;
    }
        chars=vec;
      return ans;
    }
};
