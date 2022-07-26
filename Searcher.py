import urllib.request
import re
import webbrowser

keyword= input("Enter a word: ")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + keyword.replace(" ", "+"))
video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
firsturl = 'https://www.youtube.com/watch?v=' + video_id[0]
secondurl = 'https://www.youtube.com/watch?v=' + video_id[1]
thirdurl = 'https://www.youtube.com/watch?v=' + video_id[2]
fourthurl = 'https://www.youtube.com/watch?v=' + video_id[3]
fifthurl = 'https://www.youtube.com/watch?v=' + video_id[4]

print("1:")
print(firsturl)

print("2:")
print(secondurl)

print("3:")
print(thirdurl)

print("4:")
print(fourthurl)

print("5:")
print(fifthurl)
question1 = input("Do you want to open? (1 = Yes, 2 = No): ")

if question1=="1":
    choosingalink = input("Choose a link: ")
    if choosingalink=="1":
        webbrowser.open(firsturl)
    if choosingalink=="2":
        webbrowser.open(secondurl)
    if choosingalink=="3":
        webbrowser.open(thirdurl)
    if choosingalink=="4":
        webbrowser.open(fourthurl)
    if choosingalink=="5":
        webbrowser.open(fifthurl)
if question1=="2":
    print("Closing...")
    exit()