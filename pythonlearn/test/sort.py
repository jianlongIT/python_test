# -*- coding: utf-8 -*-
# Auther : jianlong

nums = [2, 3, 4, 5, 2, 3, 432, 41244, 66, 1, ]
nums.sort(reverse=True)
print(nums)
nums.sort(reverse=False)
print(nums)

nums2 = [99, 96, 97.5, 89, 95.5, 93, 99, 95, 98, 99.5]
nums2.remove(max(nums2))
nums2.remove(min(nums2))
sum2 = sum(nums2)
c = len(nums2)
print(sum2, c, sum2 / c)

ss = {"ss": "ss", 'bb': "bb"}
ss.items()
