"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"

    return result.replace("n","N")

r = fn_hack_4()

print(r)