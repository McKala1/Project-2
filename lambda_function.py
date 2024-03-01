import pickle
import json
import logging
import pandas as pd
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_slot_value(slots, slot_name, default_value):
    if slot_name in slots:
        if slots[slot_name] == None:
            return default_value
        else:
            return slots[slot_name]['value']['interpretedValue']
    else:
        raise("Slot Name Incorrect")

def loadmodel():
    return pickle.load(open(filename,'rb'))

def convertcolor(color):
    match color:
        case 'White':
            return 'w'
        case 'Brown':
            return 'n'
        case "Buff":
            return 'b'
        case "Cinnamon":
            return 'c'
        case "Gray":
            return 'g'
        case "Orange":
            return 'o'
        case "Pink":
            return 'p'

def convertsporeprint(sporeprintcolor):
    match sporeprintcolor:
        case 'Black':
            return 'k'
        case 'Brown':
            return 'n'
        case "Buff":
            return 'b'
        case "Chocolate":
            return 'h'
        case "Green":
            return 'r'
        case "Orange":
            return 'o'
        case "Purple"
            return 'u'
        case "White"
            return 'w'
        case "Yellow"
            return 'y'

def convertodor(odor):
    match odor:
           case 'Almond':
            return 'a'
    case 'Anise':
        return 'I'
        case "Creosote":
            return 'c'
        case "Fishy":
            return 'y'
        case "Foul":
            return 'f'
        case "Musty":
            return 'm'
        case "None"
            return 'n'
        case "Pungent"
            return 'p'
        case "Spicy"
            return 's'
def convertstalkcolor(color):
    match color:
        case 'Brown'
            return n 
        case 'Buff' 
            return b 
        case 'Cinnamon' 
            return c 
        case 'Gray'
            return g 
        case 'Orange' 
            return o 
        case 'Pink' 
            return p 
        case 'Red' 
            return e      
        case 'White' 
            return w 
        case 'Yellow' 
            return y 
def convertstalksurface(surface):
    match surface:
        case 'Fibrous' 
            return f 
        case 'Grooves' 
            return g 
        case 'Scaly' 
            return y
        case 'Smooth' 
            return s 
def convertstalkroot(shape):
    match shape:
        case 'Bulbous'
            return b 
        case 'Club' 
            return c 
        case 'Cup' 
            return u 
        case 'Equal' 
            return e     
        case 'Rhizomorphs' 
            return z 
        case 'Rooted' 
            return r 
def convertcapsurface(surface):
    match surface:
        case 'Fibrous' 
            return f 
        case 'Grooves' 
            return g 
        case 'Scaly' 
            return y
        case 'Smooth' 
            return s 
def convertbruises(status):
    match status:
        case 'Yes'
            return t 
        case 'No' 
            return f 
def convertring(number):
    match number:
        case 'None':
            return n
        case 'One':
            return o
        case 'Two':
            return t
def convertcapshape(shape):
    match shape:
        case 'Bell'
            return b
        case 'Conical'
            return c
        case 'Convex'
            return x
        case 'Flat'
            return f
        case 'Knobbed'
            return k 
        case 'Sunken'
            return s 
def convertgill(size):
    match size: 
        case 'Broad':
            return b
        case 'Narrow':
            return n



def identify_a_mushroom(intent_request):
    """
    Performs dialog management and fulfillment for identifying a mushroom
    """
    # Log the entire intent request
    logging.debug(f"Intent:\n{intent_request}")
    session = intent_request['sessionState']
    intent = session['intent']
    slots = intent['slots']
    # Log the slot values
    logging.debug(f'Slots: {slots}')

    
    gillsize=get_slot_value(slots,'gillsize',"none")
    ring=get_slot_value(slots,'ring',"none")
    stalksurfacebelowring=get_slot_value(slots,'StalkSurfaceBelowRing',"none")
    bruises=get_slot_value(slots,'Bruises',"none")
    stalkrootshape=get_slot_value(slots,'StalkRootShape',"none")
    sporeprintcolor=get_slot_value(slots,'SporePrintColor',"none")
    capsurface=get_slot_value(slots,'CapShape',"none")
    capshape=get_slot_value(slots,'CapShape',"none")
    odor=get_slot_value(slots,'Odor',"none")
    stalksurfaceabovering=get_slot_value(slots,'StalkSurfaceAboveRing',"none")

    confidence=0
    mushroomType="unknown"
    temp=[{"Odor_"+ odor:1,"Spore-Print-Color_"+sporeprintcolor:1,"Stalk-Root-Shape_"+stalkrootshape:1,"Stalk-Surface-Below-The-Ring_"+stalksurfacebelowring:1,"ring-number_"+ring:1, "cap-shape_"+capshape:1,"gill-size_"+gillsize:1,"bruises_"+bruises:1  
}]
    X=pd.DataFrame(temp)
    
    





    model=loadmodel()
    ypred=model.predict(X)
    
    intent['state'] = 'Fulfilled'
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'Close'
            },
            'intent': intent
        },
        'requestAttributes': {},
        'messages': [
            {
                'contentType': 'PlainText',
                'content': f"I'm {confidence}% confident that that mushroom is probably a {mushroomType}."
            }
        ]
    }

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    logger.debug(f'Intent Request {intent_request}')
    intent_name = intent_request['sessionState']['intent']['name']
    # Dispatch to your bot's intent handlers
    if intent_name == 'To-Identify-A-Mushroom':
        return identify_a_mushroom(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')

def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    return dispatch(event)

    response = {
        "sessionAttributes": event["sessionState"]["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "You said: " + message
            }
        }
    }
    return response
