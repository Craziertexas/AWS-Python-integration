from bucket import Bucket
from exeptions import UnitTestFailed
from time import time

if __name__ == '__main__':
    MyBucket = Bucket()
    FileName = f'MyTextFile_{time()}.txt'
    FilePath = 'TestFile.txt'
    with open(FilePath, 'rb') as TextFile:
        TextFile = TextFile.read()
        UploadResult = MyBucket.UploadItem(TextFile, FileName)
        if not(UploadResult):
            raise UnitTestFailed()
    TestFileURL = MyBucket.DownloadItem(FileName, 8600)
    if not(type(TestFileURL) == str):
        raise UnitTestFailed()
    print(f"Download URL is {TestFileURL}")