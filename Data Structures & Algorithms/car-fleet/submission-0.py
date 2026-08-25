class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleets=0
        last=0
        for pos,spd in cars:
            time=(target-pos)/spd

            if time>last:
                fleets+=1
                last=time
        return fleets
        