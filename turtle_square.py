#!/usr/bin/env python3
import time

def draw_square():
    size = 5
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    steps = [
        [(0, j) for j in range(size)],
        [(i, size-1) for i in range(size)],
        [(size-1, j) for j in range(size-1, -1, -1)],
        [(i, 0) for i in range(size-1, -1, -1)]
    ]
    
    print("--- Turtle Square Trajectory Simulation ---\n")
    for side in steps:
        for r, c in side:
            grid[r][c] = '#'
            print('\n'.join([' '.join(row) for row in grid]))
            print('\n' + '='*15)
            time.sleep(0.1)

if __name__ == '__main__':
    draw_square()
