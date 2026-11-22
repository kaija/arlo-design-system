#!/usr/bin/env python3
"""Regenerate site/ (docs website) and arlo-design/ (AI kit) from project/.

Run from anywhere:  python3 tools/make.py
Both output folders are rebuilt from scratch: don't edit them by hand.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import site_gen, kit_gen, status_lab

site_gen.run()
status_lab.run()
kit_gen.run()
