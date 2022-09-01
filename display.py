import csv
import itertools
import matplotlib.pyplot as plt
import os
import shutil

frame = 0

with open('Data/data.csv') as file:
    reader, length = itertools.tee(csv.reader(file, delimiter=','))
    l = int((len(next(length)) - 1) / 25)
    del length
    os.mkdir('images')

    plt.ion()

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    points, = ax.plot([-10000, 10000], [-10000, 10000], 'wo', markersize=3)
    ax.set_aspect('equal', adjustable='box')
    text = fig.text(0.23, 0.84, '0 years', color='white')

    for row in reader:
        x, y = [], []
        for i in range(l):
            x.append(float(row[(25 * i) + 4]))
            y.append(float(row[(25 * i) + 5]))
        points.set_xdata(x)
        points.set_ydata(y)
        if (float(row[0]) >= 1000000000):
            text.set_text(f'{round((float(row[0]) / 1000000000), 2)} billion years')
        elif (float(row[0]) >= 1000000):
            text.set_text(f'{round((float(row[0]) / 1000000), 2)} million years')
        elif (float(row[0]) >= 1000):
            text.set_text(f'{round((float(row[0]) / 1000), 2)} thousand years')
        else:
            text.set_text(f'{float(row[0])} years')
        ax.autoscale_view()
        fig.canvas.draw()
        fig.savefig(f'Images/img{str(frame).zfill(4)}.png')
        fig.canvas.flush_events()
        frame += 1
os.system('ffmpeg -r 30 -i "images/img%04d.png" -c:v libx264 -pix_fmt yuv420p simulation.mp4')
shutil.rmtree('images')
