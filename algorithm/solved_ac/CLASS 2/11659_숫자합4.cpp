#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int exec_11659()
{
  int N, M;

  cin >> N >> M;
  vector<int> nums(N + 1);
  vector<int> ans(M);

  for(int i = 1; i < N + 1; i++){ // 수열 입력받기
    cin >> nums[i];
  }

  for(int i = 1; i < N + 1; i++){
    nums[i] = nums[i] + nums[i - 1];
  }
  
  int start, end;
  for (int i = 0; i < M; i++){
    cin >> start >> end;
    ans[i] = nums[end] - nums[start - 1];
  }

  for (int i = 0; i < M; i++){
    cout << ans[i] << '\n';  
  }
  
  return 0;
}