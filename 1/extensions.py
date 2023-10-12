def main():
    filename = input("What is the name of the file?").lower()

    extension_type = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    extension = filename[filename.rfind('.'):].lower()

    if extension in extension_type:
        print(extension_type[extension])
    else:
        print("application/octet-stream")

main()





