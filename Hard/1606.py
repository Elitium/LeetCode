# Naive approach

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        server_dict_handled = {x: 0 for x in range(k)}
        server_dict_ftime = {x: 0 for x in range(k)}
        res = []
        maxi = 0

        if len(arrival) == 1:
            return [0]

        for i in range(len(arrival)):
            for j in range(len(arrival) - 1):
                n = (i+j) % k
                if server_dict_ftime[n] <= arrival[i]:
                    #print(f"Task {i} taken by server {n}")
                    server_dict_handled[n] += 1
                    maxi = max(maxi, server_dict_handled[n])
                    server_dict_ftime[n] = arrival[i] + load[i]
                    break
                #print(f"dropped by {n}, finish time {server_dict_ftime[n]} vs arrival {arrival[i]}")
        
        res = []
        for key, item in server_dict_handled.items():
            if item == maxi:
                res.append(key)

        return res

# More intelligent version with O(nk) time complexity (k being max length of available servers - pop takes O(k)

import heapq
from bisect import bisect_left, insort

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        server_handled = [0] * k
        busy = []
        server_available = [x for x in range(k)]
        maxi = 0

        # maintain min heap to track finishing servers
        # ordered list to binary search for index of available server

        if len(arrival) == 1:
            return [0]

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                finish_time, server_id = heapq.heappop(busy)
                insort(server_available, server_id)

            if server_available:
                idx = bisect_left(server_available, i % k)

                if idx == len(server_available):
                    idx = 0

                server = server_available.pop(idx)
                server_handled[server] += 1
                maxi = max(server_handled[server], maxi)
                heapq.heappush(busy, (arrival[i] + load[i], server))
             
        res = []
        for i in range(k):
            if server_handled[i] == maxi:
                res.append(i)

        return res


# genius version, store heap but manipulate index s.t. best choice available server for next i is at top of heap

import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        handled = [0] * k
        available = list(range(k))
        busy = []
        maxi = 0

        push = heapq.heappush
        pop = heapq.heappop

        for i, start in enumerate(arrival):

            # Release finished servers
            while busy and busy[0][0] <= start:
                _, server = pop(busy)
                push(available, i + (server - i) % k)

            if not available:
                continue

            # Assign request
            server = pop(available) % k
            handled[server] += 1

            if handled[server] > maxi:
                maxi = handled[server]

            push(busy, (start + load[i], server))

        return [i for i, count in enumerate(handled) if count == maxi]
