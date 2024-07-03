calls = 0
string = input('Введите строку (ну а вдруг подойдет):')
list_to_search = list(["Не входит",'Входит'])
def count_calls():
    global calls
    calls = calls +1
def string_info(string):
    tuple_ = tuple([len(string), string.upper(),string.lower()])
    count_calls()
    return tuple_
def is_contains (string,list_to_search):
    count_calls()
    return string in list_to_search
for i in range(int(len(string)/3)):
    print(string_info (string))
    yes_or_not = is_contains(string,list_to_search)
print(yes_or_not)
print('calls =',calls)