// solution.h
class Solution {
public:
    vector<int> whereToStop;

    std::string encode(std::vector<std::string>& strs) {
        string res;
        int currentPos = 0;

        for (const auto& str : strs) {
            res += str;
            currentPos += str.size();
            whereToStop.push_back(currentPos);
        }

        return res;
    }

    vector<std::string> decode(const std::string& s) {
        vector<std::string> res;
        int start = 0;

        for (int stop : whereToStop) {
            res.push_back(s.substr(start, stop - start));
            start = stop;
        }

        return res;
    }
};
