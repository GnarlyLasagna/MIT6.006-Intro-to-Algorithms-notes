# def canSum(target, numbers, memo = {}):
#     if (target in memo):
#         return memo[target]
#     elif target == 0:
#         return True
#     elif target < 0:
#         return False
#     for i in numbers:
#         remainder = target - i
#         if canSum(remainder, numbers, memo):
#             memo[target] = True
#             return True
#         else:
#             memo[target] = False
#             return False

def canSum(targetsum, numbers):
    memo = dict()
    def cansum_helper(targetsum, numbers):
        # check in memory
        if targetsum in memo:
            return memo[targetsum]
        if targetsum < 0:
            return False
        if targetsum == 0:
            return True
        for number in numbers:
            remainder = targetsum - number
            if cansum_helper(remainder, numbers) == True:
                memo[targetsum] = True
                return True
        memo[targetsum] = False
        return False

    result = cansum_helper(targetsum, numbers)

    print(memo)

    return result


print(canSum(7, [2, 3])); ##true
print(canSum(7, [5, 3, 4, 7])); ##true
print(canSum(7, [2, 4])); ##false
print(canSum(8, [2, 3, 5])); ##true
print(canSum(300, [7, 14])); ##false
print(canSum(400, [7, 14, 12])); ##true

