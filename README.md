reftest-converter
=================

This is quick and dirty string to convert old fashioned reflists into link
tags.  No consideration has been given to error handling or efficiency of
execution, as this was written for a one-off operation whose result would be
checked manually. Nonetheless, if people find this useful, improvement
suggestions are most welcome.

Usage:
find . -name reftest.list -exec utils/ref-conv.py {} \;
