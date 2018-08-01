// Copyright [2017] <dmnsn7@gmail.com>

#include <bits/stdc++.h>

const int N = 10000;

struct triple {
  int a, b, c;
  triple() {}
  triple(int _a, int _b, int _c) {
    a = _a;
    b = _b;
    c = _c;
  }

  bool operator<(const triple to) const {
    if (a != to.a) {
      return a < to.a;
    } else if (b != to.b) {
      return b < to.b;
    }
    return c < to.c;
  }
};

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

bool is_square(int n) {
  int r = std::sqrt(n + 0.5);
  return r * r == n;
}

int main() {
  int cnt = 0;

  for (int i = 1; i <= N; i++) {
    if (is_square(i)) {
      continue;
    }
    std::map<triple, int> visit;
    int r = sqrt(i + 0.5);
    triple tp(1, r, i - r * r);
    while (visit.find(tp) == visit.end()) {
      visit[tp] = visit.size();
      tp.b -= static_cast<int>((tp.a * sqrt(i) + tp.b) / tp.c) * tp.c;
      tp = triple(tp.a * tp.c, -tp.b * tp.c, tp.a * tp.a * i - tp.b * tp.b);
      int g = gcd(gcd(tp.a, tp.b), tp.c) * (tp.a < 0 ? -1 : 1);
      tp = triple(tp.a / g, tp.b / g, tp.c / g);
    }
    cnt += (visit.size() - visit[tp] + 1) % 2;
  }

  printf("%d\n", cnt);

  return 0;
}
