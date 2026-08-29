class TimeMap:
    

    def __init__(self):
        self.mp={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key]=[]
        self.mp[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        
        arr=self.mp[key]

        l=0
        r=len(arr)-1
        ans=""

        while l<=r:
            mid=(l+r)//2

            if arr[mid][1]<=timestamp:
                ans=arr[mid][0]

                l=mid+1
            else:
                r=mid-1
        return ans
        
