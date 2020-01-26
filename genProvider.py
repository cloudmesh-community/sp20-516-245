from subprocess import check_output
import sys
import re

#Small script for auto-generating provider functionality from help command

data = check_output(["multipass", "help"]).decode(sys.stdout.encoding)
options = data.split("Available commands:")[1].strip()
command_info = re.split("\s{2,}", options)

commands = [c for c in command_info if " " not in c] 

with open("providerBody.py", 'w') as f:
    for command in commands:
        f_body = f"""
    def {command}(self):
        os.system("multipass {command}")
        """

        f.write(f_body)
