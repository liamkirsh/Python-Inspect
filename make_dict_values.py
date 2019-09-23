"""
In this solution, the caller function passes the set of values to the callee
function. Then, the callee function retrieves the callee's last executed line
of code and uses a regular expression to guess the identifiers that were used.


> As I said, I don't recommend using that, nor would I ever use such a hack. 
> Using inspect is IMO always a sign that something is going horrible, horrible
> wrong. I just wanted to show that it's possible... but as we all know, you 
> shouldn't do something JUST because it's possible.
> - Ivo Wetzel May 1 '10 at 12:59
> https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function/2749857#comment2780046_2749857
"""

import inspect
import traceback
import re


def make_dict(*args):
    function_name = inspect.getframeinfo(inspect.currentframe()).function
    code = traceback.extract_stack()[-2][3]   # get line that called me
    regex = re.escape(function_name) + r'\((.*?)\).*$'
    var_names = re.compile(regex).search(code).groups()[0].split(',')
    return dict(zip(var_names, [v for v in args]))


def my_func():
    a,b,c,d=1,2,3,4
    print make_dict(a,b,c,d)
	
my_func()