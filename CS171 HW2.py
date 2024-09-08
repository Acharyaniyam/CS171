# Purpose: A program that asks the user to enter the launch angle and velocity, and a a distance along the trajectory and calculates the height y of the projectile at at distance x.
# Author: Niyam Acharya
# Date:    7/11/2023

# import necessary module
import math

# define the required function below this line
def projectileMotion(theta, speed, distance):
    G = 9.81
    theta_degree = math.radians(theta)
    y = (distance * math.tan(theta_degree)) - ((G * math.pow(distance,2)) / (2 * math.pow(speed, 2) * math.pow(math.cos(theta_degree),2)))
    return y

# main script
if __name__ == "__main__" :
    # main script code goes below this line. Keep the same indentation level as this line.
    theta = float(input('Enter launch angle in degrees: '))
    speed = float(input('Enter launch velocity in meters per seconds: '))
    distance = float(input('Enter distance in meters: '))
    print('The height of this projectile at a distance of', format(distance, '.2f'), 'meters along its trajectory is', format(projectileMotion(theta, speed, distance), '.2f') , 'meters')
    