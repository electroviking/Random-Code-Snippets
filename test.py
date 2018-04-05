def find_mean(data):
    if len(data) % 2 != 0:
        print sorted(data)[((len(data) + 1) / 2) - 1]
    else:
        print len(data)/2
        print float(len(data)+1)/2




find_mean([1, 2, 2, 6, 7, 8])
