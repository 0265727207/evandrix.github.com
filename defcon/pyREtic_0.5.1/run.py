#!/usr/bin/env python

import sys
import os
import REpdb
import lazy_test

sys.path.append(os.path.join(".", "pyREtic"))
REpdb.set_trace()
REpdb.obj_mirror(lazy_test)
