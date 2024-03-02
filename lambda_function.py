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
    return pickle.load(open("mymodel.sav",'rb'))

def fix_cap_shape(cap_shape):
    # The cap-shape column has 6 unique values: b, c, f, k, s, x
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be cap-shape_b, cap-shape_c, cap-shape_f, cap-shape_k, cap-shape_s, cap-shape_x
    match cap_shape:
        case "Bell":
            return "cap-shape_b"
        case "Conical":
            return "cap-shape_c"
        case "Flat":
            return "cap-shape_f"
        case "Knobbed":
            return "cap-shape_k"
        case "Sunken":
            return "cap-shape_s"
        case "Convex":
            return "cap-shape_x"
        case _:
            return cap_shape

def fix_cap_surface(cap_surface):
    # The cap-surface column has 4 unique values: f, g, s, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be cap-surface_f, cap-surface_g, cap-surface_s, cap-surface_y
    match cap_surface:
        case "Fibrous":
            return "cap-surface_f"
        case "Grooves":
            return "cap-surface_g"
        case "Smooth":
            return "cap-surface_s"
        case "Scaly":
            return "cap-surface_y"
        case _:
            return cap_surface
        
def fix_bruises(bruises):
    # The bruises column has 2 unique values: f, t
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be bruises_f, bruises_t
    match bruises:
        case "No":
            return "bruises_f"
        case "Yes":
            return "bruises_t"
        case _:
            return bruises
        
def fix_odor(odor):
    # The odor column has 9 unique values: a, c, f, l, m, n, p, s, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be odor_a, odor_c, odor_f, odor_l, odor_m, odor_n, odor_p, odor_s, odor_y
    match odor:
        case "Almond":
            return "odor_a"
        case "Creosote":
            return "odor_c"
        case "Foul":
            return "odor_f"
        case "Anise":
            return "odor_l"
        case "Musty":
            return "odor_m"
        case "None":
            return "odor_n"
        case "Pungent":
            return "odor_p"
        case "Spicy":
            return "odor_s"
        case "Fishy":
            return "odor_y"
        case _:
            return odor
        
def fix_gill_size(gill_size):
    # The gill-size column has 2 unique values: b, n
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be gill-size_b, gill-size_n
    match gill_size:
        case "Broad":
            return "gill-size_b"
        case "Narrow":
            return "gill-size_n"
        case _:
            return gill_size
        
def fix_stalk_root(stalk_root):
    # The stalk-root column has 5 unique values: ?, b, c, e, r
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be stalk-root_?, stalk-root_b, stalk-root_c, stalk-root_e, stalk-root_r
    match stalk_root:
        case "Rhizomorphs":
            return "stalk-root_z"
        case "Bulbous":
            return "stalk-root_b"
        case "Club":
            return "stalk-root_c"
        case "Equal":
            return "stalk-root_e"
        case "Rooted":
            return "stalk-root_r"
        case _:
            return stalk_root
        
def fix_stalk_surface_above_ring(stalk_surface_above_ring):
    # The stalk-surface-above-ring column has 4 unique values: f, k, s, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be stalk-surface-above-ring_f, stalk-surface-above-ring_k, stalk-surface-above-ring_s, stalk-surface-above-ring_y
    match stalk_surface_above_ring:
        case "Fibrous":
            return "stalk-surface-above-ring_f"
        case "Silky":
            return "stalk-surface-above-ring_k"
        case "Smooth":
            return "stalk-surface-above-ring_s"
        case "Scaly":
            return "stalk-surface-above-ring_y"
        case _:
            return stalk_surface_above_ring
        
        
def fix_stalk_surface_below_ring(stalk_surface_below_ring):
    # The stalk-surface-below-ring column has 4 unique values: f, k, s, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be stalk-surface-below-ring_f, stalk-surface-below-ring_k, stalk-surface-below-ring_s, stalk-surface-below-ring_y
    match stalk_surface_below_ring:
        case "Fibrous":
            return "stalk-surface-below-ring_f"
        case "Silky":
            return "stalk-surface-below-ring_k"
        case "Smooth":
            return "stalk-surface-below-ring_s"
        case "Scaly":
            return "stalk-surface-below-ring_y"
        case _:
            return stalk_surface_below_ring
        
def fix_stalk_color_above_ring(stalk_color_above_ring):
    # The stalk-color-above-ring column has 9 unique values: b, c, e, g, n, o, p, w, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be stalk-color-above-ring_b, stalk-color-above-ring_c, stalk-color-above-ring_e, stalk-color-above-ring_g, stalk-color-above-ring_n, stalk-color-above-ring_o, stalk-color-above-ring_p, stalk-color-above-ring_w, stalk-color-above-ring_y
    match stalk_color_above_ring:
        case "Buff":
            return "stalk-color-above-ring_b"
        case "Cinnamon":
            return "stalk-color-above-ring_c"
        case "Red":
            return "stalk-color-above-ring_e"
        case "Gray":
            return "stalk-color-above-ring_g"
        case "Brown":
            return "stalk-color-above-ring_n"
        case "Orange":
            return "stalk-color-above-ring_o"
        case "Pink":
            return "stalk-color-above-ring_p"
        case "White":
            return "stalk-color-above-ring_w"
        case "Yellow":
            return "stalk-color-above-ring_y"
        case _:
            return stalk_color_above_ring
        
def fix_spore_print_color(spore_print_color):
    # The spore-print-color column has 9 unique values: b, h, k, n, o, r, u, w, y
    # The column is one-hot-encoded, so we need to fix the column names
    # The column names should be spore-print-color_b, spore-print-color_h, spore-print-color_k, spore-print-color_n, spore-print-color_o, spore-print-color_r, spore-print-color_u, spore-print-color_w, spore-print-color_y
    match spore_print_color:
        case "Buff":
            return "spore-print-color_b"
        case "Chocolate":
            return "spore-print-color_h"
        case "Black":
            return "spore-print-color_k"
        case "Brown":
            return "spore-print-color_n"
        case "Orange":
            return "spore-print-color_o"
        case "Green":
            return "spore-print-color_r"
        case "Purple":
            return "spore-print-color_u"
        case "White":
            return "spore-print-color_w"
        case "Yellow":
            return "spore-print-color_y"
        case _:
            return spore_print_color
def fix_ring_number(ring_number):
    match ring_number:
        case "None":
                return "ring_number_n"
        case "One":
                return "ring_number_o"
        case "Two":
                return "ring_number_t"

def fix_columns(gillsize, ringnumber, stalksurfacebelowring, bruises,
        stalkrootshape, sporeprintcolor, mushroomcapsurface, mushroomcapshape,
        odor, stalksurfaceabovering):
    df = pd.read_csv("simple1.csv")
    df[fix_bruises(bruises)] = 1
    df[fix_cap_shape(mushroomcapshape)] = 1
    df[fix_cap_surface(mushroomcapsurface)] = 1
    df[fix_odor(odor)] = 1
    df[fix_gill_size(gillsize)] = 1 
    df[fix_ring_number(ringnumber)] = 1
    df[fix_stalk_surface_below_ring(stalksurfacebelowring)] = 1
    df[fix_stalk_root(stalkrootshape)] = 1
    df[fix_spore_print_color(sporeprintcolor)] = 1
    df[fix_stalk_surface_above_ring(stalksurfaceabovering)] = 1
    return df

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
    ringnumber=get_slot_value(slots,'ringnumber',"none")
    stalksurfacebelowring=get_slot_value(slots,'stalksurfacebelowring',"none")
    bruises=get_slot_value(slots,'bruises',"none")
    stalkrootshape=get_slot_value(slots,'stalkrootshape',"none")
    sporeprintcolor=get_slot_value(slots,'sporeprintcolor',"none")
    mushroomcapsurface=get_slot_value(slots,'mushroomcapsurface',"none")
    mushroomcapshape=get_slot_value(slots,'mushroomcapshape',"none")
    odor=get_slot_value(slots,'odor',"none")
    stalksurfaceabovering=get_slot_value(slots,'stalksurfaceabovering',"none")

    X = fix_columns(gillsize, ringnumber, stalksurfacebelowring, bruises,
        stalkrootshape, sporeprintcolor, mushroomcapsurface, mushroomcapshape,
        odor, stalksurfaceabovering)

    model=loadmodel()
    ypred=model.predict(X)
    
    if ypred == 1:
        mushroomType = "Poisonous"
    else:
        mushroomType = 'Ed'
    
    confidence = 100*model.score(X,ypred)
    
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
                'content': f"I'm {confidence}% confident that that mushroom is probably {mushroomType}."
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
    return dispatch(event)


