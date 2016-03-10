# def lightBulbs(lights, n):
#     for :
#         j = -1
#         l = lights[:]
#         for bulb in l:
#             if l[j]:
#                 lights[j+1] = int(not bulb)
#             j += 1
#         print(lights)
#     return lights


def lightBulbs(l, n):
    while n:
        l = [x ^ l[i-1] for i, x in enumerate(l)]
        n -= 1
    return l

print(lightBulbs([0, 1, 1, 0, 1], 2))
