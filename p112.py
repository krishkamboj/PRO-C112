import os
import shutil

source="C:/Users/asus/Downloads"
destination="C:/Users/asus/OneDrive/123_abc"

files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1=source + "/" + i
        path2=destination  + "/" + "documentfile"
        path3=destination  + "/" + "documentfile" + "/" + i

        if os.path.exists(path2):
            print("Moving")

            shutil.move(path1,path3)
        else:

             os.makedirs(path2)
             print("Moving")

             shutil.move(path1,path3)

                  
   