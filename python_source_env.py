import os, subprocess as sp


def python_execute(cmd):
    proc = sp.Popen(cmd, stdout=sp.PIPE, shell=True)
    output, err = proc.communicate() 
#     print "status = ",proc.wait()
#     print "output = ", output
    p_status = proc.wait()
    return p_status, output, err

def updateEnv(sourcerc):
    if (not os.path.isfile(sourcerc)):
        print "Could not find source file '%s' Exiting!" % sourcerc
        return 0
    try:
        newenv = {}
#         print "filename is _%s_" %sourcerc
        cmd = ". "+sourcerc+"; env"
        fd = os.popen(cmd)
#         with open(sourcerc, 'r') as fd:
#         print "opened file ",sourcerc
        for line in fd:
#             print "line is ", line
            # check if line is NOT empty
            if line.strip():
                try:
                    k, v = line.strip("\n").split('=', 1)
                    #print k, " = ", v
                    newenv[k] = v  # print line
#                         os.environ[k] = v.strip()
                except:
                    print "Error while reading source file ", sourcerc, " at line: ", line
                    return 0
        os.environ.update(newenv)
        fd.close()
        print "Sourced file ", sourcerc
        return 1
    except IOError as e:
        print "Error: %s not found.\n Stack trace: %s" % (sourcerc, e)
        return 0


if __name__ == '__main__':
    res = updateEnv("/root/adminrc")
    if res:
      print "Enviroment set Successfull"
      status, output, error = python_execute("date")
      print "Date is %s", %output.
    else:
      print "Environment setting was unsuccessfull"
