import os

def delete_un(ip, t):
    for folders, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            size = os.path.getsize(os.path.join(folders, filename))
            if size > int(threshold)*(10**6):
                print(filename,'-Size =  %s' %(size // 10 ** 6), 'MB' '-Path= ', os.path.join(folders, filename))
if __name__ == "__main__":
    folder = str(input("Absolute path:"))
    threshold = int(input("Max file size to ignore:"))
    delete_un(folder, threshold)