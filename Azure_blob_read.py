pip install azure-storage-blob --upgrade
from azure.storage.blob import BlockBlobService

block_blob_service = BlockBlobService(account_name='pmcovidstorage', account_key='4Ufd30qimeVHKioZcFzZx33PF+4MbrmT0/AwOEZTqDE6zZ6RDuZnmRjrgU52Gl6bIBLLM35dZcC+A1Gi3cCl/w==')

print("Retreiving blobs in specified container...")

blob_list=[]

container="coviddatasetsblobcontainer"

def list_blobs(container):

        try:



                global blob_list

                content = block_blob_service.list_blobs(container)

                print("******Blobs currently in the container:**********")

                for blob in content:

                        blob_list.append(blob.name)

                        print(blob.name)

        except:

                print("The specified container does not exist, Please check the container name or if it exists.")

list_blobs(container)

print("The list() is:")

print(blob_list)
block_blob_service.get_blob_to_path('coviddatasetsblobcontainer','ourworldin.full_data.csv','ourworldin.full_data.csv')
import pandas as pd 
dataframe_blobdata = pd.read_csv('ourworldin.full_data.csv')
dataframe_blobdata.head(10)
