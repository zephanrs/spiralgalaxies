from orbitsimulation import galaxy, blackHole, star
import time

spiral = galaxy(width=1400, height=900)

center = blackHole(spiral, mass=10000)
star2 = star(spiral, mass=1, position=(-200, 0), velocity=(0, 6))
star3 = star(spiral, mass=3, position=(400, 0), velocity=(0,2))
star4 = star(spiral, mass=5, position=(300, 100), velocity=(0,2))
star5 = star(spiral, mass=7, position=(400, 200), velocity=(0,2))
star6 = star(spiral, mass=9, position=(100, 0), velocity=(0,10))
#star7 = star(spiral, mass=11, position=(600, 600), velocity=(-1,-1))


while True:
    time.sleep(0.01)
    spiral.update_all()