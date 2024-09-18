#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*int main()
{
  int N, M, K;

  cin >> N >> M >> K;
  vector<int> arr;
  for(int i = 0; i < N; i++){
    int num;
    cin >> num;
    arr.push_back(num);
  }

  sort(arr.begin(), arr.end(), greater<int>());

  int ans = 0;
  int a = M / (K + 1);
  ans += (arr[0] * K + arr[1]) * a + arr[0] * (M % (K + 1));

  printf("%d\n", ans);
}*/