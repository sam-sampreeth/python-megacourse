fnames = ['1.doc', '1.report', '1.presentation']

fnames = [fname.replace('.', '-') + '.txt' for fname in fnames]
print(fnames)