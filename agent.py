import os, uuid, time
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

#TODO: This should be saved in more secured storage such as environment variable.
CONN_STR = "DefaultEndpointsProtocol=https;AccountName=gafstorageaccount;AccountKey=4e4TLY3fOUzx30s97Wm9YtMQcUcvSKRsP5S+9Do1eHE1f7AQEeD8mTLLUR4F/stf55hOAt053zOJ+AStuRZB4g==;EndpointSuffix=core.windows.net"

try:
    #Queue name should be static so this can be used by pipeline
    queue_name = "gafqueue-329a4ff3-2197-4e61-84e3-adf794c7ffc0"
    print("Connecting Queue: {}".format(queue_name))
    queue_client = QueueClient.from_connection_string(CONN_STR, queue_name)

    # Send several messages to the queue
    queue_client.send_message(u"First message")
    queue_client.send_message(u"Second message")
    saved_message = queue_client.send_message(u"Third message")

    #Peeking message, This should prevent to dequeue message
    peeked_messages = queue_client.peek_messages(max_messages=5)
    for peeked_message in peeked_messages:
        print("Message: " + peeked_message.content)
    #Set sleep to see if the queue is reflecting to the portal
    time.sleep(20)

    while True:
        response = queue_client.receive_messages()
        for msg in response:
            print("Dequeueing message: " + msg.content)
            queue_client.delete_message(msg.id, msg.pop_receipt)

except Exception as ex:
    print('Exception:')
    print(ex)
