// Last updated: 7/14/2026, 2:16:56 PM
class Solution {
    static final int MOD = 1000000007;

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;

        long[] up = new long[m];
        long[] down = new long[m];

        for (int i = 0; i < m; i++) {
            up[i] = i;
            down[i] = (m - 1 - i);
        }

        for (int len = 2; len < n; len++) {

            long[] newUp = new long[m];
            long[] newDown = new long[m];

            long[] prefixUp = new long[m + 1];
            long[] prefixDown = new long[m + 1];

            for (int i = 0; i < m; i++) {
                prefixUp[i + 1] = (prefixUp[i] + up[i]) % MOD;
                prefixDown[i + 1] = (prefixDown[i] + down[i]) % MOD;
            }

            for (int cur = 0; cur < m; cur++) {

                newUp[cur] = prefixDown[cur];

                newDown[cur] =
                        (prefixUp[m] - prefixUp[cur + 1] + MOD) % MOD;
            }

            up = newUp;
            down = newDown;
        }

        long ans = 0;

        for (int i = 0; i < m; i++) {
            ans = (ans + up[i]) % MOD;
            ans = (ans + down[i]) % MOD;
        }

        return (int) ans;
    }
}