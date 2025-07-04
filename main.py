import re
import csv
import json


def to_camel_case(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove non-alphanumeric characters except spaces
    words = re.split(r'\s+', text.strip())  # Split by spaces
    camel_case_text = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case_text

def convert_csv_to_arb(input_file, output_file, is_en=True):
    translations = {}
    
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='-')
        seen_keys = set()
        for row in reader:
            if len(row) > 0:
                key = row[0]
                print(row)
                value = row[1] if len(row) > 1 else '™ ' + key
                camel_case_key = to_camel_case(key)
                if camel_case_key not in seen_keys:  # Skip duplicates
                    if is_en:
                        translations[camel_case_key] = key
                        seen_keys.add(camel_case_key)
                    else:
                        translations[camel_case_key] = value
                        seen_keys.add(camel_case_key)

    with open(output_file, 'w', encoding='utf-8') as arbfile:
        json.dump(translations, arbfile, ensure_ascii=False, indent=2)

# Example usage
input_csv = "data.csv"
output_arb = "app_en.arb"
output_arb_id = "app_id.arb"
convert_csv_to_arb(input_csv, output_arb)
convert_csv_to_arb(input_csv, output_arb_id, is_en=False)
print(f"Conversion complete. Output saved to {output_arb} and {output_arb_id}.")
