import os


def validate_file_extension(value):
    isValid = True
    value_array = value.split()

    ext = os.path.splitext(value_array[1])
    # ext = value_array[-1]
    file_extension = ext[1]
    print(file_extension)
    valid_extensions = ['.pdf']


    if not file_extension.lower() in valid_extensions:
        isValid = False
        
    return isValid


def validate_image(value):
    isValid = True

    ext = os.path.splitext(value[1])
    valid_extensions = ['.jpg', '.png', 'jpeg']


    if not ext.lower() in valid_extensions:
        isValid = False
        
    return isValid