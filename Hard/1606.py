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


