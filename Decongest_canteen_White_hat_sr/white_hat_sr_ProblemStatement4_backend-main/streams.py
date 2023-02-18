import pymongo
import datetime

SERVER_URL = 'mongodb+srv://shreyas22010793:A1Hn12yTvIvx21fw@cluster0.8dvqlye.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(SERVER_URL)
db = client.test2DB


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def get_new_order(time_quantum):
    """ Blocking call to check for new orders """
    
    cursor = db["order"].watch()
    order_document = next(cursor)
    if('fullDocument' in order_document): #Implies that a new order has been added

            order_document =  order_document['fullDocument']
            del order_document["_id"] #cannot be serialized, hence removed
            order_document["from"] = json_serial(order_document["from"])
            order_document["to"] = json_serial(order_document["to"])
            #now = datetime.datetime.now()
            #if(order_document["from"] >= now and order_document["to"] <= (now+datetime.timedelta(hours=time_quantum))): #change this, remove the right condition
            return order_document

    else:

        return None



def get_order_update(order_id: int):
    """ Blocking call to get order updates """
    
    cursor = db["order"].watch()
    order_document = next(cursor)

    if('updateDescription' in order_document): #Implies that a new order has been added

            return order_document['updateDescription']['updatedFields']
    else:

        return None
