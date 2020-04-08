#!/usr/bin/python3
# Write a function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    if list_of_integers:
        size = len(list_of_integers)
        end_list = size - 1
        start_list = 0
        peak = list_of_integers[int(size/2)]
        for i in range(int(size/2)):
            if list_of_integers[start_list] <= list_of_integers[end_list]:
                if peak <= list_of_integers[end_list]:
                    peak = list_of_integers[end_list]
            else:
                if peak <= list_of_integers[start_list]:
                    peak = list_of_integers[start_list]
            end_list -= 1
            start_list += 1
        return(peak)   
