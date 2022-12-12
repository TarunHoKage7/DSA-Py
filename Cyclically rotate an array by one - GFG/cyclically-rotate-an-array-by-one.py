#User function Template for python3

def rotate( arr, n):
    '''arr.insert(0, arr[-1])
    arr.pop(-1)'''
    
    
    '''temp = arr[0]
    for i in range(1, n):
        temp, arr[i] = arr[i], temp
    temp,arr[0] = arr[0],temp'''
    
    for i in range(n - 1, 0, -1):
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends