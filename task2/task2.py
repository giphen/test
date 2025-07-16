import sys

def read_circle(circle_file):
    with open(circle_file, 'r') as file:
        center = tuple(map(float, file.readline().split()))
        radius = float(file.readline())
    return center, radius

def main():

    circle_file = sys.argv[1]
    dot_file = sys.argv[2]

    center, radius = read_circle(circle_file)
    dots = read_dots(dot_file)

    notes = {

        0: "лежит на окружности",
        1: "лежит внутри окружности",
        2: "лежит вне окружности"

    }

    for dot in dots:
        position = dot_pos(center, radius, dot)
        print(f"{position} - Точка {notes[position]}")


def read_dots(dot_file):
    with open(dot_file, 'r') as file:
        dots = [tuple(map(float, line.split())) for line in file]
    return dots


def dot_pos(center, radius, dot):
    circle_distance = (dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2
    circle_radius = radius * radius

    if circle_distance == circle_radius:
        return 0
    if circle_distance < circle_radius:
        return 1
    else:
        return 2
    
main()

            #Для использования введите: python task2.py < файл circle.txt> < файл dot.txt >
