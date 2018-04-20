#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 22:33:48 2018

@author: crantu
"""

import csv


def export_txt():
    msg0 = "G01X{:.3f}Y{:.3f};"
    msg1 = "# CHOKUSEN-KAKO # <move to C{}>"

    with open("NCProgramming_C.csv", "w") as f:
        writer = csv.writer(f)

        for i, xy in enumerate(get_xy_list()):
            tmp_msg0 = msg0.format(xy["x"], xy["y"])
            tmp_msg1 = msg1.format(i)
            # print(tmp_msg)
            writer.writerow([tmp_msg0, tmp_msg1])


def get_xy_list():

    xy_list = []

    with open("NCprogramming_C_xy.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        # print("header:", header)
        for row in reader:
            tmp_xy = {"x": 0.0, "y": 0.0}

            if row[0] == "96":
                break

            no = int(row[0]) % 4

            if no == 0 or no == 1:
                mode = 0
            elif no == 2 or no == 3:
                mode = 2
            else:
                raise ValueError

            tmp_xy["x"] = float(row[1+mode])
            tmp_xy["y"] = float(row[2+mode])
            xy_list.append(tmp_xy)

    return xy_list


if __name__ == "__main__":
    export_txt()
