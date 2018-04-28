#!/usr/bin/env python
import base64, string
flag = "ny_nx_tsq3_zumnqq_kwtr_mjwj_6a7559be5e"
upper = string.ascii_uppercase
print upper
lower = string.ascii_lowercase
print lower
for key in range(1, 26):
    shift = string.maketrans(
        upper + lower,
        upper[key:] + upper[:key] + lower[key:] + lower[:key])
    a = string.translate(flag,shift)
    print a, "\n"
    # print key, base64.b64decode(a)

# decode caesar cipher
