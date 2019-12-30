#!C:\Apython\student_sys\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pandoradep==0.3.0','console_scripts','pandoradep'
__requires__ = 'pandoradep==0.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pandoradep==0.3.0', 'console_scripts', 'pandoradep')()
    )
