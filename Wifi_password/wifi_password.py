import subprocess

# Get the output of netsh command and decode it properly
command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')

# Extract profiles
profiles = [i.split(":")[1][1:-1] for i in command_output.split("\n") if "All User Profile" in i]

# Loop through each profile and extract passwords
for profile in profiles:
    try:
        results_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8')
        results = [b.split(":")[1][1:-1] for b in results_output.split("\n") if "Key Content" in b]

        print("{:<30}| {:<}".format(profile, results[0] if results else ""))
    except subprocess.CalledProcessError:
        print("{:<30}| {:<}".format(profile, "ERROR"))

input("")  # Keep the console open