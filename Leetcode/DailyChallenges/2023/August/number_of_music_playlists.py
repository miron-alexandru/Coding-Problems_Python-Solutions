# problem link: https://leetcode.com/problems/number-of-music-playlists


# my solution:

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        # Initialize a 2D array dp to store the number of playlists
        # dp[i][j] represents the number of playlists of length i with j different songs
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        # Base case: There is one way to have an empty playlist with no different songs.
        dp[0][0] = 1

        # Iterate over the playlist length from 1 to goal
        for i in range(1, goal + 1):
            # Iterate over the number of different songs from 1 to n
            for j in range(1, n + 1):
                # Calculate the number of playlists for the current length and number of different songs
                # use the recurrence relation: dp(i, j) = dp(i-1, j-1) * (n-j+1) + dp(i-1, j) * max(j-k, 0)
                dp[i][j] = (dp[i-1][j-1] * (n-j+1) + dp[i-1][j] * max(j-k, 0)) % MOD

        # The final answer is stored in dp[goal][n] representing the number of playlists
        # of length 'goal' with 'n' different songs.
        return dp[goal][n]
