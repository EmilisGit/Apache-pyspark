from Helpers import Helpers

# Sample data
with open("./data/duom_cut.txt") as file:
    line = file.read()

    extracted_entries = list(Helpers.extract_entries(line, ["svoris", "svorio grupe"]))

    # Print the results
    print("Extracted entries:")
    for entry in extracted_entries:
        print(entry)