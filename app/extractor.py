import re

def extract_fields(text):
    fields = {}

    # Normalize symbols and spacing issues
    text = text.replace('\n', ' ')
    text = re.sub(r"\s{2,}", " ", text)
    text = text.replace("₹", "").replace("%", "").replace("$", "")
    text = text.strip()

    # --- Name Extraction --- (updated to ensure we don't capture DOB)
    first_name_match = re.search(r"First Name[:\-]?\s*(\w+)", text, re.IGNORECASE)
    middle_name_match = re.search(r"Middle Name[:\-]?\s*(\w+)", text, re.IGNORECASE)
    last_name_match = re.search(r"Last Name[:\-]?\s*(\w+)", text, re.IGNORECASE)
    
    # Match for Name only, without capturing DOB
    name_match = re.search(r"Name[:\-]?\s*([A-Za-z ]+)(?=\n|Date of Birth|$)", text, re.IGNORECASE)

    if name_match:
        fields["Name"] = name_match.group(1).strip()
    elif first_name_match and last_name_match:
        middle = f" {middle_name_match.group(1)}" if middle_name_match else ""
        fields["Name"] = f"{first_name_match.group(1)}{middle} {last_name_match.group(1)}"
    else:
        fields["Name"] = "Not Found"

    # --- Address Extraction ---
    address_match = re.search(r"(Address|Add|Postal Address|Home Address)[:\-]?\s*(.+?)(?=(Monthly Income|Loan Amount|Phone|Email|$))", text, re.IGNORECASE)
    fields["Address"] = address_match.group(2).strip() if address_match else "Not Found"

    # --- Income Extraction ---
    income_match = re.search(r"(Monthly Income|Income|Annual Income)[:\-]?\s*([\d,]+(?:\.\d{2})?)", text, re.IGNORECASE)
    fields["Income"] = income_match.group(2).strip() if income_match else "Not Found"

    # --- Loan Amount Extraction ---
    loan_amount_match = re.search(r"Loan Amount[:\-]?\s*([\d,]+(?:\.\d{2})?)", text, re.IGNORECASE)
    fields["Loan Amount"] = loan_amount_match.group(1).strip() if loan_amount_match else "Not Found"

    return fields
