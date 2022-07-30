import requests
import boto3
import os


class Mixpeek:
    def __init__(self, api_key):
        self.base_url = "https://api.mixpeek.com"
        self.header = {"Authorization":api_key}

    def upload(self, file_name, file_path):
        # build api endpoint url with key and path
        url = f'{self.base_url}/upload'
        # add url params
        params = dict()
        # file upload
        files = [
            ('file', (file_name, open(file_path, 'rb'), 'application/octet-stream'))
        ]
        # send request
        response = requests.request("POST", url, files=files, params=params, headers=self.header)
        #
        return response.json()

    def search(self, query):
        url = f'{self.base_url}/search'
        # add url params
        params = dict()
        params["q"] = query
        # send request
        response = requests.request("GET", url, params=params, headers=self.header)

        return response.json()


class S3:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name, mixpeek_api_key):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.mixpeek = Mixpeek(api_key=mixpeek_api_key)

    def upload_one(self, s3_file_name, bucket_name):
        tmp_file = f'tmp/{s3_file_name}'
        # open in memory
        with open(tmp_file, 'wb') as file:
            self.s3_client.download_fileobj(
                bucket_name,
                s3_file_name,
                file
            )
            try:
                # send to mixpeek
                r = self.mixpeek.upload(file_name=s3_file_name, file_path=tmp_file)
                # print result to console
                print(r)
                # remove from tmp dir
                os.remove(tmp_file)
            except Exception as e:
                print(e)


    def upload_all(self, bucket_name):
        # bucket
        objects = self.s3_client.list_objects(Bucket=bucket_name)
        # go through each object within bucket
        for obj in objects['Contents']:
            # this is the file object
            s3_file_name = obj['Key']
            # tmp filpath
            self.upload_one(s3_file_name=s3_file_name, bucket_name=bucket_name)
