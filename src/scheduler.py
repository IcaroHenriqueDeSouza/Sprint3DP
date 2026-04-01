import bisect

def max_appointments(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    starts = [i[0] for i in intervals]

    memo = {}

    def dp(index):
        if index >= len(intervals):
            return 0

        if index in memo:
            return memo[index]

        # pular
        skip = dp(index + 1)

        # pegar
        end_time = intervals[index][1]
        next_index = bisect.bisect_left(starts, end_time)

        take = 1 + dp(next_index)

        memo[index] = max(skip, take)
        return memo[index]

    return dp(0)