def getBert(input):
    x = input.lower()
    y = x.split("bert")
    if len(y) > 2:
        return (y[1])[::-1]
    else:
        return ""
print(getBert("sdhsdjhbertclivebertjdwehd"))
