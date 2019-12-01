def repl(inp: str) -> str:
    return inp.translate(inp.maketrans({'"':"'","'":'"'}))
