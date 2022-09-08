import sys

program = 'argv_demo.py'
source = 'default.src'
dest = 'default.dest'

def show_config():
    print(' Here is the current configuration')
    print('Program: %s' % program)
    print('source: %s' % source)
    print('Destination: %s' % dest)

if_name_ == '_main_' :
    import sys
    print('Here is sys.argv: %s' % sys.argv)
    if len(sys.argv) >2: # Two or more args passed
        program, source, dest = sys.argv[ : 3]
    elif len(sys.argv) >1: # Only one arg passed
        program, source = sys.argv[ : 2]
    else: # No args passed
        program = sys.argv[0]
    show_config()
    

