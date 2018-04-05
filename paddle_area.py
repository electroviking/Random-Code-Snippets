def get_paddle_area(data):
    START = -1
    END = 0
    depth = {}

    lowest_point = 0

    for cur in range(1, len(data) - 1):
        prevItem = data[cur - 1]
        nextItem = data[cur + 1]
        current = data[cur]

        if prevItem > current > nextItem:
            START = prevItem

        if START != -1 and END == 0:
            print "prev ", prevItem
            print "curr ", current
            print "next ", nextItem

            h = max(prevItem, current, nextItem)
            depth[cur] = ([current, h])

            if lowest_point > current:
                lowest_point = current

            if nextItem >= START:
                END = h
    print lowest_point
    print depth



get_paddle_area([6, 2, 1, 3, 7, 4])
