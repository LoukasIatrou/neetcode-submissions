class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# How do we calculate the median?? We take the middle value of a sorted array. Problem in our case, the 2 arrays sorted 
# but they arent increasing from one array to the other. So we simpy cant just set them as a single array and return the
# middle value. Brute Force, Merge the 2 arrays, by potentially using merge sort, and return the middle value. 
# this leads to O((m+n)(log(m+n))     
        arrA = nums1 if len(nums1)<len(nums2) else nums2 
        arrB = nums2 if len(nums1)<len(nums2) else nums1 
        print(arrA,arrB)
        half = (len(nums1)+len(nums2))//2
        l,r = 0 , len(arrA)
        while l<=r:
            mid = (l+r)//2
            remainder = half - mid
            Aleft = arrA[mid-1] if mid > 0 else float("-inf")
            Aright = arrA[mid] if mid  < len(arrA) else float("inf")
            Bleft = arrB[remainder-1] if remainder > 0 else float("-inf")
            Bright = arrB[remainder] if remainder < len(arrB) else float("inf")            
            if Aleft>Bright:
                r = mid - 1
                print(r,Aleft,Bright)
            elif Bleft>Aright:
                l = mid + 1
                print(l,Aright,Bleft)
            else:
                if (len(nums1)+len(nums2))%2 == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2    
                else:
                    return min(Aright,Bright)