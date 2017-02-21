#!/usr/bin/env python

import csv
import sys
import md5

# making sure that there are two arguements
# [csv file with passwords, filename to write to]
if len(sys.argv) != 2:
    print("failed")
    exit(2)

# opening the first file to parsing
with open(sys.argv[1], 'r') as passwords:

    # opening the second file for writing to
    with open(sys.argv[2], 'wb') as hashes:

        # reading from the first file with the password hashes
        writer = csv.writer(hashes, delimiter=' ')

        # writing to the second file after md5 hashing it
        # to make it easy to crack the password
        for line in passwords:
            hashed = md5.new(str(line.strip())).hexdigest()
            writer.writerow([line.strip(), hashed])
