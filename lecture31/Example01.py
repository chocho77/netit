# https://www.pythontutorial.net/python-concurrency/python-threading/

def test_func( **kwargs ):
    options = {
            'option1' : 'default_value1',
            'option2' : 'default_value2',
            'option3' : 'default_value3', }

    options.update(kwargs)
    print(options)

test_func( option1='new_value1', option3='new_value3' )