

# Python3 code for Max 
# Water Container
def mostWater(height):
    left = 0
    right = len(A) -1
    area = 0
     
    while left < right:

        area = max(area, min(height[left], 
                        height[right]) * (right - left))
     
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area
 
n = int(input('Enter the number of vertical bars: '))
print('Enter the heights of vertical bars:\n')
height = []
for i in range(n):
    i = int(input('>>'))
    heights.append(i)
 
print(f'The maximum area of water : {mostWater(heights)}')