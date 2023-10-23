from pathlib import Path
import os

class file_service:
    def save_uploaded_file(uploaded_file):
        public_folder = os.path.join(os.getcwd(), 'public')
        temp_folder = os.path.join(public_folder,'temp')
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        file_path = os.path.join(temp_folder, uploaded_file.filename)
        uploaded_file.save(file_path)
        return file_path
    
    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)