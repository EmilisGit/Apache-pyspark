import re

class Helpers:
    @staticmethod
    def extract_entries(line: str, params_to_extract=None):
        if not params_to_extract:
            raise ValueError("Error: Specify parameter names to extract.")
        
        # Extract entries like {{...}} from the line
        entries = re.findall(r'\{\{.*?\}\}', line)
        
        for entry in entries:
            # Extract key=value pairs from the entry
            pairs = re.findall(r'(\w+(?:\s\w+)*)=([^,}]+)?', entry)
            entry_dict = {key.strip(): (value.strip() if value else "") for key, value in pairs}

            # Skip entry if any required param is missing or has an empty value
            if all(var in entry_dict and entry_dict[var].strip() for var in params_to_extract):
                filtered_dict = {}
                for var in params_to_extract:
                    value = entry_dict[var]
                    try:
                        value = float(value)
                    except ValueError:
                        pass  # Leave as string if not a float
                    filtered_dict[var] = value

                yield filtered_dict