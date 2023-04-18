#include<bits/stdc++.h>

using namespace std;


#define ll long long int
#define ld long double
#define rep(i,n) for(ll i = 0; i < n; i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define vi vector<int>
#define vll vector<ll>
#define ff first
#define ss second
#define setbit(x) __builtin_popcountll(x)
#define b_ctz(x) __builtin_ctzll(x)
#define b_clz(x) __builtin_clzll(x)
#define iendl "\n", cout<<flush
#define nl '\n'


// order_of_key		   ---> number of elements less than
//~~~~~~~~~~~~~~~~~~

#ifndef ONLINE_JUDGE

#else
#define dbg(x)
#endif

//~~~~~~~~~~~~~~~~~~
//random generator
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
ll rnd(ll a, ll b) {if (a > b) {return -1;} return a + (ll)rng() % (b - a + 1);}


template<class T>
using minheap = priority_queue<T, vector<T>, greater<T> >;

// Input Operatirons Pair, Vector
template<class T, class V>istream& operator>>(istream &in, pair<T, V> &a) {in >> a.ff >> a.ss; return in;}
template<class T>istream& operator>>(istream &in, vector<T> &a) {for (auto &i : a) {in >> i;} return in;}

// Output Operations Pair Vector
template<class T, class V>ostream& operator<<(ostream &os, pair<T, V> &a) {os << a.ff << " " << a.ss; return os;}
template<class T>ostream& operator<<(ostream &os, vector<T> &a) {for (int i = 0 ; i < a.size() ; i++) {if (i != 0) {os << ' ';} os << a[i];} return os;}

//~~~~~~~~~~~~~~~~~~~

vector<ll> sieve(int n) {int*arr = new int[n + 1](); vector<ll> vect; for (int i = 2; i <= n; i++)if (arr[i] == 0) {vect.push_back(i); for (int j = 2 * i; j <= n; j += i)arr[j] = 1;} return vect;}
ll gcd(ll a, ll b) {if (b > a) {return gcd(b, a);} if (b == 0) {return a;} return gcd(b, a % b);}
ll modpow(ll x, ll n, ll m) { if (n == 0) return 1 % m; ll u = modpow(x, n / 2, m); u = (u * u) % m; if (n % 2 == 1) u = (u * x) % m; return u; } //x^n mod m
//~~~~~~~~~~~~~~~~~~~

const ll INF = 1e18;
const ll mod = 1000000007;
const int N = 200005;

void solve();

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	// freopen("err.txt", "w", stderr);
// #endif
	ll testcase = 1;
	ll no_testcase = 1;
	// cin >> testcase;
	while (no_testcase <= testcase) {
		// cout << "Case #" << no_testcase << ": ";
		solve();
		no_testcase++;
	}
	return 0;
}
/*
*/

void solve() {
	string s;
	cin >> s;
	char fir = s[0];
	s = s.substr(2, s.size());
	map<char, ll> mpp;
	if (s.back() > 'z' || s.back() < 'a') {
		cout << "Invalid" << nl;
		return;
	}
	rep(i, s.size()) {
		if (s[i] >= 'a' && s[i] <= 'z') mpp[s[i]]++;
	}
	for (auto it : mpp) {
		if (it.ss >= 2) {
			cout << "Invalid" << nl;
			return;
		}
	}
	for (ll i = 1; i < s.size(); i++) {
		if (s[i] <= 'z' && s[i] >= 'a') {
			if (s[i - 1] <= 'z' && s[i - 1] >= 'a') {
				cout << "Invalid" << nl;
				return;
			}
		}
		if (s[i] > 'z' || s[i] < 'a') {
			if (s[i - 1] > 'z' || s[i - 1] < 'a') {
				cout << "Invalid" << nl;
				return;
			}
		}
	}
	int op = 4;
	int cc = 0;
	while (s.size() > 1) {
		if (op == 4) {
			string temp;
			rep(i, s.size()) {
				if (s[i] == '/') {
					int a = -1, b = -1;
					a = s[i - 1] - '0';
					if (s[i - 1] < '0' || s[i - 1] > '4') {
						cout << "MOV R" << cc << ", " << s[i - 1] << nl;
						a = cc;
						cc++;
					}
					if (s[i + 1] < '0' || s[i + 1] > '4') {
						b = cc;
						cout << "MOV R" << cc << ", " << s[i + 1] << nl;
						cc++;
					}
					else b = s[i + 1] - '0';
					temp = s.substr(0, i - 1);
					temp.pb(a + '0');
					temp += s.substr(i + 2, s.size());
					cout << "DIV R" << a << ", R" << b << nl;
					s = temp;
					break;
				}
			}
			if (temp.size() == 0)
				op = 3;
		}
		else if (op == 3) {
			string temp;
			rep(i, s.size()) {
				if (s[i] == '*') {
					int a = -1, b = -1;
					a = s[i - 1] - '0';
					if (s[i - 1] < '0' || s[i - 1] > '4') {
						cout << "MOV R" << cc << ", " << s[i - 1] << nl;
						a = cc;
						cc++;
					}
					if (s[i + 1] < '0' || s[i + 1] > '4') {
						b = cc;
						cout << "MOV R" << cc << ", " << s[i + 1] << nl;
						cc++;
					}
					else b = s[i + 1] - '0';
					temp = s.substr(0, i - 1);
					temp.pb(a + '0');
					temp += s.substr(i + 2, s.size());
					cout << "MUL R" << a << ", R" << b << nl;
					s = temp;
					break;
				}
			}
			if (temp.size() == 0)
				op = 2;
		}
		else if (op == 2) {
			string temp;

			rep(i, s.size()) {
				if (s[i] == '+') {
					int a = -1, b = -1;
					a = s[i - 1] - '0';
					if (s[i - 1] < '0' || s[i - 1] > '4') {
						cout << "MOV R" << cc << ", " << s[i - 1] << nl;
						a = cc;
						cc++;
					}
					if (s[i + 1] < '0' || s[i + 1] > '4') {
						b = cc;
						cout << "MOV R" << cc << ", " << s[i + 1] << nl;
						cc++;
					}
					else b = s[i + 1] - '0';
					temp = s.substr(0, i - 1);
					temp.pb(a + '0');
					temp += s.substr(i + 2, s.size());
					cout << "ADD R" << a << ", R" << b << nl;
					s = temp;
					break;
				}
			}
			if (temp.size() == 0)
				op = 1;
		}
		else if (op == 1) {
			string temp;
			rep(i, s.size()) {
				if (s[i] == '-') {
					int a = -1, b = -1;
					a = s[i - 1] - '0';
					if (s[i - 1] < '0' || s[i - 1] > '4') {
						cout << "MOV R" << cc << ", " << s[i - 1] << nl;
						a = cc;
						cc++;
					}
					if (s[i + 1] < '0' || s[i + 1] > '4') {
						b = cc;
						cout << "MOV R" << cc << ", " << s[i + 1] << nl;
						cc++;
					}
					else b = s[i + 1] - '0';
					temp = s.substr(0, i - 1);
					temp.pb(a + '0');
					temp += s.substr(i + 2, s.size());
					cout << "SUB R" << a << ", R" << b << nl;
					s = temp;
					break;
				}
			}
			if (temp.size() == 0)
				op = 0;
		}
		else {
			break;
		}
	}
	cout << "MOV " << fir << ", R" << s[0] << nl;
}