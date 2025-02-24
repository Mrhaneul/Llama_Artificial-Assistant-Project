import os
import subprocess

def find_and_open_app(app_name):
    search_dirs = ["C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users\\haneu\\AppData\\Local\\Microsoft\\WindowsApps", "C:\\Users\\haneu\\Desktop\\Program"]
    
    for directory in search_dirs:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower() == f"{app_name}.exe":
                    app_path = os.path.join(root, file)
                    try:
                        subprocess.run(app_path, shell=True)
                        print(f"Opening {app_name}...")
                        return
                    except Exception as e:
                        print(f"Failed to open {app_name}: {e}")
                        return
    print(f"{app_name}.exe not found.")

# Example usage
app_name = input("Enter the name of the application to open: ")
find_and_open_app(app_name)