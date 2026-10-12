// solution.h
class Solution {
public:
    vector<int> whereToStop;

    string encode(vector<string>& strs) {
        string ans;
        int prv = 0;
        for(string str: strs){
            ans += str;
            prv += str.size();
            whereToStop.push_back(prv);
        }
        return ans;
    }

    vector<string> decode(const string& s) {
        vector<string> res;
        int start = 0;
        for(int stop: whereToStop){
            string auxS;
            for(int i = start; i < stop; i++){
                auxS += s[i];
            }
            res.push_back(auxS);
            start = stop;
        }
        return res;
    }
};
