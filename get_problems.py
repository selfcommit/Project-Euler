import requests
import os
from bs4 import BeautifulSoup

euler_url = 'https://projecteuler.net/problem='
last_problem = 506
repo_dir = '/Users/doboyle/code/Project-Euler'

for x in xrange(1, last_problem):
    r = requests.get(euler_url+str(x))
    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    problem_folder = os.path.join(repo_dir, 'Problem' + str(x))

    if not os.access(problem_folder, os.F_OK):
        os.mkdir(problem_folder)

    problem = soup.find_all(class_='problem_content')

    problem_text = problem[0].text.encode('ascii', 'xmlcharrefreplace')

    readme = open(os.path.join(problem_folder, 'readme.md'), 'w')
    readme.write(problem_text)
    readme.close()
