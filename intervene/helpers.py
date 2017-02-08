# coding: utf-8
'''
Helper functions for Intervene
'''
from matplotlib import colors

def default_colors():
    """
    Get a list of RGBA colors 
    """
    # default_colors = [
    #     # r, g, b, a
    #     [92, 192, 98, 0.5],
    #     [90, 155, 212, 0.5],
    #     [246, 236, 86, 0.6],
    #     [241, 90, 96, 0.4],
    #     [255, 117, 0, 0.3],
    #     [82, 82, 190, 0.2],
    # ]

    default_colors = [
        # r, g, b, a
        [188, 114, 3, 0.5],
        [3, 133, 188, 0.5],
        [155, 9, 118, 0.6],
        [155, 53, 9, 0.4],
        [4, 140, 128, 0.3],
        [140, 8, 8, 0.2],
    ]

    default_colors = [
        [i[0] / 255.0, i[1] / 255.0, i[2] / 255.0, i[3]]
        for i in default_colors
    ]

    return default_colors

def get_colors(color_list):
    """
    Get color combinations for Venn diagram. This converts color names to RGBA 

    """
    rgba_colors = []
    a = [0.5,0.5,0.6,0.4,0.3,0.2]
    i = 0
    for c in color_list:
        rgba_colors.append(list(colors.to_rgba(c)))
        rgba_colors[i][3] = a[i]
        i+=1

    return rgba_colors
