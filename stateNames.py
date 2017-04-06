"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


def printPlus(obj):
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print(u'{0}: {1}'.ljust().format(k, v))


# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

""".upper() converts any input to uppercase"""

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        """Remove this line to create the second layout of this task, the list still prints (print 9 lines down)"""
        print(state, "is", STATE_NAMES[state])

        """Creates spacing and padding value"""

        spacing = 1
        minPadding = 2
        padded_width = max(minPadding, max(len(x) for x in iter(STATE_NAMES.keys())) + spacing)
        for key in STATE_NAMES:
            print("{key: <{width}}{char}{value}".format(key=key, width=padded_width,char="is  ", value=STATE_NAMES[key]))

    else:
        print("Invalid short state")
    state = input("Enter short state: ")
