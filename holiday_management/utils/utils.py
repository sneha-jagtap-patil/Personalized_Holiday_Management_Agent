from autogen_agentchat.conditions import TextMentionTermination


def get_termination_condition():
    """
    Returns the termination condition for the holiday management team.
    The team stops when an agent explicitly outputs TERMINATE.
    """

    TERMINATION_WORD = "TERMINATE"

    return TextMentionTermination(TERMINATION_WORD)