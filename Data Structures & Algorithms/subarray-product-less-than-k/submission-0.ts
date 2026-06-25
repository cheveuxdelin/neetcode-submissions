class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    numSubarrayProductLessThanK(nums: number[], k: number): number {
        let result = 0;
        let left = 0;
        let product = 1;
        for (let right = 0; right < nums.length; right++) {
            product *= nums[right];
            while (left <= right && product >= k) {
                product /= nums[left];
                left += 1;
            }
            result += right - left + 1;
        };
        return result;
    }
}
