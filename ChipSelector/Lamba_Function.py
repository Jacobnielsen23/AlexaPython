import random
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launchRequest(handler_input): 
    speechOutput = "Greetings, welcome to the random chip selector! Which chip category are ya feeling today? Our categories are salty, spicy, sweet, sour, and cheesy." 
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("SaltyIntent"))
def SaltyIntent(handler_input): 
    SaltySelection = ["Lightly Salted Lays", "Salt and Vinegar Lays", "Salted Lays", "Pinch of Salt Lays", "Original Tostitos"]
    randomChipIndex = random.randint(0,len(SaltySelection)-1)
    speechOutput = "Here is your next salty snack!: " + SaltySelection[randomChipIndex]
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("SpicyIntent"))
def SpicyIntent(handler_input): 
    SpicySelection = ["Spicy Ruffles", "Jalapeño Lays", "Flamin' Hot Cheetos", "Takis Fuegos", "XXTRA Flamin' Hot Cheetos", "Spicy Nacho Doritos", "Doritos Spicy Sweet", "Kettle Cooked Jalapeño Lays", "Chili Cheese Fritos", "Flamin' Hot Funions", "Wild Takis", "Dynamite Takis", "Tapatio Doritos", "Chester's Hot Fries", "Hot Cheeto Puffs", "Jalapeño Cheetos", "Flamas Turbos", "Blue Heat Takis", "Spicy Queso Tostitos", "Flamin' Hot Dill Pickle Lays", "Jalapaño Fritos"]
    randomChipIndex = random.randint(0,len(SpicySelection)-1)
    speechOutput = "Here is your next spicy snack!: " + SpicySelection[randomChipIndex]
    
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("SweetIntent"))
def SweetIntent(handler_input): 
    SweetSelection = ["Barbeque Lays", "Sweet Southern Heat Barbeque Lays", "Sweet Potato Terra", "Doritos Spicy Sweet", "Salty Caramel Lays"]
    randomChipIndex = random.randint(0,len(SweetSelection)-1)
    speechOutput = "Here is your next sweet snack!: " + SweetSelection[randomChipIndex]
    
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("SourIntent"))
def SourIntent(handler_input): 
    SourSelection = ["Sour Cream & Onion Lays", "Cheddar & Sour Cream Lays", "Flamin' Hot Limon", "Lays Limon", "Spicy Limon Lays", "Tosisto Lime Chips"]
    randomChipIndex = random.randint(0,len(SourSelection)-1)
    speechOutput = "Here is your next sour snack!: " + SourSelection[randomChipIndex]
    
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("CheesyIntent"))
def CheesyIntent(handler_input): 
    CheesySelection = ["Spicy Nacho Doritos", "Classic Crunchy Cheetos", "Classic Cheeto Puffs", "Classic Ruffles", "Cheeto Paws", "Cheeto Balls", "Nacho Chips Bugle", "Cheddar Cheese Pringles", "Harvest Cheddar Sun Chips"]
    randomChipIndex = random.randint(0,len(CheesySelection)-1)
    speechOutput = "Here is your next cheesy snack!: " + CheesySelection[randomChipIndex]
    
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("ClassicIntent"))
def ClassicIntent(handler_input): 
    ClassicSelection = ["Classic Lays ", "Original Cheese Cheetos", "Original Ruffles", "Classic Pringles", "Classic Tositos", "Classic Fuego Takis", "Classic Sun Chips", "Classic Fritos", "Classic Sea Salt Terra", "Classic Funions"]
    randomChipIndex = random.randint(0,len(ClassicSelection)-1)
    speechOutput = "Here is your next classic snack!: " + ClassicSelection[randomChipIndex]
    
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def helpIntent(handler_input): 
    speechOutput = "You can say hello to me! How can I help?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
        )

@sb.request_handler(can_handle_func=lambda input: 
    is_intent_name("AMAZON.CancelIntent")(input) or 
    is_intent_name("AMAZON.StopIntent")(input))
def cancelOrStopIntent(handler_input): 
    speechOutput = "Okay, see you later"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallbackIntent(handler_input): 
    speechOutput = "Hmm, I'm not sure I caught that. You can say hello or help"
    reprompt = "I didn't catch that. What can I help you with?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(reprompt)
        .response
    )

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def sessionEndedRequest(handler_input): 
    logger.info("Session ended with reason: {}".format(
        handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("IntentRequest"))
def intentReflectorHandler(handler_input): 
    intentName = ask_utils.get_intent_name(handler_input)
    speechOutput = "You just triggered " + intentName + "."
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=lambda i,e: True)
def catchAllHandler(handler_input, exception): 
    logger.error(exception, exc_info = True)
    speechOutput = "Sorry, I had trouble doing what you asked. Please try again."
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(speechOutput)
        .response
        )

lambda_handler = sb.lambda_handler()
