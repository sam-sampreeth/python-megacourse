contents = ['daaaaaaaamn content for 1st file',
            'daaaaaaaamn content for 2nd file',
            'daaaaaaaamn content for 3rd file']

filenames = ['f1.txt', 'f2.txt', 'f3.txt']
for content, filename in zip(contents, filenames):
    file = open(f"subfiles/{filename}", 'w')
    file.write(content)
    print()
