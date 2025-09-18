def minimumAbsoluteDifference(arr):
    arr.sort()
    minimumtemp = float('inf')
    for i in range(len(arr) - 1) :
        minimumtemp = min(minimumtemp, abs(arr[i]-arr[i+1]))
    return minimumtemp
        



# float랑
# arr.sort 부분 헷갈림
# for 안에 넣는거 항상 더 익숙해져야됨