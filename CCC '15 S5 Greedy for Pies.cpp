#include <bits/stdc++.h>
using namespace std;
int N, M;
int npie[3001], mpie[101];
int memo[3001][2][101][101];

int get_pies(int pos, bool can_take, int left, int right){

    if (memo[pos][can_take][left][right] != -1){
        return memo[pos][can_take][left][right];
    }

    if (pos == N){
        if (left <= right){

            if (can_take){
                memo[pos][can_take][left][right] = mpie[right] + get_pies(pos, false, left, right-1);
                return memo[pos][can_take][left][right];
            }
            memo[pos][can_take][left][right] = get_pies(pos, true, left+1, right);
            return memo[pos][can_take][left][right];
        }
        return 0;
    }

    int without_M;
    int with_M = 0;
    if (can_take){
        without_M = max(npie[pos] + get_pies(pos+1, false, left, right), get_pies(pos+1, true, left, right));
        if (left <= right){
            with_M = get_pies(pos, false, left, right-1) + mpie[right];
        }
        memo[pos][can_take][left][right] = max(with_M, without_M);
        return memo[pos][can_take][left][right];
    }
    else{
        if (left <= right){
           with_M = get_pies(pos, true, left+1, right); 
        }
        memo[pos][can_take][left][right] = max(with_M, get_pies(pos+1, true, left, right));
        return memo[pos][can_take][left][right];
    }
}

int main(){
    memset(memo, -1, sizeof memo);

    scanf("%d", &N);
    for (int i=0; i < N; i++){
        scanf("%d", &npie[i]);
    }
    scanf("%d", &M);
    for (int i=0; i < M; i++){
        scanf("%d", &mpie[i]);
    }
    sort(mpie, mpie + M);
    printf("%d\n", get_pies(0, true, 0, M-1));
    return 0;

}