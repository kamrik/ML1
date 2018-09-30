################################################################################
## COMP3122 - Home assignment 1 - Due: Tuesday Oct 9, 23:59                   ##
################################################################################

# Read the instructions below and complete the function for each task.
#  - The __main__ section at the bottom contains test cases which will also
#    provide an estimate of your grade.
#  - Submit the completed assignment by emailing it as an attachment to
#    graderbot@kamrik.org (as a .py file, no zip)
#  - You can submit up to 5 times, the best submissions will be used.

# Scoring: The score calculated here is just an estimate, actual score will be
# calculated by other code (otherwise it would be too easy to cheat). For the
# score to be calculated properly, importing this file must not crash with an
# unhandled exception. Submissions where the estimate differs from the actual
# grade significantly will be inspected manually.

# General hints:
#  - You may want to use loops (not everything is supposed to be a one-liner)


# Useful references
# - Quick Python reference: https://learnxinyminutes.com/docs/python3/
# - Chapter 2 of the book: https://jakevdp.github.io/PythonDataScienceHandbook/

import numpy as np

assignment_name = 'assignment1'
assignment_version = '1.0'


## Task 1 ###################################################################### 
# Replace 999 with your student id
student_id = 999

## Task 2 ######################################################################
# Create an N by N 2D array with 1 on both diagonals and zeros everywhere else. 
# Examples :
#           N = 4                N = 3
#       [[1, 0, 0, 1],        [[1, 0, 1],
#        [0, 1, 1, 0],         [0, 1, 0],
#        [0, 1, 1, 0],         [1, 0, 1]]
#        [1, 0, 0, 1]])

def xmatrix(N):
    return np.zeros((N,N), dtype=int)

## Task 3 ######################################################################
# Write a function that given a 2D array m finds the column with the lowest sum, 
# and the row with the lowest sum and returns their indices.
# min_row_col(m) => [min_row_idx, min_col_idx]
# For example:
# m1 = np.array( [[0, 1, 2],
#                 [0, 0, 0],
#                 [0, 1, 2]])
# In [n]: min_row_col(m1)
# Out[n]: [1, 0]
# The lowest sums are in the middle row (row 1) and the leftmost column (col 0).
#
# The output value should be either a list or a tuple of length 2, row index
# first, and then column index.
# If two or more rows (or columns) have the same lowest sum, use the one with 
# the lowest index.
# 
# Hints:
#  - Check out the numpy argmin() function: same as min, but returns the index
#    of the minimum rather than the minimum itself.
#    For example, for 1D array `b` if ix = b.argmin() then b[ix] == b.min()

def min_row_col(m):
    return 0, 0  # min_row_ix, min_col_ix

## Task 4 ###################################################################### 
# The `car_data` array holds reading from a car dashboard. The first column is
# speed in km/h and the second column is engine rotation speed in revolutions
# per minute (RPM). After the readings were taken it was discovered that both
# gauges exaggerate their readings, the speed is reported `speed_bias` above the
# real speed and the RPMs are `rpm_bias` above the real RPMs. Write a function
# that takes the readings and the biases and returns the corrected data.
# The returned array should be of the same shape as `car_data`.
#
# FYI: The RPM gauge is called "tachometer"
def fix_gauge_bias(car_data, speed_bias, rpm_bias):
    return car_data

## Task 5
# Continuing with car data from previous task. In most cars the ratio between
# car speed and engine rotation speed only changes when the car shifts gears.
# For example in the test data for the previous task (after adjustment for
# biases), RPMs=(car speed)*85 for _all_ rows. This means the car was in the
# same gear while all of the readings were taken and the speed ratio was 85.
#
# Write a function that detects if the car switched gears and returns True if it
# did and False otherwise. Use the following assumptions:
#  - The car from which this data originates has simple gears with constant
#    ratios as described above.
#  - RPMs/(car speed) ratios for different gears differ by at least 10%. For
#    example ratios of 75 and 95 are definitely from different gears, while 85.1
#    and 85.2 should be considered the same gear. The slight variations can
#    result from measurement inaccuracies and rounding errors, but you can
#    safely assume that those variations are way below 10%.
#  - The data is in the same format as before - two columns - [km/h, RPMs]
#  - Any known biases were already accounted for in the input - no need to call
#    fix_gauge_bias()
#
# FYI: The ratio behaves differently for some newer transmission architectures
# such as continuously variable transmission (CVT) and the hybrid transmission
# in Toyota Prius.
def was_gear_switched(car_data):
    return False

## Task 6 (bonus) ##############################################################
# With the same data and assumptions as Task 3 count how many different gears
# were used. If car goes from gear 1 to gear 2 and back to gear 1, it still
# counts as two different gears, not 3. 
#
# NOTE: it's difficult to solve this question perfectly, almost any strategy
# here can be tricked by specially constructed weird data. Try to come up with a
# reasonable strategy that would result in a correct answer in most cases.
#
# HINT: take a look at np.unique() and array sort() functions, they might be
# useful (depending on the strategy you choose).
def count_gears_used(car_data):
    return 1

    

if __name__ == '__main__':
    ## Your own tests, feel free to do whatever you want here as long as it doesn't crash
    # print('Task 1: %s', min_row_col(np.array([0])))

    ##============================ Tests (don't change) ======================##

    # Convenience variables for printouts
    OUT = 'OUT ╦'
    OK  = '    ╚ OK'
    ERR = '    ╚ ERROR:'

    total_score = 0

    print('####### Task1: student ID #########################################')
    print(OUT, 'Student ID:', student_id)
    if student_id == 999 or student_id is None or type(student_id) != int:
        print(ERR, 'student_id not set')
    else:
        print(OK)
    
    print()
    print('####### Task2: x matrix ###########################################')
    task_score = 25
    for N in range(3,6):
        xm = xmatrix(N)
        print(OUT, 'xmatrix(%d) = \n%s' % (N, xm.__repr__()))
        if xm[N//2,0] == 0 and xm[0, 0] == 1 and xm[N//2, N//2] == 1:
            print(OK)
        else:
            print(ERR, 'xmaxtrix(%d) doesn\'t look right' % N)
            task_score = 0
    total_score += task_score

    print()
    print('####### Task3: Find row and column with minimal sums ##############')
    task_score = 25
    # Expect min_row_col(m1) => [1, 0]
    m1 = np.array( [[0, 1, 2],
                    [0, 0, 0],
                    [0, 1, 2]])
    minrc1 = min_row_col(m1)
    print(OUT, 'min_row_col(m1) => %s' % (minrc1,) )
    if len(minrc1) == 2 and minrc1[0] == 1 and minrc1[1] == 0:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected [1, 0]')

    # Expect min_row_col(m2) => [1, 1]
    m2 = np.array( [[1, 0, 1],
                    [0, 0, 0],
                    [1, 0, 1]])
    minrc2 = min_row_col(m2)
    print(OUT, 'min_row_col(m2) => %s' % (minrc2,) )
    if len(minrc2) == 2 and minrc2[0] == 1 and minrc2[1] == 1:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected [1, 1]')

    # Expect min_row_col(m3) => [0, 0]
    m3 = np.array( [[0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])
    minrc3 = min_row_col(m3)
    print(OUT, 'min_row_col(m3) => %s' % (minrc3,) )
    if len(minrc3) == 2 and minrc3[0] == 0 and minrc3[1] == 0:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected [0, 0]')
    
    # Expect min_row_col(m3) => [0, 0]
    m4 = np.array([[0]])
    minrc4 = min_row_col(m3)
    print(OUT, 'min_row_col(m4) => %s' % (minrc4,) )
    if len(minrc4) == 2 and minrc4[0] == 0 and minrc4[1] == 0:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected [0, 0]')

    total_score += task_score
        
    print()
    print('####### Task4: fix car speed readings #############################')
    # Car speed data:      km/h   RPM
    gauges = np.array( [[  28.2, 2524 ],
                        [  30  , 2677 ],
                        [  31.8, 2830 ],
                        [  33.6, 2983 ],
                        [  35.4, 3136 ]])
    s_bias = 1.8
    r_bias = 280
    adjusted = fix_gauge_bias(gauges.copy(), s_bias, r_bias)
    d = gauges - adjusted
    print(OUT, 'fix_gauge_bias(gauges, ...)[0] = %s' % (adjusted[0],) )
    if adjusted.shape == gauges.shape and np.allclose(d[0], [s_bias, r_bias]):
        print(OK)
        total_score += 25
    else:
        print(ERR, 'expected [%0.2f, %d]' % (gauges[0, 0] - s_bias, gauges[0, 1] - r_bias))

    print()
    print('####### Task5: was there a gear shift #############################')
    task_score = 25
    # Car speed data:          km/h   RPM
    no_shift = np.array(   [[  26.4, 2244. ],
                            [  28.2, 2397. ],
                            [  30. , 2550. ],
                            [  31.8, 2703. ],
                            [  33.6, 2856. ]])
    # Note that for all readings above have the same ratio. Below we construct
    # input with a gear shift.
    yes_shift = no_shift.copy()
    yes_shift[0, 1] = yes_shift[0, 0] * 105
                            
    wasSwitched1 = was_gear_switched(no_shift)
    print(OUT, 'was_gear_switched(no_shift) = %s' % (wasSwitched1,) )
    if not wasSwitched1:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected False')

    wasSwitched2 = was_gear_switched(yes_shift)
    print(OUT, 'was_gear_switched(yes_shift) = %s' % (wasSwitched2,) )
    if wasSwitched2:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected True')

    total_score += task_score

    print()
    print('####### Task6: count gears used #############################')
    task_score = 25
    n1 = count_gears_used(no_shift)
    print(OUT, 'count_gears_used(no_shift) = %s' % (n1,) )
    if n1 == 1:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected 1')

    n2 = count_gears_used(yes_shift)
    print(OUT, 'count_gears_used(yes_shift) = %s' % (n2,) )
    if n2 == 2:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected 2')
        
    two_shifts = yes_shift.copy()
    two_shifts[-1, 1] = two_shifts[-1,0] * 70
    n3 = count_gears_used(two_shifts)
    print(OUT, 'count_gears_used(yes_shift) = %s' % (n3,) )
    if n3 == 3:
        print(OK)
    else:
        task_score = 0
        print(ERR, 'expected 3')

    total_score += task_score


    ### Estimated total score
    print('ESTIMATED SCORE: %d (if above 100 will be set to 100)' % total_score)
