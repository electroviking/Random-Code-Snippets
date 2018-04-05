
def sumBitDifferences(arr, n):
    ans = 0  # Initialize result

    # traverse over all bits
    for i in range(0, 32):

        # count number of elements with i'th bit set
        count = 0
        for j in range(0, n):
            # print arr[j] & 1 << i

            if ((arr[j] & (1 << i))):
                count += 1  # Add "count * (n - count) * 2" to the answer

        ans += (count * (n - count) * 2)

    return ans


# Driver prorgram
arr = [1, 3, 5]
n = len(arr)
print(sumBitDifferences(arr, n))

# This code is contributed by

