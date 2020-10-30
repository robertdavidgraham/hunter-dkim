#!/usr/bin/env python3
# Command-line tool to use hardcoded public-key instead of DNS query
# from https://gist.githubusercontent.com/stevecheckoway/51e63d4c269bd2be4a50a3b39645a77c/raw/4ed815490f4c619a5ba47dcd01d50aa32ee2cf55/verify.py
# written by Stephen Checkoway @stevecheckoway
# do 'pip install dkimpy' first to get 'dkim' dependency

from dkim import DKIM
import sys

def get_txt(*args, **kwargs):
    return b'k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1Kd87/UeJjenpabgbFwh+eBCsSTrqmwIYYvywlbhbqoo2DymndFkbjOVIPIldNs/m40KF+yzMn1skyoxcTUGCQs8g3FgD2Ap3ZB5DekAo5wMmk4wimDO+U8QzI3SD0" "7y2+07wlNWwIt8svnxgdxGkVbbhzY8i+RQ9DpSVpPbF7ykQxtKXkv/ahW3KjViiAH+ghvvIhkx4xYSIc9oSwVmAl5OctMEeWUwg8Istjqz8BZeTWbf41fbNhte7Y+YqZOwq1Sd0DbvYAD9NOZK9vlfuac0598HY+vtSBczUiKERHv1yRbcaQtZFh5wtiRrN04BLUTD21MycBX5jYchHjPY/wIDAQAB'

failed = False

for path in sys.argv[1:]:
    with open(path, 'rb') as f:
        verifier = DKIM(message=f.read())

    if verifier.verify(0, dnsfunc=get_txt):
        print("{}: DKIM signature verified".format(path))
    else:
        print("{}: DKIM signature verification failed".format(path))
        failed = True
if failed:
    sys.exit(1)
