import os
import shutil

# Directories
train_dir = 'trn'
val_dir = 'val'
test_dir = 'tst'

# New directories
new_train_dir = 'new_train'
new_val_dir = 'new_val'
new_test_dir = 'new_test'

# Create new directories if they don't exist
os.makedirs(new_train_dir, exist_ok=True)
os.makedirs(new_val_dir, exist_ok=True)
os.makedirs(new_test_dir, exist_ok=True)

def reorganize_files(src_dir, dest_dir):
    for writer in os.listdir(src_dir):
        writer_path = os.path.join(src_dir, writer)
        if os.path.isdir(writer_path):
            for word in os.listdir(writer_path):
                word_path = os.path.join(writer_path, word)
                if os.path.isfile(word_path):
                    # Create word directory if it doesn't exist
                    word_dest_dir = os.path.join(dest_dir, word)
                    os.makedirs(word_dest_dir, exist_ok=True)

                    # New filename
                    new_filename = f"{writer}_{word}"
                    new_filepath = os.path.join(word_dest_dir, new_filename)

                    # Move file
                    shutil.copy2(word_path, new_filepath)
                    print(f"Moved {word_path} to {new_filepath}")

# Reorganize training files
reorganize_files(train_dir, new_train_dir)

# Reorganize testing files
reorganize_files(val_dir, new_val_dir)

# Reorganize testing files
reorganize_files(test_dir, new_test_dir)

print("Reorganization complete.")
