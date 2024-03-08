def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


source_file = '4.txt'
destination_file = '5.txt'

copy_file(source_file, destination_file)