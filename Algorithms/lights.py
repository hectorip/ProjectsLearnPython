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


def rlightBulbs(l, n):
    while n:
        for i, b in enumerate(l[:]):
            l[i + 1] = b ^ l[i+1]
        n -= 1
        print(l)
    return l

print(rlightBulbs([0, 1, 1, 0, 1], 2))
