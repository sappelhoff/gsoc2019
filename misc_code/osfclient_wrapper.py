"""Wrap osfclient and upload a folder one file at a time.

osfclient tends to take very long for recursive updates and has an unpredictable
behavior that sometimes leads to missing files on the OSF server. This simple
script takes a directory to be uploaded `UPLOAD_DIR` and an OSF password
`OSF_PW` to upload a folder recursively.

It is expected that you ran `osf init` in the same working directory where you
are going to start this script from.

If you need to interrupt your script or it stopped with an error, simply note the
number from the log, and update `progress_counter_min` to that number, so your 
script will start again from where it left off.

"""
import os
import os.path as op
import time
import subprocess

# Definitions
UPLOAD_DIR = './MNE-somato-data'  # rel path to the data directory you want to upload
OSF_PW = ''  # put your OSF password here
progress_counter_min = 0  # Set this to where the script last broke down, or 0

# Setup (do not change)
path = op.abspath(UPLOAD_DIR)
assert op.isdir(path)
os.environ['OSF_PASSWORD'] = OSF_PW

# Start uploading
progress_counter = 0
for root, dirs, files in os.walk(path):

    for file in files:
        # Skip, if script broke down earlier and we want to continue there
        if progress_counter < progress_counter_min:
            progress_counter += 1
            continue

        # Get local file path and remote location
        fname_local = op.join(root, file)
        flocation_remote = '.' + fname_local.replace(path, '')

        # upload the file using a subprocess call
        cmd = ['osf', 'upload',
               '{}'.format(fname_local),
               '{}'.format(flocation_remote),
               ]
        print(' '.join(cmd))
        subprocess.run(cmd, check=True)

        # how much have we progressed?
        progress_counter += 1
        print(progress_counter)
        time.sleep(1)  # wait a bit
