#! /usr/bin/ENV python


# cribbed heavily from: https://github.com/socialplanning/fassembler/blob/master/fassembler/create-venv-script.py


import  os
import subprocess
import virtualenv

here = os.path.abspath(__file__)
base_dir = os.path.dirname(here)
script_name = os.path.join(base_dir, '.wto_scraper_bootstrap.py')


EXTRA_TEXT="""
def adjust_options(options, args):
    if not args:
        args=['.']
        # return # caller will raise error
    
    base_dir = os.path.abspath('.')
    args[0] = join(base_dir, 'venv')

# def after_install(options, home_dir):
#     pip = os.path.join(home_dir, 'bin', 'pip')
#     subprocess.call([pip, 'install', '-r', os.path.join(os.path.abspath('.'),'requirements.txt')])

"""



def main():
    text = virtualenv.create_bootstrap_script(EXTRA_TEXT)
    if os.path.exists(script_name):
        f = open(script_name)
        cur_text = f.read()
        f.close()
    else:
        cur_text = ''
    print 'Updating %s' % script_name
    if cur_text == 'text':
        print 'No update'
    else:
        print 'Script changed; updating...'
        f = open(script_name, 'w')
        f.write(text)
        f.close()

if __name__ == '__main__':
    main()
