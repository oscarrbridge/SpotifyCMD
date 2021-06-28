import sys
import subprocess
from start import *

import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages])

new_list = []
found_package = []

for package in range(len(installed_packages_list)):
    new_list.append(installed_packages_list[package].split("=="))

    if new_list[package][0] == "spotipy":
        found_package.append(True)

if found_package[0] is True:
    print("Required packages found...")

else:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'spotipy'])

setup()
