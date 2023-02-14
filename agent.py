import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

try:
    print("Azure Queue storage - Python quickstart sample")
    # Quickstart code goes here
except Exception as ex:
    print('Exception:')
    print(ex)