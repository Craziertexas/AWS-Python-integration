import os
import base64
import requests
import boto3
from dotenv import load_dotenv
from exeptions import SettingEnvNotFound

class Bucket():
    
    def __init__(self):
        load_dotenv()
        self.BucketName = os.environ.get('AWS_S3_BUCKET_NAME', None)
        self.EndPointURL = os.environ.get('AWS_ENDPOINT_URL', None)
        self.AccessKey = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
        self.AccessKeyID = os.environ.get('AWS_ACCESS_KEY_ID', None)
        
        if not(self.BucketName and self.EndPointURL and self.AccessKey and self.AccessKeyID): 
            raise SettingEnvNotFound()
        
        self.Client = self.InitClient()
    
    def InitClient(self):
        return boto3.client(
            's3',
            aws_access_key_id = self.AccessKeyID,
            aws_secret_access_key = self.AccessKey
        )
        
    def GetItemURL(self, FileName: str, ExpiresIn: int):
        return self.Client.generate_presigned_url(
            ClientMethod='get_object', 
            Params={'Bucket': self.BucketName, 'Key': FileName},
            ExpiresIn=ExpiresIn
        )
    
    def UploadItem(self, Base64File, FileName: str, Metadata_:dict = {}):
        try:
            DecodedFile = base64.b64decode(Base64File)
        except Exception:
            DecodedFile = Base64File
        return self.Client.put_object(Body=DecodedFile, Bucket=self.BucketName, Key=FileName, Metadata=Metadata_)
    
    def DownloadItem(self, FileName:str):
        response = requests.get(self.GetItemURL(FileName, 8600), stream=True)
        return response.content
