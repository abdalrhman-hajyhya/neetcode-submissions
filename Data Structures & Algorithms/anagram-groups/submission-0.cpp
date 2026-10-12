#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

struct VectorHash {
    size_t operator()(const vector<int>& vec) const {
        size_t hash = 0;
        for (int num : vec) {
            hash ^= hash * 31 + std::hash<int>{}(num);
        }
        return hash;
    }
};

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<vector<int>, vector<string>, VectorHash> auxMap;

        for (const string& word : strs) {
            vector<int> freq(26, 0);
            for (char c : word) freq[c - 'a']++;
            auxMap[freq].push_back(word);
        }

        vector<vector<string>> ans;
        for (auto& pair : auxMap) {
            ans.push_back(move(pair.second));
        }
        return ans;
    }
};


