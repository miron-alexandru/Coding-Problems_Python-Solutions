# problem link: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


# my solution:
def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort the leaderboard
    ranked_scores = sorted(set(ranked), reverse=True)
    i = len(ranked_scores)
    ranks = []

    for s in player:
        while i > 0 and s >= ranked_scores[i - 1]:
            # Decrement index for next iteration
            i -= 1
        ranks.append(i + 1)

    return ranks
