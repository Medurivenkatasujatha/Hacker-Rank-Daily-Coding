```
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    i = len(arr) - 1
    while i > 0:
        if arr[i] == arr[i-1]:
            pass
        else:
            print (arr[i-1])
            break
        i -= 1
```
