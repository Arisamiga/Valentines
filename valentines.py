import sys
import time

RED = '\033[91m'
END = '\033[0m'

text = list("                     Happy Valentine's Day!")

heart = '@'
output = []

# Adjust this value to change the size of the heart (Note this works as a zoom in/out so the higher the number the more you zoom out)
heart_size = 2.0  


#-- These two loops run before we write anything---

# Adjust the size of the heart based on the heart_size variable
for y in range(15, -15, -1):
    row = []
    for x in range(-30, 30):
        if ((x*0.04*heart_size)**2+(y*0.1*heart_size)**2-1)**3-(x*0.04*heart_size)**2*(y*0.1*heart_size)**3 <= 0:
            row.append(heart[(x-y) % len(heart)])
        else:
            row.append(' ')
    output.append(''.join(row))

# Remove leading newlines (any newlines at the start)
while output and output[0] == '':
    output.pop(0)

# --------------------------------


# Main Function
def main():
    sys.stdout.write(RED)
    sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Start (Writing of Happy valentines day)
    for i in range(0, len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        # Time.sleep here adds a delay till we add the next letter
        time.sleep(0.1)

    # Nice line
    sys.stdout.write("\n")
    sys.stdout.flush()

    # Nice line to make it look good
    sys.stdout.write("==========================================================================")
    sys.stdout.flush()

    # Add spacing
    for j in range(0,2):
        sys.stdout.write("\n")
        sys.stdout.flush()
    
    # Start drawing the heart
    for line in output:
        listLine = list(line)

        # Check if the line is just empty space
        if line.isspace():
            # If it is then dont run the rest of the code and continue to the next line
            continue

        for letter in listLine:
            sys.stdout.write(letter)
            sys.stdout.flush()
            # Time.sleep here adds a delay till we add the next letter
            time.sleep(0.02)
        sys.stdout.write("\n")
        sys.stdout.flush()

    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write(END)
    sys.stdout.flush()

# Default thing. It basically runs the main() function when the script starts
if __name__ == "__main__":
    main()