class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> z;
for (int i=1;i<=n;i++){
    if (i%3==0){
        if (i%5==0)
            z.push_back("FizzBuzz");
        else
            z.push_back("Fizz");
    }
    else if (i%5==0)
        z.push_back("Buzz");
    else 

        z.push_back(to_string(i));
    }
    return z;
    }
    
};
