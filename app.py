import subprocess

#Getting necessary inputs to generate command
url = input("Enter the URL: ")
filename = input("Enter the filename: ")

#build command with user inputs
#command = f'streamlink -o {filename}.mp4 {url} best '
command = f'streamlink --http-header User-Agent="Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25" --http-header Origin=https://iframe.mediadelivery.net "hls://{url} best -o {filename}.ts'

print('Generated command: ' + command)

#open shell and run generated command
subprocess.run(command, shell=True)