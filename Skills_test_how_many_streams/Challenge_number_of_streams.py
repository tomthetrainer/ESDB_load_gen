from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package
import hashlib

#######################################################
#
# Step 1. Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

##########################################
#
# Step 2. Read all events from the stream
#
##########################################


# YOUR CODE HERE
# If you are not sure how to start read hint.txt





client.close()