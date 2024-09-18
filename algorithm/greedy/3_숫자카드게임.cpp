#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

/*int main()
{
  int N, M;
  cin >> N >> M;

  vector <vector<int>> v(M, vector<int>(N, 0)); // M개의 행, N개의 열로 된 2차원
vector 배열 생성하며 0으로 초기화 for(int i = 0; i < N; i++){ for(int j = 0; j <
M; j++){ cin >> v[i][j];
    }
  }
  vector<int> min;
  for (int i = 0; i < N; i++){
    min.push_back(*min_element(v[i].begin(), v[i].end()));
  }
  int max;
  for (int i = 0; i < N; i++){
    max = *max_element(min.begin(), min.end());
  }
  cout << max;
}*/