from src.convert import convert_image

def main():
    # Get the image path from the user
    image_path = input("Enter the path to the image file: ")
    # Get the input format from the user
    input_format = input("Enter the input format (e.g., qcow2): ")
    # Get the output format from the user
    output_format = input("Enter the output format (e.g., raw): ")
    # Get the output path from the user
    output_path = input("Enter the desired output path: ")

    # Convert the image using the provided details
    success, result = convert_image(image_path, output_path, input_format, output_format)

    if success:
        print(f"Image successfully converted to {output_path}")
    else:
        print(f"Failed to convert image: {result}")

# Call the main function
if __name__ == "__main__":
    main()