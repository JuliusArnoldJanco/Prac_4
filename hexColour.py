colourName = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "	#8b8378", "Aquamarine1": "#7fffd4",
               "Aquamarine2": "#76eec6", "Aquamarine4": "	#458b74", "Azure1": "#f0ffff"}


choice = input("(No spaces, and capital for new word)\nEnter colour name: ")

while choice != "":
    if choice in colourName:
        print(choice,  colourName[choice])

    else:
        print("Invalid short state")
    choice = input("Enter colour name please: ")