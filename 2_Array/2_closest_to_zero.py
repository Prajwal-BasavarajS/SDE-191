# # def closest_to_zero(nums):
# #     closest = nums[0]
# #     for x in nums:
# #         if abs(x) < abs(closest):
# #             closest = x
        
# #         if closest < 0 and abs(closest) in nums :
# #             return abs(closest)
# #         else :
# #             return closest 
        

# # if __name__ == "__main__":
# #     test_arrays = [
# #         [3, -1, -7, 2, 5],
# #         [-2, 2, 1, -1],
# #         [-5, -3, -1],
# #         [4, 2, 8],
# #         [0, -1, 1],
# #         []
# #     ]


# # for nums in test_arrays:
# #     print(" input array = " , nums)
# #     print("\n closest to 0 is :   ",closest_to_zero(nums))
# def closest_to_zero(nums):
#     if not nums:  # handle empty array
#         return None

#     closest = nums[0]
#     for x in nums:
#         # If abs(x) is smaller, update
#         if abs(x) < abs(closest):
#             closest = x
#         # If tie, prefer positive
#         elif abs(x) == abs(closest) and x > closest:
#             closest = x
#     return closest


# if __name__ == "__main__":
#     test_arrays = [
#         [3, -1, -7, 2, 5],
#         [-2, 2, 1, -1],
#         [-5, -3, -1],
#         [4, 2, 8],
#         [0, -1, 1],
#         []
#     ]

#     for nums in test_arrays:
#         print("Input array:", nums)
#         print("Closest to 0:", closest_to_zero(nums))
#         print("-" * 30)



def closest_to_zero(nums):
    if not nums :
        return None
    
    closest = nums[0]

    for x in nums:
        if abs(x) < abs(closest):
            closest = x
        elif abs(x) == abs(closest) and x > closest :
            closest = x

    return closest
    


test_case = [[1,-1,2,3,4,-5],[-5,-2,-1],[1,-1,0],[]]

for nums in test_case:
    print("closest_to_zero : " , closest_to_zero(nums))
    print("-"*30)