from bucket import Bucket
import tkinter as tk
import io
from tkinter import filedialog


if __name__ == "__main__": 
    root = tk.Tk()
    root.withdraw()

    MyBucket = Bucket()
    FilePath = filedialog.askopenfilename()
    FileName = FilePath.split("/")[-1]

    File = io.FileIO(FilePath)
    UploadResult = MyBucket.UploadItem(File, FileName)
        
    print(f"File URL {MyBucket.GetItemURL(FileName, 8600)}")