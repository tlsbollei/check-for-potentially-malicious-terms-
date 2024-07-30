import re

red_flags = [ "data sharing", "third parties", "without notice", "indemnify", "waiver",
    "liability", "sole discretion", "terminate", "arbitration", "no responsibility",
    "without limitation", "binding", "mandatory", "perpetual", "royalty-free",
    "unrestricted", "assignable", "dispute", "governing law", "severability"
]

def check_terms(text):
    found_flags = {}
    for flag in red_flags:
        matches = re.findall(flag, text, re.IGNORECASE)
        if matches:
            found_flags[flag] = len(matches)
    return found_flags

def read_terms_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            terms_text = file.read()
        return terms_text
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    file_path = input("Enter the path of the document containing the terms of services : ")
    terms_text = read_terms_file(file_path)
    
    if terms_text:
        found_flags = check_terms(terms_text)
        
        if found_flags:
            print("Potentially malicious terms found : ")
            for flag, count in found_flags.items():
                    print(f"'{flag}': found {count} time(s)")
        else:
            print("No malicious flags found.")
    else:
        print("Could not read terms and services file.")


if __name__ == "__main__":
    main()