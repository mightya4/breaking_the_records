#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    # Create array for lowest/highest score breaking records
    # Create array to track points of high/low record break
    # Index 0 for breaking highest points index 1 for breaking least points record
    score_breaking_records = [0, 0]
    score_limits = [0, 0]
    end_of_array = len(scores)

    #Update values for both high/low limits with initial score array element
    score_limits[0] = scores[0]
    score_limits[1] = scores[0]

    def update_score_info(score_point, score_card, ind, val):
        update_score_limits(score_card, ind, val)
        update_counter(score_point, ind)

    def update_score_limits(score_card, ind, val):
        score_card[ind] = val

    def update_counter(score_point, ind):
        score_point[ind] += 1
 

    # If element is < lowest score
    # Update lowest score
    # Increment lowest score index
    [update_score_info(score_breaking_records, score_limits, 1, x) for x in scores if x < score_limits[1]]

    # If element > highest score
    # Update highest score
    # Increment highest score index
    [update_score_info(score_breaking_records, score_limits, 0, x) for x in scores if x > score_limits[0]]
    return score_breaking_records

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
