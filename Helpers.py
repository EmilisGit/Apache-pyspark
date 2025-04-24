import re

class Helpers:
    @staticmethod
    def extract_entries(line: str, params_to_extract=None):
        if params_to_extract is None:
            assert("Error: Specify parameter names to extract.")
        
        # Find all entries in the line
        entries = re.findall(r'\{\{.*?\}\}', line)
        
        for entry in entries:
            # Extract all key-value pairs from the entry
            pairs = re.findall(r'(\w+(?:\s\w+)*)[=<>]+([^}]*)', entry)

            # Convert to dictionary
            entry_dict = {key.strip(): value.strip() for key, value in pairs}

            # Check if all required variables are present
            if all(var in entry_dict for var in params_to_extract):
                # Create a filtered dictionary with only the requested variables
                filtered_dict = {}
                for var in params_to_extract:
                    value = entry_dict[var]
                    try:
                        if re.match(r'^-?\d+(\.\d+)?$', value):
                            value = float(value)
                    except ValueError:
                        pass  # Keep as string if conversion fails
                    filtered_dict[var] = value
                
                yield filtered_dict