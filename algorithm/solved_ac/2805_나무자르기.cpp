#include <algorithm>
#include <cmath> // abs 함수를 사용하기 위해 추가
#include <iostream>
#include <vector>

using namespace std;

int main() {
  long N, target;
  cin >> N >> target;

  vector<long> v(N);
  for (long i = 0; i < N; i++) {
    cin >> v[i];
  }
  sort(v.begin(), v.end());

  long left = 0; // 최소값을 0으로 초기화
  long right = v[N - 1];
  long closest = 0; // 처음에 closest를 0으로 초기화
  long mid;

  // 이진 탐색 시작
  while (left <= right) {
    mid = left + (right - left) / 2; // 나무의 길이 평균값
    long sum = 0;

    // 나무의 길이 조정에 따른 총 합계 계산
    for (long i = 0; i < N; i++) {
      sum += max(v[i] - mid, 0L); // max의 두 번째 인수를 long으로 설정
    }

    // 목표값과의 차이 비교
    if (abs(sum - target) < abs(closest - target)) {
      closest = sum; // 가장 가까운 합계 업데이트
    }

    // 목표값과 같은 경우
    if (sum == target) {
      break;
    } else if (sum < target) {
      right = mid - 1; // 더 높은 길이 탐색
    } else {
      left = mid + 1; // 더 낮은 길이 탐색
    }
  }

  // 만약 closest가 target보다 작으면 mid를 조정
  if (closest < target) {
    mid -= 1;
  }

  cout << mid << endl; // 결과 출력

  return 0;
}
