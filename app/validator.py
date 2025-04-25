from word2number import w2n

def validate_fields(fields):
    errors = {}

    # Validate Income
    if fields["Income"] == "Not Found":
        errors["Income"] = "Income is missing."
    else:
        # Try to convert income to a valid number (either integer or float)
        try:
            # First, try to parse the value as a float (handles floating-point numbers)
            fields["Income"] = float(fields["Income"].replace(',', ''))  # Remove commas and convert to float
        except ValueError:
            # If it's not a valid number, check if it's in words
            try:
                fields["Income"] = w2n.word_to_num(fields["Income"])  # Convert words to number
            except ValueError:
                errors["Income"] = "Invalid income value."

    # Validate Loan Amount
    if fields["Loan Amount"] == "Not Found":
        errors["Loan Amount"] = "Loan amount is missing."
    else:
        # Try to convert loan amount to a valid number (either integer or float)
        try:
            # First, try to parse the value as a float (handles floating-point numbers)
            fields["Loan Amount"] = float(fields["Loan Amount"].replace(',', ''))  # Remove commas and convert to float
        except ValueError:
            # If it's not a valid number, check if it's in words
            try:
                fields["Loan Amount"] = w2n.word_to_num(fields["Loan Amount"])  # Convert words to number
            except ValueError:
                errors["Loan Amount"] = "Invalid loan amount value."

    return errors
