from PIL import Image
import sys, os

def divide_image_by_grid(image_path, width, height):
    # Open the image
    with Image.open(image_path) as img:
        # Get the width and height of the image
        img_width, img_height = img.size

        # Calculate the size of each grid cell
        cell_width = img_width / width
        cell_height = img_height / height

        # create the output folder if not exist
        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        # Iterate over the grid
        for i in range(height):
            for j in range(width):
                # Define the boundaries of the cell
                left = j * cell_width
                upper = i * cell_height
                right = (j + 1) * cell_width
                lower = (i + 1) * cell_height

                # Crop the cell from the image
                cell = img.crop((left, upper, right, lower))

                # Convert the cell to RGB if it is not already
                cell = cell.convert('RGB')

                # Save the cell as a separate image
                cell.save(f"outputs/cell_{i}_{j}.jpg")

def main():
    try:
        image_path = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    except IndexError:
        print("Not enough arguments provided.")
        print("Usage: python script.py image_path width height")
        return
    divide_image_by_grid(image_path, width, height)
    print("image is split!")

if __name__ == "__main__":
    main()