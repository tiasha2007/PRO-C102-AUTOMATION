import cv2
import time
import random
import dropbox

start_time = time()

def take_snapshot():
    num = random(0,100)
    #video capture object from cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
        return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.A-wTpDNKEm1rOnbht-3hWjzfgsaj6MPHj86PObw7kLNFMzPEgWuDdC8QVA--Hp9jFO5xUC0MFnUARU0O2G86FxfQTL5XeMJDy30Nyx1f3r3OKJGeTtnJamEHWbZ4QVCa4xcVsdO2GF4"
    file = img_name
    file_from = file
    file_to = "/photos/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()