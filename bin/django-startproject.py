#!/usr/bin/env python

try:
    import django_startproject
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

def main():
    from django_startproject.management import start_project
    start_project()


if __name__ == '__main__':
    main()
