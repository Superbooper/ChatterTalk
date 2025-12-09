from modules.chatter import converse
def check_return_string():
    '''
    tests chatterbot is correctly returning a string
    '''
    result = converse('hi')
    assert result is str, f"expected string response but got{type(result)}"