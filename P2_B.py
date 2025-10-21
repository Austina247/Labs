import console_gfx

def display_menu():
    print("\nRLE Menu\n"
          "--------")
    print("0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data\n")

def to_hex_string(data):
    string = ""
    for i in range(len(data)):
        if data[i] < 10:
            string = string + data[i]
        else:
            string = string + hex(data[i])

def count_runs(flat_data):
    count = 1
    num = 0
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
        else:
            num += 1
            count = 1
        if count == 15:
            num += 1
            count = 1
    return num + 1

def encode_rle(flat_data):
    count = 1
    rle_data = []
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
        elif count == 15:
            rle_data.append(15)
            rle_data.append(flat_data[i])
            count = 1
        else:
            rle_data.append(count)
            rle_data.append(flat_data[i])
    return rle_data

def get_decoded_length(rle_data):
    sum = 0
    for i in range(0,len(rle_data),2):
        sum += rle_data[i]
    return sum

def decode_rle(rle_data):
    unzipped_rle = []
    for i in range(0,len(rle_data),2):
        for j in range(rle_data[i]):
            unzipped_rle.append(rle_data[i+1])
    return unzipped_rle

def string_to_data(data_string):
    rle = []
    for char in data_string:
        if type(char) == int:
            rle.append(char)
        else:
            rle.append(int(char,16))
    return rle

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    console_gfx.display_image(console_gfx.test_rainbow)
    while True:
        display_menu()
        option = int(input("Select a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = console_gfx.load_file(file_name)
        elif option == 2:
            image_data = console_gfx.load_rle(console_gfx.test_image)
            print("Test image data loaded.")
        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
        elif option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ")
        elif option == 5:
            rle_flat_hex_string = input("Enter the hex string holding flat data: ")
        elif option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data)

