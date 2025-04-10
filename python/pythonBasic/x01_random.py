#!/usr/bin/env python

import random
from x02_max_def import max

data = random.sample(range(1,101),10)
print(data)

print(f"Max value is {max(data)}")
