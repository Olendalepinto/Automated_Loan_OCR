
from app.preprocessing import preprocess_image
from app.ocr import extract_text
from app.extractor import extract_fields
from app.validator import validate_fields
from app.integrator import integrate_with_loan_system

def process_document(image_path):
    preprocessed_img = preprocess_image(image_path)
    text = extract_text(preprocessed_img)
    fields = extract_fields(text)
    validation_errors = validate_fields(fields)

    if validation_errors:
        print("Validation Errors:", validation_errors)
    else:
        integrate_with_loan_system(fields)
    return fields, validation_errors

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
    else:
        process_document(sys.argv[1])
