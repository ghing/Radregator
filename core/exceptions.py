"""Exceptions thrown throughout the core app."""

class UnknownOutputFormat(Exception):
    """Exception thrown when an API call is made requesting output in
       an unknown format."""
    pass

class InvalidTopic(Exception):
    """Exception thrown when an API call requests an invalid topic via
    title."""
    pass

class NonAjaxRequest(Exception):
    """Exception thrown when an API call is made that is not an AJAX request
       and we don't want to allow this kind of (potentially) cross-site 
       call
    
    """
    pass

class MissingParameter(Exception):
    """Exception thrown when a parameter to an API request is missing"""
    pass

class RecentlyResponded(Exception):
    """Exception thrown when a user has already responded once within the
       allowable time limit"""
    pass

class MethodUnsupported(Exception):
    """Exception thrown when an HTTP request method isn't supported by the REST
       API"""
    pass

class MaximumExceeded(Exception):
    """Exception thrown when some API call exceeds a threshold.""" 
    pass

class UserOwnsItem(Exception):
    """Exception thrown when a user tries to vote on an item that she has 
       created"""
    pass

class NotUserQuestionReply(Exception):
    """Exception thrown when a user tries to accept a comment not a reply to 
       her own question"""
    pass
