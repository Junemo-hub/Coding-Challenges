def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


# return에 print를 해야하는걸 헷갈렸음
# range 안에 숫자가 여러개 들어가는 게 헷갈림.
