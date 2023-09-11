"""
4. While loops (while)

    4.6. Implement an algorithm for calculating an approximation for the value
         of pi (π). Let's assume that A is a unit circle. A unit circle has
         the radius of one and it is centered at the origin (0,0). Smallest
         possible square B is drawn around the unit circle so that circle A is
         completely inside the square. The corners of the square are now
         (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random
         points are scattered inside the square, the fraction of points that
         fall inside the circle A correlates with the fraction of the area of
         circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
         This can be used as a simple method for calculating an approximation
         of the value of pi: Let's generate a large number of random points,
         such as one million, inside square B. Let N be the total number of
         random points. Each point inside the square is tested for whether it
         resides inside circle A. Let n be the total number of points that fall
         inside circle A. Now we have n/N≈π/4, and from that we get
         π≈4n/N. Write a program that asks the user how many random points
         to generate, and then calculates the approximate value of pi using the
         method explained above. At the end, the program prints out the
         approximation of pi to the user. (Notice that it is easy to test if
         a point falls inside circle A by testing if it fulfills the inequation
         x^2+y^2<1.).

"""
import time
from threading import Thread
from random import uniform

def calculate_points(number, results):
    num_circle = 0


    while number > 0:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            num_circle += 1

        number -= 1

    results.append(num_circle)

print("Let's calculate an approximation for the value of pi (π).")
number = int(input('Please input how many random points to generate.\n'))
Num = number

start = time.time()

threads_num = 10
threads = []
results = []


for item in range(threads_num):
    thread_ = Thread(target=calculate_points, args=(number/threads_num, results))
    threads.append(thread_)

for thread_ in threads:
    thread_.start()

for thread_ in threads:
    thread_.join()

num_circle = sum(results)


pi = num_circle * 4 / Num

print(num_circle, Num)
print(f'The approximation of pi is: {pi}')

print(f'Running in {time.time()-start:.2f} seconds.')
