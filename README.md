# Building Bézier Curves with Divide and Conquer based Midpoint Algorithm  

Tugas Kecil 2 Mata Kuliah IF2211 Strategi Algoritma 2024 - Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis Divide and Conquer

## Table of Contents
- [Description](#description)
- [Requirements and Installation](#requirements-and-installation)
- [How to Run](#how-to-run)
- [Program Display](#program-display)
- [Author Information](#author-information)

## Description
This program is designed to animate the process of forming Bézier curves using a divide and conquer based midpoint algorithm. By inputting a set of control points, the program will progressively display the curve formation from these points through a series of iterations.

## Requirements and Installation
- Python 3.x
- Matplotlib

### Installing Matplotlib
```bash
pip install matplotlib
```

## How to Run
To run the program, open a terminal or command prompt, navigate to the directory where the program file is saved
```
cd src
```
then execute the command
```
python main.py
```
After launching the program, you will be prompted to enter several inputs to configure the Bézier curve animation:
### Input Fromat
1. Control Points: First, you will be asked to enter the number of control points. A minimum of 2 control points are required to form a Bézier curve. For each control point, enter the x and y coordinates separated by a space.
```bash
Enter the number of control points: 3
Enter the x and y coordinates of point 1: 0 0
Enter the x and y coordinates of point 2: 1 2
Enter the x and y coordinates of point 3: 2 0
```
2. Algorithm Selection: Next, select the algorithm to use for generating the Bézier curve.
```bash
Select the algorithm to use:
1. Brute Force
2. Divide and Conquer
Enter the number of the algorithm: 2
```
3. If you choose Divide and Conquer, enter the number of iterations:
```bash
Enter the number of iterations: 3
```

## Program Display

## Author Information
| Name                    | NIM      |
| ----------------------- |:--------:|
| Melati Anggraini        | 13522035 |
| Novelya Putri Ramadhani | 13522096 |