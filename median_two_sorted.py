# observation: to find the median of two sorted lists of length (2+3) = 5 can be compressed to finding 3 using
# max of the two mins and min of two maxs and the median
# to find the median of (2+2) = 4 elements can be directly found using max of two mins and min of two maxs

# Note: used floor division // instead of float division / in python 3.X

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        # 0: no elements in nums1
        if len(nums1) == 0:
            l = len(nums2)
            if l % 2 != 0:
                return nums2[(l - 1) // 2]
            else:
                return nums2[l // 2 - 1] * 0.5 + nums2[l // 2] * 0.5

        elif len(nums1) == 1:
            l = len(nums2)
            # 1
            if l == 1:
                return nums1[0] * 0.5 + nums2[0] * 0.5
            # 2
            elif l % 2 != 0:
                # M = l-1. Take median of B[ M // 2 – 1 ], B[ M // 2 + 1], A[ 0 ] and take its average with B[ M // 2 ]
                candidate_sort = sorted([nums2[(l - 1) // 2 - 1], nums2[(l - 1) // 2 + 1], nums1[0]])
                return candidate_sort[1] * 0.5 + nums2[(l - 1) // 2] * 0.5
            # 3 len(nums2) % 2 == 0
            else:
                # find the median of three elements B[ M // 2 – 1 ], B[ M // 2] and A[ 0 ].
                candidate_sort = sorted([nums2[l // 2 - 1], nums2[l // 2], nums1[0]])
                return candidate_sort[1]
        elif len(nums1) == 2:
            l = len(nums2)
            # 4
            if l == 2:
                return max(nums1[0], nums2[0]) * 0.5 + min(nums1[1], nums2[1]) * 0.5
            # 5
            elif l % 2 != 0:
                # M = l -1. Return the median of B[M//2], max(A[0], B[M//2 – 1]), min(A[1], B[M//2 + 1]).
                candidate_sort = sorted([max(nums1[0], nums2[(l - 1) // 2 - 1]),
                                         min(nums1[1], nums2[(l - 1) // 2 + 1]), nums2[(l - 1) // 2]])
                return candidate_sort[1]
            # 6
            else:
                #  median of following four elements: B[l//2], B[l//2 – 1], max(A[0], B[l//2 – 2]), min(A[1], B[l//2 + 1])
                candidate_sort = sorted([nums2[l // 2 - 1], nums2[l // 2],
                                         max(nums1[0], nums2[l // 2 - 2]),
                                         min(nums1[1], nums2[l // 2 + 2])])
                return candidate_sort[1] * 0.5 + candidate_sort[2] * 0.5
        else:
            l1 = len(nums1)
            l2 = len(nums2)
            if l2 % 2 != 0:
                median2 = nums2[(l2 - 1) // 2]
            else:
                median2 = nums2[l2 // 2 - 1] * 0.5 + nums2[l2 // 2] * 0.5
            if l1 % 2 != 0:
                if nums1[(l1 - 1) // 2] > median2:
                    return self.findMedianSortedArrays(nums1[:(l1 - 1) // 2 + 1], nums2[(l1 - 1) // 2 - 1:])
                else:
                    return self.findMedianSortedArrays(nums1[(l1 - 1) // 2:], nums2[:l2 - (l1 - 1) // 2 + 1])
            else:
                median1 = nums1[l1 // 2 - 1] * 0.5 + nums1[l1 // 2] * 0.5
                if median1 > median2:
                    return self.findMedianSortedArrays(nums1[:l1 // 2 + 1], nums2[l1 // 2 - 1:])
                else:
                    return self.findMedianSortedArrays(nums1[l1 // 2 - 1:], nums2[:l2 - l1 // 2 + 1])
