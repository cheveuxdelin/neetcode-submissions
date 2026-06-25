class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True

        for i in range(len(flowerbed)):
            left_is_ok = i == 0 or not flowerbed[i-1]
            right_is_ok = i == len(flowerbed)-1 or not flowerbed[i+1]
            if not flowerbed[i] and left_is_ok and right_is_ok:
                flowerbed[i] = 1
                n -= 1
                if not n:
                    return True
        return False