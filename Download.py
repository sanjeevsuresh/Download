import urllib.request
import re
import os
import sys
from bs4 import BeautifulSoup

def createFolder(folderName):
    try:
        os.makedirs(folderName)
    except FileExistsError:
        print("Folder already exists")

def handler(signalNum,  frame):
    raise KeyboardInterrupt


def raw_input_with_timeout(prompt, timeout=5):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    astring = None
    try:
        # timer.start()
        astring = input(prompt)
    except KeyboardInterrupt:
        print("\nTimedOut!")
    # timer.cancel()
    signal.alarm(0)
    return astring


def ask(prompt,  timeout):
    answer = raw_input_with_timeout(prompt, timeout)
    return answer

def askForExtensions():
    inputExtensions = input("Enter any extensions I should look for: ")
    inputExtensions = re.split('\W+', inputExtensions)
    otherExtensions = "checkIfUserIsDone"
    while(otherExtensions not in ["n", "no", ""]):
        otherExtensions = input("Any others? [Enter them or Respond (n/no)]: ")
        if(otherExtensions not in ["n", "no", ""]):
            extras = re.split('\W+', otherExtensions)
            inputExtensions.extend(extras)
    return correctIssues(inputExtensions)


def correctIssues(userDefinedExtensions):
    requestedExtensions = "These are the extensions I'm looking for:\n{0}"
    requestedExtensions = requestedExtensions.format(userDefinedExtensions)
    print(requestedExtensions)
    issues = input("Any issues? (y/n): ")
    if issues in ['y', 'yes']:
        print("Restarting...")
        return askForExtensions()
    return userDefinedExtensions

def parodyBrowser(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML,  like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1, utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US, en;q=0.8', 'Connection': 'keep-alive'}
    req = urllib.request.Request(url, headers=hdr)
    return req


def main():
    suggestedPage = input("Please enter the url of an online directory: ")
    aFolder = input("Please enter in a folder name to save your files...\n" +
                    "(you can create a subdirectory e.g. hw8/list) --> ")
    webpageRequest = parodyBrowser(suggestedPage)
    htmlPageResponse = urllib.request.urlopen(webpageRequest)
    '''htmlByteObj = htmlPageResponse.read()
    htmlText = htmlByteObj.__repr__()'''
    #print(htmlText)
    inputExtensions = askForExtensions()
    createFolder(aFolder)
    print("Type of parameter for BeautifulSoup {0}".format(type(htmlPageResponse)))
    print("Status: {0} {1}".format(htmlPageResponse.status, htmlPageResponse.reason))
    soup = BeautifulSoup(htmlPageResponse)
    files = list()
    allTags = soup.find_all("a")
    allImages = soup.find_all("img")
    print("All anchors:\n{0}".format(allTags))
    print("All images:\n{0}".format(allImages))
    for tag in allTags:
        possibleFile = tag.get('href')
        print(possibleFile)
        extensions = possibleFile.split(".")
        extension = extensions[len(extensions) - 1]
        if extension in inputExtensions:
            files.append(possibleFile)
    print("\n\nThese are the files I found:\n{0} \n".format(files))
    for count, foundFile in enumerate(files):
        # print(suggestedPage)
        link = suggestedPage + foundFile
        try:
            print("Trying: " + link)
            saveDestination = "{0}/{1}".format(aFolder, foundFile)
            urllib.request.urlretrieve(link, saveDestination)
            print("Succeeded")
        except Exception as e:
            print(e)
    return
main()
