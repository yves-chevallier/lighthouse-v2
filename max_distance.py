from math import pi, tan, atan

freq = 50 # Hertz (swipe cycle frequency) [1/s]
v = pi * freq # Sweep speed [rad/s]
a = 3e-3 # Approximate sensor aperture [m]
m = 6e6 # Encoded data bits per seconds
bits = 17 # Minimum number of bits required to decode the frame
w = tan(5e-3 / 20) # Beam width

def max_distance(a):
    return (a) / atan(bits / m * v - w)

# Maximum operating distance for different aperture size
# Only valid if the sensor is perpendicular to the lighthouse
# 1 mm :  5 m
# 2 mm :  10 m
# 3 mm :  15 m
# 4 mm :  20 m
for a in range(1, 5):
    print(f"{a} mm : ", "%d m" % max_distance(a* 1e-3))

# With an IMU, knowing g direction, we could estimate the sensor
# angle related to the
