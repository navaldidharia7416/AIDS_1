
import sys
INT_MAX = sys.maxsize;
def minSteps(string, n, k):
    if (string[n - 1] == '0'):
        return -1;
    if (n == 1):
        return 0;

    if (n < 4):
        return 1;
    dp = [0] * n;

    dp[n - 1] = 0;
    dp[n - 2] = 1;
    dp[n - 3] = 1;
    for i in range(n - 4, -1, -1):
        if (string[i] == '0'):
            continue;
        steps = INT_MAX;
        if (i + k < n and string[i + k] == '1'):
            steps = min(steps, dp[i + k]);

        if (string[i + 1] == '1'):
            steps = min(steps, dp[i + 1]);

        if (string[i + 2] == '1'):
            steps = min(steps, dp[i + 2]);
        dp[i] = steps if (steps == INT_MAX) else (1 + steps);
    if (dp[0] == INT_MAX):
        return -1;
    return dp[0];
if "__name__" == "__main__":
    string = "101000011";
    n = len(string);
    k = 5;
    print(minSteps(string, n, k));
