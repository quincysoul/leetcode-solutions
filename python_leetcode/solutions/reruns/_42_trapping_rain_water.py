class Solution:
    def trap(self, elevation_map_list):
        # 1. Find highest point to iterate to

        if len(elevation_map_list) == 0:
            return 0

        highest_point = max(elevation_map_list)
        highest_point_index = elevation_map_list.index(highest_point)

        print(highest_point)
        print(highest_point_index)

        total_water_sum = 0

        current_highest = -1
        for i in range(highest_point_index):
            if elevation_map_list[i] >= current_highest:
                current_highest = elevation_map_list[i]
                continue
            else:
                total_water_sum += current_highest - elevation_map_list[i]

        current_highest = -1
        i = 0
        for element in reversed(elevation_map_list):
            if i == len(elevation_map_list) - 1 - highest_point_index:
                break
            if element >= current_highest:
                current_highest = element
                i += 1
                continue
            else:
                total_water_sum += current_highest - element
                i += 1

        return total_water_sum
