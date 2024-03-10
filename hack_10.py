"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    
    ls = []
    lista = []
    result = "fooziman"
    lista.append(result.replace("fooziman","F00Z1M@N"))
    ls = list(lista[0])

    return ls

r = fn_hack_10()
print(r)  