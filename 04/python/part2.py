#!/usr/bin/env python

import hashlib
import re

key = "ckczppom"

pattern = re.compile("^0{6}")

index = 1

while (not pattern.match(hashlib.md5((key + str(index)).encode("utf-8")).hexdigest())):
    index += 1

print("Secret key is", index)
