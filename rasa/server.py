from rasa_core.channels import SocketIOInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.policies import KerasPolicy, MemoizationPolicy

# load your trained agent
interpreter = RasaNLUInterpreter('rasa/models/nlu/profiler/nlu')
agent = Agent.load('rasa/models/dialogue', 
	interpreter=interpreter, 
	action_endpoint=EndpointConfig('http://localhost:5055/webhook')
    #for action endpoint
)

input_channel = SocketIOInput(
    # event name for messages sent from the user
    user_message_evt="user_uttered",
    # event name for messages sent from the bot
    bot_message_evt="bot_uttered",
    # socket.io namespace to use for the messages
    namespace=None
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5500, serve_forever=True)