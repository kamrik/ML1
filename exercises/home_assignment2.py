################################################################################    
## COMP3122 - Home assignment 2 - Due: Tuesday Nov 20, 23:59                  ##
################################################################################

# Read the instructions below and complete the function for each task.
#  - The __main__ section at the bottom contains test cases which will also
#    provide an estimate of your grade.
#  - Submit the completed assignment by emailing it as an attachment to
#    graderbot@kamrik.org (as a .py file, no zip)
#  - You can submit up to 5 times, the best submissions will be used.
#
# Scoring: The score calculated here is just an estimate, actual score will be
# calculated by other code (otherwise it would be too easy to cheat). For the
# score to be calculated properly, importing this file must not crash with an
# unhandled exception. Submissions where the estimate differs from the actual
# grade significantly will be inspected manually.
#
# General hints:
#  - Brush up your memory about Python data types: List, Dict and Set
#  - Feel free to define helper functions if you want to
#  - Experiment with your code - computer is much faster than you at 
#    interpreting code 
#  - Don't overthink
#
# Useful references
# - Quick Python reference: https://learnxinyminutes.com/docs/python3/

assignment_name = 'assignment2'
assignment_version = '1.0'


## Task 1 ######################################################################
# Replace 999 with your student id
student_id = 999


## Task 2 - Average-by #########################################################
# You are only allowed to use the Python standard libraries for this task: 
# No NumPy, no Pandas !!!
#
# Given a table of data represented as a list of lists, compute the averages
# of a specified column `col`, within groups specified by column `by`
# `col` and `by` are column indices.
# The input table is a list lists, each inner list is a row of the table.
# The output should be a dictionary.
#
# Example:
# Calculating the average of col 0, grouped by col 3
# [[15 29  6  2]
#  [16  9  8  0]
#  [ 7 27 16  0]]
# OUT - {0: 11.5, 2: 15.0}
#     - OK
#
# Make sure to try edge cases, such as an empty table.
# No need to check input validity.
def avgby(tbl, col, by):
    return {}


## Task 3 - Merge ##############################################################
# You are only allowed to use the Python standard libraries for this task: 
# No NumPy, no Pandas !!!
#
# Write a merge function to implement a _inner_ join of two data tables each 
# represented as a list of rows where each row is a list.
#
# Inputs:
#  - `left` and `right` - data tables
#  - `left_on` and `right_on` - the column indices containing the key to merge 
#     on in each of the tables.
# 
# Example 1:
# Merging on column 0 of each table (person name)
# left = [['Bob', 'Accounting'],
#         ['Jake', 'Engineering'],
#         ['Lisa', 'HR']]
# right = [['Lisa', 2004],
#         ['Bob', 2008], 
#         ['Jake', 2012], 
#         ['Sue', 2014]]
# merged =   [['Bob', 'Accounting', 'Bob', 2008],
#             ['Jake', 'Engineering', 'Jake', 2012],
#             ['Lisa', 'HR', 'Lisa', 2004]]
#  
# Example 2:
# Merging on columns 1 and 0, note that 'B' appears twice in the right table.
# left = [[1, 'A'], [2, 'B'], [3, 'C']]
# right = [['A', 2004], ['B', 2008], ['C', 2012], ['B', 2014]]
# merged =   [[1, 'A', 'A', 2004],
#             [2, 'B', 'B', 2008],
#             [2, 'B', 'B', 2014],
#             [3, 'C', 'C', 2012]]
#
# "Inner join" means that only rows with data from both tables are returned.
# Each row in the merged table should be the concatenation of corresponding
# rows from the left and right tables. 
# In terms of Python lists:
#     row_in_merged_tbl = row_from_left + row_from_right
# where the following is true
#     row_from_left[left_on] == row_from_right[right_on]
# This merge is essentially equivalent to pd.merge(tbl1, tbl2, left_on=?, right_on=?)
# You can read about Pandas merge function in the book:
# https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html#Categories-of-Joins
# Note what happens when a key appears multiple times in both tables
# https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html#Many-to-many-joins

def merge(left, right, left_on, right_on):
    merged = []
    return merged


################################## Tests #######################################
if __name__ == '__main__':
    # Convenience variables for printouts
    OUT = 'OUT ╦'
    OK  = '    ╚ OK'
    ERR = '    ╚ ERROR:'

    total_score = 0

    print('####### Task1: student ID ########################################')
    print(OUT, 'Student ID:', student_id)
    if student_id == 999 or student_id is None or type(student_id) != int:
        print(ERR, 'student_id not set')
    else:
        print(OK)
    
    # This is for tests only, don't use NumPy in your solutions.
    import numpy as np
    import pandas as pd

    print()
    print('####### Task 2: average by ########################################')
    task_score = 0

    # Test the case of empty table
    if avgby([], 1, 0) != {}:
        print(ERR, "avgby([],...) should return and empty dict")
    task_score = 5  # 5 points for avgby() not crashing so far.

    # A helper function for comparing dicts with floating point values.
    def cmp_dict(d1, d2):
        if set(d1.keys()) != set(d2.keys()):
            return False
        for k in d1:
            if d1[k] - d2[k] > 1e-6:
                return False
        return True

    # Run a bunch of randomly generated cases
    # Once your solution works for 10 cases, try running it with a 1000 cases.
    n_cases = 10
    rng = np.random.RandomState(seed=1) # Settin the seed for repeatability
    for test_case in range(n_cases):
        # Generating random input data
        nrows = rng.randint(15)
        ncols = rng.randint(2, 6)
        # The input table will be of shape (nrows, ncols) containing integers
        arr = rng.randint(30, size=(nrows, ncols))
        by = rng.randint(ncols)

        # Randomly decide which column to average
        avg_col = rng.randint(ncols)

        # Change the 'by' column so that it contains multiple copies of the same 
        # number, this way group by makes more sense.
        groupmod = rng.randint(1, nrows+2)
        arr[:, by] %= groupmod

        print("Case number ", test_case)
        print("Calculating the average of col %d, grouped by col %d" % (avg_col, by))
        print(arr)

        # Compute the answer using NumPy
        by_arr = arr[:, by]
        avg_arr = arr[:, avg_col]
        test_ans = dict((k, avg_arr[by_arr==k].mean()) for k in set(by_arr))

        # Convert NumPy array into list of lists
        lst = arr.tolist()
        # Run the solution function
        avgs = avgby(lst, avg_col, by)

        # Compare outputs
        print(OUT, avgs)
        if cmp_dict(avgs, test_ans):
            print(OK)
            task_score += 50 / n_cases
        else:
            print(ERR, 'Expected: ', test_ans)

    # End of test case loop
    total_score += task_score


    print()
    print('####### Task 3: merge #############################################')
    task_score = 0
    if merge([], [], 0, 0) != []:
        print(ERR, "merge([], [],...) should return and empty list")

    # 5 points for merge() not crashing so far.
    task_score = 5 

    # Function to compare your merge with Pandas merge :)
    def check_merged(merged, tbl1, tbl2, left_on, right_on):
        df1 = pd.DataFrame(tbl1)
        df2 = pd.DataFrame(tbl2)
        n1 = len(df1.columns)
        # Make sure we have distinct column names between the to data frames.
        # Column names here are integers starting from 0, add n1 to each of them.
        df2.columns += n1
        # Pandas merge
        dfpd = pd.merge(df1, df2, left_on=left_on, right_on=(right_on+n1))
        # Your answer converted to DataFrame
        dfm = pd.DataFrame(merged)
        print(dfm)
        # Special case of empty merge and 0 length tables.
        if len(dfpd) == 0 and len(merged) == 0:
            return True
        if len(dfpd) == 0 and len(merged) != 0:
            print(ERR, 'Expected empty list as output')
            return False
        if len(merged) == 0:
            print(ERR, 'Got empty table as output. Expected table:')
            print (dfpd)
            return False
        # Sort by all columns to ensure the same order
        dfpd = dfpd.sort_values(by=list(dfpd.columns)) 
        dfm = dfm.sort_values(by=list(dfm.columns))
        # Compare shapes first
        if dfpd.shape != dfm.shape:
            print(ERR, 'Wrong shape, expected table:\n', dfpd)
            return False
        # Compare content
        if not dfpd.equals(dfm):
            print(ERR, 'Correct shape, but not contents. Expected table:\n', dfpd)
        return True

    #### Test cases ####
    print()
    print('Case 1:')
    tbl1 = [['Bob', 'Accounting'], ['Jake', 'Engineering'], ['Lisa', 'HR']]
    tbl2 = [['Lisa', 2004], ['Bob', 2008], ['Jake', 2012], ['Sue', 2014]]
    left_on = 0
    right_on = 0
    merged = merge(tbl1, tbl2, left_on, left_on)

    if check_merged(merged, tbl1, tbl2, left_on, right_on):
        print(OK)
        task_score += 10

    print()
    print('Case 2:')
    tbl1 = [[1, 'A'], [2, 'B'], [3, 'C']]
    tbl2 = [['A', 2004], ['B', 2008], ['C', 2012], ['B', 2014]]
    left_on = 1
    right_on = 0
    merged = merge(tbl1, tbl2, left_on, right_on)
    if check_merged(merged, tbl1, tbl2, left_on, right_on):
        print(OK)
        task_score += 10
 
    print()
    print('Case 3 - empty merge:')
    tbl1 = [[1, 'A']]
    tbl2 = [['B', 2004]]
    left_on = 1
    right_on = 0
    merged = merge(tbl1, tbl2, left_on, right_on)
    if check_merged(merged, tbl1, tbl2, left_on, right_on):
        print(OK)
        task_score += 10

    print()
    print('Case 4:')
    tbl1 = [[1, 'A'], [2, 'A'], [3, 'A']]
    tbl2 = [['A', 2004, True], ['A', 2008, False]]
    left_on = 1
    right_on = 0
    merged = merge(tbl1, tbl2, left_on, right_on)
    if check_merged(merged, tbl1, tbl2, left_on, right_on):
        print(OK)
        task_score += 10

    print()
    print('Case 5:')
    tbl1 = [[1, 'A'], [2, 'A'], [3, 'A']]
    tbl2 = [['A', 2004, 1], ['A', 2008, 2]]
    left_on = 0
    right_on = 2
    merged = merge(tbl1, tbl2, left_on, right_on)
    if check_merged(merged, tbl1, tbl2, left_on, right_on):
        print(OK)
        task_score += 10


    total_score += task_score

    ### Estimated total score
    print('ESTIMATED SCORE: %d (if above 100 will be set to 100)' % total_score)
