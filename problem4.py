# Sum Pairs

# arr = [1, 2, 3, 4, 5]
# target = 5

def sumPairs(arr,target):
    res = []
    for i in range(len(arr)):
        for j in range(i , len(arr)):
            if arr[i]+arr[j] == target:
                if [arr[i],arr[j]] not in res:
                    res.append([arr[i],arr[j]])
    return res

def main()->None:
    l = []
    n = int(input('Enter length of the array: '))
    for i in range(n):
        val = int(input(f'Enter value {i}: '))
        l.append(val)
    t = int(input('Enter the target number: '))
    print(sumPairs(l,t)) 
    
if __name__ == '__main__':
    main()