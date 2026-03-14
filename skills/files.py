import os
import config
from speech.speaker import speak

def search_downloads(query):
    """
    Searches the Downloads folder for a file matching the query.
    """
    speak(f"Searching for {query} in your Downloads.")
    query = query.lower()
    downloads_path = config.DOWNLOADS_DIR
    
    found = []
    
    for root, dirs, files in os.walk(downloads_path):
        # Limit depth to 2
        depth = root[len(downloads_path):].count(os.sep)
        if depth > 2:
            del dirs[:]
            
        for name in files:
            if query in name.lower():
                found.append(os.path.join(root, name))
                
        if len(found) >= 3:
            break
            
    if not found:
        return f"I couldn't find any file matching {query} in your downloads."
        
    target_file = found[0]
    filename = os.path.basename(target_file)
    speak(f"Found {filename}. Opening it now.")
    try:
        os.startfile(target_file)
        return f"Opened {filename}."
    except Exception as e:
        print(e)
        return f"Found {filename} but couldn't open it."
