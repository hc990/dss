'''
Created on 2013-3-21

@author: huangchong
'''


def main():
    s = []
    with open('/var/log/firewall/log.log') as f:
        for a in f:
            s.append(a)
    print s
    
if __name__ == '__main__':
    main() 