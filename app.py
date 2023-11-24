import subprocess

#Getting necessary inputs to generate command
url = input("Enter the URL: ")
filename = input("Enter the filename: ")

#build command with user inputs
command = f'streamlink -o {filename}.mp4 {url} best '
print('Generated command: ' + command)

#open shell and run generated command
subprocess.run(command, shell=True)
