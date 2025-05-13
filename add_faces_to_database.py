import os
import sqlite3
import face_recognition

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("faces.db")
cursor = conn.cursor()

def add_face(image_path, name):
    """Encodes a face from an image and saves it to the database with the given name."""
    print(f"📷 Processing: {image_path}...")

    try:
        # Load the image using face_recognition library
        image = face_recognition.load_image_file(image_path)
        
        # Detect and encode faces in the image
        encodings = face_recognition.face_encodings(image)

        # If no face is detected, skip this image
        if not encodings:
            print(f"❌ No face found in {image_path}")
            return

        # Use the first face encoding found and convert it to binary
        encoding_blob = encodings[0].tobytes()
        print(f"✔️ Face found, encoding stored for {name}")

        # Save the name and face encoding into the database
        cursor.execute("INSERT INTO known_faces (name, encoding) VALUES (?, ?)", (name, encoding_blob))
        conn.commit()
        print(f"✅ {name} added successfully to the database!")

    except Exception as e:
        # Handle and log any errors that occur while processing
        print(f"⚠️ Error processing {image_path}: {e}")

# Set the folder where the known images are stored
image_directory = "known_faces/Mouloud_Elguellab"  # Folder with images of one person

# Define a single consistent name for all images (used as the key in the database)
person_name = "Mouloud_Guellab"  # This is how the person will be referenced in the DB

# Loop through each image in the folder
for filename in os.listdir(image_directory):
    # Only process image files with common image extensions
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Send the image and name to the add_face function
        add_face(os.path.join(image_directory, filename), person_name)

# Close the database connection after all processing is done
conn.close()
print("✅ Done adding faces to the database!")
