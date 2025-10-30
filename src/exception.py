import sys
import logging


def error_message_detail(error: Exception, exc_info=None) -> str:
    """Return a concise message with filename and line number for the given exception.

    If exc_info is None, sys.exc_info() is used to obtain the current exception info.
    """
    if exc_info is None:
        exc_info = sys.exc_info()

    _, _, tb = exc_info
    # Walk to the last traceback frame (the origin of the exception)
    while tb and tb.tb_next:
        tb = tb.tb_next

    if tb is None:
        # Fallback if traceback is not available
        return f"Error message [{error}]"

    file_name = tb.tb_frame.f_code.co_filename
    line_number = tb.tb_lineno
    return f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{error}]"


class CustomException(Exception):
    def __init__(self, error_message: Exception, exc_info=None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_info)

    def __str__(self) -> str:
        return self.error_message


