#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;

int main() {
  
  int n;
  cin >> n;

  for (int i = 1; i <= n; i ++) {
    int count = 0;
    stringstream ss;

    for (int j = 1; j <= n; j++) {
      int v;
      cin >> v;
      if (v == 1) {
        count++;
        ss << ' ' << j;
      }
    }
    cout << count << ss.str() << '\n';
  }

  return 0;
}
