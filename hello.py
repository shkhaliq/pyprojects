import subprocess
import sys
x=subprocess.call('git --version',shell=True)
sys.exit(x)
