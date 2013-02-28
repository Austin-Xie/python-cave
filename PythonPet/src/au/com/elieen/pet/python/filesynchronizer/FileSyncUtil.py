'''
Created on 2012-12-25

@author: Austin
'''

import filecmp
import os
from shutil import *
#from commands import *

ONE_WAY = 1
TWO_WAY = 2

def synchronize(leftDir, rightDir, action, logCallback):
    ld = leftDir.replace("\\", "/")
    rd = rightDir.replace("\\", "/")
    dc = filecmp.dircmp(ld, rd);

    for lo in dc.left_only:
        lf = ld + "/" + lo
        rf = rd + "/" + lo
        copy(lf, rf, logCallback)

    if (action == TWO_WAY):
        for ro in dc.right_only:
            lf = ld + "/" + ro
            rf = rd + "/" + ro
            copy(rf, lf, logCallback)
    else:
        for ro in dc.right_only:
            rof = rd + "/" + ro
            if (ro[0] == "."):
                logCallback("ignored right-only folder '" + rof + "'")
                continue;

            if (os.path.isdir(rof)):
                rmtree(rof)
                logCallback("removed right-only folder '" + rof + "'")
            elif (os.path.isfile(rof)):
                os.remove(rof)
                logCallback("removed right-only file '" + rof + "'")
            elif (os.path.islink(rof)):
                os.remove(rof)
                logCallback("removed right-only file link '" + rof + "'")
                
            logCallback("deleted '" + rof + "'")

    for cf in dc.common_dirs:
        logCallback("to synchronize common folder '" + cf + "' between '" + ld + "' and '" + rd + "'")
        synchronize(ld + "/" + cf, rd + "/" + cf, action, logCallback)
    

def copy(source, target, logCallback):
    if (os.path.isdir(source)):
        copytree(source, target)
        logCallback('copied folder "' + source + '" to "' + target + '"')
    elif (os.path.isfile(source)):
        copyfile(source, target)
        logCallback('copied file "' + source + '" to "' + target + '"')
    elif (os.path.islink(source)):
#        print('link"' + source + '" ignored!')
        logCallback('link"' + source + '" ignored!')
    else:
#        print('"' + source + '" ignored!')
        logCallback('"' + source + '" ignored!')
