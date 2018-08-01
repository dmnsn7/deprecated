// Copyright [2017] <dmnsn7@gmail.com>

#include <bits/stdc++.h>

using std::swap;

const int maxn = 0;

int r[maxn], wa[maxn], wb[maxn], wv[maxn], _ws[maxn], sa[maxn];
int _rank[maxn], height[maxn];

inline bool cmp(int *r, int a, int b, int l) {
  return r[a] == r[b] && r[a + l] == r[b + l];
}

void da(int n, int m) {
  int i, j, p, *x = wa, *y = wb;

  for (i = 0; i < m; i++) {
    _ws[i] = 0;
  }

  for (i = 0; i < n; i++) {
    _ws[x[i] = r[i]]++;
  }

  for (i = 1; i < m; i++) {
    _ws[i] += _ws[i - 1];
  }

  for (i = n - 1; i >= 0; i--) {
    sa[--_ws[x[i]]] = i;
  }

  for (j = 1, p = 1; p < n; j <<= 1, m = p) {
    for (p = 0, i = n - j; i < n; i++) {
      y[p++] = i;
    }

    for (i = 0; i < n; i++)
      if (sa[i] >= j) {
        y[p++] = sa[i] - j;
      }

    for (i = 0; i < n; i++) {
      wv[i] = x[y[i]];
    }

    for (i = 0; i < m; i++) {
      _ws[i] = 0;
    }

    for (i = 0; i < n; i++) {
      _ws[wv[i]]++;
    }

    for (i = 1; i < m; i++) {
      _ws[i] += _ws[i - 1];
    }

    for (i = n - 1; i >= 0; i--) {
      sa[--_ws[wv[i]]] = y[i];
    }

    swap(x, y);

    for (p = 1, x[sa[0]] = 0, i = 1; i < n; i++) {
      x[sa[i]] = cmp(y, sa[i - 1], sa[i], j) ? p - 1 : p++;
    }
  }

  return;
}

void calheitght(int n) {
  int i, j, k = 0;

  for (i = 1; i < n; i++) {
    _rank[sa[i]] = i;
  }

  // print(_rank, n);
  for (i = 0; i < n; height[_rank[i++]] = k)
    for (k ? k-- : 0, j = sa[_rank[i] - 1]; r[i + k] == r[j + k]; k++) {
    }

  return;
}

int main() { return 0; }
