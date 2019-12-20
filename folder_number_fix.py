import os
import shutil


euler_url = 'https://projecteuler.net/problem='
repo_dir = '/Users/doboyle/code/Project-Euler'

for x in xrange(1, 10):

    problem_folder = os.path.join(repo_dir, 'Problem' + '0' + str(x))

    if os.access(problem_folder, os.F_OK):
        new_folder = os.path.join(repo_dir, 'Problem' + '00' + str(x))
        shutil.move(problem_folder, new_folder)
