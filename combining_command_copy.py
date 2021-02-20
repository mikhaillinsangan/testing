Making this change

import os
os.system("echo Hello from the otherside!")

Im also making this change

#os.system("cd ~")

import subprocess
RunClews = subprocess.Popen(['python3', 'BuildCLEWS_Canada.py', 'CLEWSCanada_Oct3_2020.yaml'])
RunClews.wait()

# otoole_path = input("Enter the absolute path to otoole_output: ")

# os.chdir(otoole_path)
# > otoole convert csv datafile data datafile.txt


# RunOtoole = subprocess.Popen(['python3', 'preprocess_data.py', 'otoole', 'datafile.txt', 'preprocessed_datafile.txt'])
# RunOtoole.wait()

# import subprocess

# Popen(["/Users/mikhaillinsangan/CLEWS_CANADA"])


# result = subprocess.run([sys.executable, "-c", "print('ocean')"])

# home_dir = os.system("cd ~")
# print("`cd ~` ran with exit code %d" % home_dir)
# unknown_dir = os.system("cd doesnotexist")
# print("`cd doesnotexis` ran with exit code %d" % unknown_dir)

# import subprocess

# import subprocess
# list_files = subprocess.run(["ls", "-l"])
# print("The exit code was: %d" % list_files.returncode)



# list_dir = subprocess.Popen(["ls", "-l"])
# list_dir.wait()

# import subprocess

# useless_cat_call = subprocess.run(["cat"], stdout=subprocess.PIPE, text=True, input="Hello from the other side")
# print(useless_cat_call.stdout)  # Hello from the other side

# import subprocess

# failed_command = subprocess.run(["false"], check=True)
# print("The exit code was: %d" % failed_command.returncode)