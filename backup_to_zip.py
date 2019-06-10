import os, zipfile

def backupToZip(f):
    folder = os.path.abspath(f)
    cnt = 1
    while 1:
        zipName = os.path.basename(folder) + '_' + str(cnt) + '.zip'
        print(zipName)
        if not os.path.exists(zipName):
            break
        cnt += 1
    print("Creating zip : %s", zipName)
    bckZip = zipfile.ZipFile(zipName, "w")

    for folder_nm, sub_nm, file_nm in os.walk(folder):
        bckZip.write(folder_nm)
        for f in file_nm:
            if f.endswith('.zip'):
                continue
            bckZip.write(os.path.join(folder_nm, f))
    bckZip.close()

backupToZip(os.path.dirname(os.path.realpath(__file__)))