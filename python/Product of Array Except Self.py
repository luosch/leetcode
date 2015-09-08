class Solution(object):
    def productExceptSelf(self, nums):
        number_of_zero = 0
        max_product = 1

        for num in nums:
            if num == 0:
                number_of_zero += 1
            else:
                max_product *= num

        results = []
        for num in nums:
            if number_of_zero > 1:
                results.append(0)
            elif number_of_zero == 1:
                if num == 0:
                    results.append(max_product)
                else:
                    results.append(0)
            else:
                results.append(max_product / num)
            
        return results
