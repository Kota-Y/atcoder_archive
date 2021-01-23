#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> vec(n);
  for (int i = 0; i < n; i++) {
    cin >> vec.at(i);
  }
  
  int max_count = 0;
  
  for (int i = 0; i < n; i++) {
  	int x = vec[i];
    int tmp = 0;
    for (int j = 0; j < n; j++) {
    	tmp++;
      	if (vec[j] < x) {
         	tmp = 0;
        }
     	max_count = max(max_count, tmp * x);
    }
  }
  
  cout << max_count << endl;  
}