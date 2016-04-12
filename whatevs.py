import sys,re

def main():
    fh = open(sys.argv[1],'r')
    lines = fh.readlines()
    print '\tpython2.2 -c "`printf \\"if 1:\\n\\'
    for line in lines:
        line = re.sub('[\\\'\"()]','\\\g<0>',line)
        # grab leading white space (should be multiples of 4) and makes them into
        # tabs
        wh_spc_len = len(re.match('\s*',line).group())

        sys.stdout.write('\t')
        sys.stdout.write(wh_spc_len/4*'\\t'+line.rstrip().lstrip())
        sys.stdout.write('\\n\\\n')
    print '\t\\"`"'
    print 3

if __name__=='__main__':
    main()
