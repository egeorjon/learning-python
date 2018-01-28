# With glob:
# ---------------------
import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)or simply os.listdir:import os

# With os
# ---------------------
for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))or if you want to traverse directory, use os.walk:import os

# with os.walk
# For the current directory, and all subdirectories
# ---------------------
for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
