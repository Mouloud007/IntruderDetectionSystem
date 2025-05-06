import os
import sqlite3
import face_recognition

# Connect to SQLite database
conn = sqlite3.connect("faces.db")
cursor = conn.cursor()

def add_face(image_path, name):
    """Encodes and stores a face in the database under a consistent name."""
    print(f"📷 Processing: {image_path}...")

    try:
        # Load image and encode faces
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if not encodings:
            print(f"❌ No face found in {image_path}")
            return

        encoding_blob = encodings[0].tobytes()  # Convert encoding to binary
        print(f"✔️ Face found, encoding stored for {name}")

        # Insert face into the database
        cursor.execute("INSERT INTO known_faces (name, encoding) VALUES (?, ?)", (name, encoding_blob))
        conn.commit()
        print(f"✅ {name} added successfully to the database!")

    except Exception as e:
        print(f"⚠️ Error processing {image_path}: {e}")

# **Define the folder and person's real name**
image_directory = "known_faces/Mouloud_Elguellab" # Folder with images
person_name = "Mouloud_Guellab"  # Store all images under this name

# **Process all images in the folder**
for filename in os.listdir(image_directory):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  
        add_face(os.path.join(image_directory, filename), person_name)  # Use consistent name

conn.close()
print("✅ Done adding faces to the database!")
