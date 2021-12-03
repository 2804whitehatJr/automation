import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
     #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #Read the frame while the camera is on
        ret, frame=videoCaptureObject.read()
        #cv2.imwrite(). This method is used to save an image to any storage device.
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    #Release the camera
    videoCaptureObject.release()
    #closes all the window which might be open during all the process
    cv2.destroyAllWindows()


def uploadFile(image_name):
    access_token='DcHVIGCTk_8AAAAAAAAAAbQIDwHY9N-4XhUK0pZXICfPFWd3NRIPufHfGhDhl776e'
    file=image_name
    file_from= file
    file_to= '/newFolder/' + image_name
    dbx= dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
            print("FILE UPLOADED")


def main():
     while (True):
         if((time.time()-startTime)>=5):
             name=takeSnapshot()
             uploadFile(name)

main()

    





