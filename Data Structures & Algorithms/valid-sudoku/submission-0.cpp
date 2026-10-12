class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i < 9; i++){
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++){
                if( board[i][j] == '.' ) continue;
                if( seen.count(board[i][j]) ) return false;
                seen.insert(board[i][j]);
            }
        }

        for(int i = 0; i < 9; i++){
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++){
                if( board[j][i] == '.' ) continue;
                if( seen.count(board[j][i]) ) return false;
                seen.insert(board[j][i]);
            }
        }

        for(int square = 0; square < 9; square++){
            
            unordered_set<char> seen;
            int indexForI = (square / 3) * 3;
            int indexForJ = (square * 3) % 9;

            for(int i = indexForI; i < indexForI + 3; i++){
                for(int j = indexForJ; j < indexForJ + 3; j++){
                    if( board[i][j] == '.' ) continue;
                    if( seen.count(board[i][j]) ) return false;
                    seen.insert(board[i][j]);
                }
            }
        }
        return true;
    }
};
