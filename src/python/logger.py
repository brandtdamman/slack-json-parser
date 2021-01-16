"""Centralized logging file.  Provides a wrapper for logging
and ensures there is no necessary clutter for the primary application.
"""

import logging

# ENUM instead of require other files to import logging
from enum import Enum
class LEVELS(Enum):
    """Enumerable object for classification of logging levels.
    """
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class SlackJPLogger:
    """Logging wrapper for SlackJP.
    """

    def __init__(self, LogFilename: str) -> None:
        """Initializes the wrapper logger.

        Arguments:
            LogFilename     --  file location where log should be placed
        """
        pass

    def log(Level: LEVELS, Message: str, Origin: str) -> None:
        """Logs the specified message using a given logging level
        and origin file.

        Arguments:
            Level           --  specifies how severe the message may be
            Message         --  descriptive message to be logged
            Origin          --  from where this message originated
        """
        pass

    def stack_trace(Trace: list, Error: str) -> None:
        """Prints a stack trace out on severe problems (ERROR or higher).

        Arguments:
            Trace           --  custom stack trace for where the error ended up
            Error           --  other details regarding the problem at hand
        """
        pass

class StackTracer:
    """Customized stack tracer.  Meant to produce more meaningful
    error results where applicable.

    This is added as a placeholder for the moment being.  Significant consideration
    is required to determine if this is really needed.  This would be better as an
    R&D project.
    """

    def __init__(self) -> None:
        """Initializes the StackTracer.
        """
        pass

    def add_event(self, Event: str, LineNumber: int) -> bool:
        """Appends a notable event to the stack.

        An event is defined as such:
            <DETAILS>

        Arguments:
            Event           --  description for stack
            LineNumber      --  specifies _exactly_ where this event was located

        Returns:
            result          --  if event addition was successful
        """
        pass

    def remove_event(self) -> bool:
        """Removes the top-most event from the stack.

        Returns:
            result          --  if event removal was successful
        """
        pass