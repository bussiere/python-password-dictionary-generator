'''
Example code, how to use pwddictlib.py v0.1

'''
import sys

try:
    import pwddictlib
except:
    try:
        sys.path.append('.')
        import pwddictlib
    except:
        sys.exit(2)

def gen_usage():
    p = pwddictlib.PasswordDictionary(string_length=2, char_list='abcdef0123456789')
    for password in p.generator():
        print password
        
def cdl_usage():
    p = pwddictlib.PasswordDictionary(string_length=2, char_list='0123456789')
    for password in p.candle():
        print password     
        
if __name__ == '__main__':
    ## Basic generator
    print 'generator'
    gen_usage()
    print '-' * 60
