nums = [1,2,3,4]
ans = [0] * len(nums)
ans[0] = nums[0]
for i in range(1, len(nums)):
    ans[i] = ans[i-1] + nums[i]
# Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
# 在此期间可以得知 ans是之前的ans与对应位置的num的array相加

print(ans)