import re
import requests


# Edit URL Link to the RSS Feed Link at the bottom of the matches tab on TBA
# Copy the link that of the button named "Matches in RSS" and should look like this https://www.thebluealliance.com/event/*0000XXXX*/feed

url = 'https://www.thebluealliance.com/event/2023new/feed'

response = requests.get(url)

if response.status_code == 200:
    rss_entry = response.text
else:
    print("URL Invalid or no matches posted")
    exit
# Extract the teams using regular expressions
red_teams = re.findall(r'<li>(\d+)</li>', re.search(r'Red Alliance: -1(.+?)Blue Alliance:', rss_entry, re.DOTALL).group(1))
blue_teams = re.findall(r'<li>(\d+)</li>', re.search(r'Blue Alliance: -1(.+)', rss_entry, re.DOTALL).group(1))

# Print the teams separated by new line
with open('frc.txt', 'a') as f:
    for i, team in enumerate(red_teams + blue_teams):
        f.write(team + '\n' if (i + 1) % 6 == 0 else team + ' ')

# Print the teams separated by new line, six teams per line
for i, team in enumerate(red_teams + blue_teams):
    print(team)
    if (i + 1) % 6 == 0:
        print('')