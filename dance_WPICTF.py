#!/usr/bin/env python
import base64, string
flag = "E1KSn2SSktOcG2AeV3WdUQAoj24fm19xVGmomMSoH3SuHEAuG2WxHDuSIF5wIGW9MZx="
upper = string.ascii_uppercase
print upper
lower = string.ascii_lowercase
print lower
for key in range(1, 26):
    shift = string.maketrans(
        upper + lower,
        upper[key:] + upper[:key] + lower[key:] + lower[:key])
    # ham nay lam gi
    print shift
    a = string.translate(flag,shift)
    # print a
    print key, base64.b64decode(a)

# decode caesar cipher