class SettingEnvNotFound(Exception):
    
    def __init__(self, *args: object):
        ErrorMessage = 'Enviroment variables not found please check AWS_S3_BUCKET_NAME, AWS_ENDPOINT_URL, AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID'
        super().__init__(ErrorMessage,*args)
        
class UnitTestFailed(Exception):
    
    def __init__(self, *args: object):
        ErrorMessage = 'Unit Test Failed!'
        super().__init__(ErrorMessage,*args)