class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        #for k in range(n):
        #    for i in range(1,n):
        #      if arr[i]<arr[i-1]:
        #            arr[i],arr[i-1] = arr[i-1],arr[i]
        arr.sort()
        for i in range(1,n):
              if arr[i] - arr[i-1] !=arr[1]-arr[0]:
                return False
        return True
        