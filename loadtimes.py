def loadTimeEstimator(sizes, uploadingStart, V):
    if not sizes:
        return sizes
    rest = sizes[:]
    size_range = range(len(rest))
    n_files = len(rest)
    result = uploadingStart[:]
    time = min(uploadingStart)
    zipped = list(zip(rest, uploadingStart))
    list_uploading, current_uploading = count_uploading(zipped, time)
    passed = current_uploading
    while current_uploading > 0:
        current_speed = V/ current_uploading
        if passed >= n_files:
                
                result[item] += math.ceil(zipped[item][0]/current_speed)

            next_start_time = uploadingStart[passed]
        print(next_start_time)
        total = current_speed * (next_start_time - time)

        time = next_start_time
        for item in list_uploading:
            zipped[item] = zipped[item][0] - total, zipped[item][1]
            print(zipped[item])
            if zipped[item][0] <= 0:
                result[item] = time
    
        list_uploading, current_uploading = count_uploading(zipped, time)
    
    return result
        

def count_uploading(zipped, time):
    total = []
    i = 0
    for x, y in zipped:
        if x > 0 and time >= y:
            total.append(i)
        i += 1
    # print(total)
    return total, len(total)

# print(loadTimeEstimator(list(range(1000)), [1 for x in range(1000)], 1000))
print(loadTimeEstimator([10, 20], [1, 2], 2))