#!/usr/bin/python
import sys

def generate_tag( ref, xml=False ):
	ref_name, match = ref
	return "<link rel='"+ ["mismatch","match"][match] + "' href='" + ref_name + "'"+ [">"," />"][xml]

def find_refs(reftest_list):
	tests = {}
	for entry in reftest_list:
		if entry.strip() == '':
			continue
		split_entry = entry.split()
		if "#" in split_entry[0]:
			continue
		name = split_entry[1]
		ref = split_entry[2]
		match = split_entry[0] == '=='
		tests.setdefault(name,[]).append( (ref, match))
	return tests

if len(sys.argv) != 2:
	print "Error: this script should be called with a path as argument"
	exit(1)

path = sys.argv[1].replace("reftest.list","")

print "processing: " +  path
entries= [line.strip() for line in open(path + 'reftest.list')]
tests= find_refs(entries)

for test in tests:
	xml = False
	if 'XHTML' in open(path + test).read():
		xml = True
	f = open(path + test, "r")
	contents = f.readlines()
	f.close()

	for i, j in enumerate(contents):
		if j.strip() == '<style>':
			contents.insert(i, "\n".join(map(lambda t: generate_tag(t,xml), tests[test])) + "\n")
			break
	f = open(path + test, "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()

