import zipfile


def extractArchive(archivePath, destinationDirectory):
    with zipfile.ZipFile(archivePath, 'r') as archive:
        archive.extractall(destinationDirectory)


if __name__ == '__main__':
    extractArchive("D:\\Source Codes\\Python\\Udemy\\App-1\\Bonus\\subfiles\\compressed.zip",
                   "D:\\Source Codes\\Python\\Udemy\\App-1\\Bonus\\subfiles")
