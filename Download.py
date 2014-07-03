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


def main():
    suggestedPage = input("Please enter the url of an online directory: ")
    aFolder = input("Please enter in a folder name to save your files...\n" +
                    "(you can create a subdirectory e.g. hw8/list) --> ")
    webpage = urllib.request.urlopen(suggestedPage)
    htmlByteObj = webpage.read()
    htmlText = htmlByteObj.__repr__()
    # print(htmlText)
    inputExtensions = askForExtensions()
    createFolder(aFolder)
    htmlPageSource = urllib.request.urlopen(suggestedPage)
    print(type(htmlPageSource))
    soup = BeautifulSoup(htmlPageSource)
    files = list()
    allTags = soup.findAll('a')
    for tag in allTags:
        possibleFile = tag.get('href')
        # print(possibleFile)
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
