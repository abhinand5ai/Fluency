import itertools
from collections import deque


def findMaximumSustainableClusterSize(processing_power, booting_power, power_max):
    c_power = list(itertools.accumulate(processing_power))
    q = deque()
    start, end = 0, 0
    n = len(processing_power)
    mx_len = 0
    total_processing_power = 0
    while end < n:
        total_processing_power += processing_power[end]
        while q and booting_power[q[-1]] < booting_power[end]:
            q.pop()
        q.append(end)
        end += 1

        while q and get_net(start, end, c_power, booting_power[q[0]]) > power_max:
            if q[0] == start:
                q.popleft()
            start += 1

        mx_len = max(end - start, mx_len)

    return mx_len


def get_net(start, end, c_power, max_booting):
    total_processing_power = c_power[end - 1] - (c_power[start - 1] if start > 0 else 0)
    k = end - start
    net = max_booting + total_processing_power * k
    print(start, end, net)
    return net


if __name__ == '__main__':
    cluster_size = findMaximumSustainableClusterSize([2, 1, 3, 4, 5], [3, 6, 1, 3, 4], 25)
    # cluster_size = findMaximumSustainableClusterSize([4, 1, 4, 5, 3], [8, 8, 10, 9, 12], 33)
    print(cluster_size)
