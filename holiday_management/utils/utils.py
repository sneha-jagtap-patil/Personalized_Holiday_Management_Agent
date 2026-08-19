from multiprocessing.pool import TERMINATE
from xml.etree.ElementInclude import include

from autogen_agentchat.condition import TextMentionTermination

def get_termination_condition():
    """
    get the termination condition for the agent.
    """
    TERMINATION_WORD = "stop"
    text_mention_termination = TextMentionTermination(TERMINATION_WORD)
    return text_mention_termination
    