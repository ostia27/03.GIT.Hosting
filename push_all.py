import subprocess
import argparse

parser = argparse.ArgumentParser(prog='Push all')
parser.add_argument('branch')
args = parser.parse_args()

for remote in subprocess.run(["git", "remote"], capture_output=True).stdout.decode().split('\n')[:-1]:
   print(f'Return code: {subprocess.run(["git", "push", remote, args.branch]).returncode}')

print('All changes pushed')