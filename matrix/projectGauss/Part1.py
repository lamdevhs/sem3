


def promptPart1():
    prompt(title = "Part 1: Interactive linear system solver. Type `:q` to quit.",
           request = "Enter filepath of file containing the systems to solve:",
           parser = parseFilePart12,
           callback = solver,
           getInput = getInput)

# necessary because UI is not a sage module and therefore otherwise it crashes
def getInput():
    out = raw_input()
    return out


def solver(systems, filepath)