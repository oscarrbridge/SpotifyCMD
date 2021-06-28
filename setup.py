import sys
import subprocess
import pkg_resources
import time

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages])

new_list = []
found_package = False

for package in range(len(installed_packages_list)):
    new_list.append(installed_packages_list[package].split("=="))

    if new_list[package][0] == "spotipy":
        found_package = True

if found_package is True:
    print("Required packages found...")

else:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'spotipy'])

input("Press enter to continue")

from start import *

setup()
