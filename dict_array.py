#
# Implement function get_result
#
def get_result(s, words):
    for i in words:
        s = s.replace(i, '')
    if len(s) == 0:
        return True
    else:
        return False

print(get_result("onetwone",["one", "two"]))