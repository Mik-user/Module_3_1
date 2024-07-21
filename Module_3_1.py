calls = 0
string = str()
list_to_search = list()
tuple_ = tuple()
def count_calls():
    global calls
    calls += 1
def string_info(string):
    tuple_ = tuple([len(string), string.upper(),string.lower()])
    count_calls()
    return tuple_
def is_contains (string,list_to_search):
    count_calls()
    for i in list_to_search:
        k = bool(string.lower() == i.lower())
        if k == 'true':
            break
        else:
            continue
    return k
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('calls =',calls)