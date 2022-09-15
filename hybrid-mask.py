import numpy as np

"""
Cases:
0:
None:
L/R:
Generate initial position info
Given w and turning radius, construct two circles
All squares that fall between, or overlap the borders of, those two circles are 
given 1. Only selecting however from a length of L + rover length 


Figure the above out for grid-square 10cm, rover width 1.2x1.2.
Then generalise


Possibly visualise for additional POWAH
"""
def construct_blank_array (radius, primitive_length, rov_width, rov_length, square_size): 
    """
    :param radius: Turning radius of rover in cm
    :param primitive_length: Length of motion primitive about circle defined by radius
    :param rov_width: width of rover in cm, dimension parallel to turning radius
    :param rov_length: length of rover in cm, dimension perpendicular to turning radius
    :grid_size: size of a grid square in cm
    :return: Initial pos of rover within grid square (x,y intger tuple), 0 array 
    """

    #Logic:
    # If turning to left, rover starts on right side
    # If turning to right, rover starts on left side
    # Center of turning radius is origin
    # One side is radius + width/2 + padding
    # Other side is cos(max_angle)*(radius+width/2+padding)
    # max angle calculated from L
    origin = (0,0)
    position_array = []

    # Angle (degrees) of endpoint of centre of motion primitive
    # Abs because size of array is independent of direction of curve and don't want to handle negative numbers
    end_angle = int((180/np.pi)*(primitive_length/abs(radius)))

    range_of_angles = range(0,end_angle,90)
    for angle in range_of_angles:
        position_array.append((np.cos(angle) * abs(radius), np.sin(angle) * abs(radius)))

    position_array.append((np.cos(end_angle) * abs(radius), np.sin(end_angle) * abs(radius))) # Pos2
    
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for pos in position_array:
        if pos[0] > max_x:
            max_x = pos[0]
        if pos[0] < min_x:
            min_x = pos[0]
        if pos[1] > max_y:
            max_y = pos[1]
        if pos[1] < min_y:
            min_y = pos[1]

    # Padding
    padding = max(rov_width, rov_length) * 2
    max_x += padding
    min_x -= padding
    max_y += padding
    min_y -= padding

    grid_width = int(np.ceil((max_x - min_x) / square_size))
    grid_height = int(np.ceil((max_y - min_y) / square_size))

    blank_array = np.zeros((grid_width, grid_height))

    #TODO: Calculate origin and rover centre
    return blank_array, origin, rov_centre


def print_array (arr):
    for line in arr:
        for value in line:
            print(int(value), end = "")
        print("")

def construct_ring_segment (radius, rov_width, rov_length):
    """
    :param radius: Turning radius of rover in cm
    :param rov_width: width of rover in cm, dimension parallel to turning radius
    :param rov_length: length of rover in cm, dimension perpendicular to turning radius
    :return: section of ring rover will exist within - boolean mask
    """
    inner_radius = radius - rov_width/2
    outer_radius = radius + rov_width/2

def main():
    arr = construct_blank_array(100, 600, 120, 120, 10)
    print_array(arr)

if __name__ == '__main__':
    main()