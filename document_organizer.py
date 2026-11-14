import os
import shutil
from datetime import datetime

# 1. Define your Downloads folder and target destination base folder
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")
BASE_DEST_DIR = os.path.expanduser("~/Documents/Organized_Files")

# 2. Define keyword rules to sort your everyday files automatically
CATEGORY_RULES = {
    "Job_Applications": ["lebenslauf", "cv", "resume", "reference", "ndic", "sec", "zach", "vesterling", "hays"],
    "Amazon_Onboarding": ["amazon", "contract", "vertrag", "shift", "steuer"],
    "Certificates": ["certificate", "zertifikat", "coursera", "google", "ibm", "wireshark"],
    "Government_Visa": ["arbeitsagentur", "chancenkarte", "anmeldung", "termin"]
}

LOG_FILE = os.path.join(BASE_DEST_DIR, "organizer_log.txt")


def log_action(message):
    """Appends a timestamped log entry to organizer_log.txt."""
    os.makedirs(BASE_DEST_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")


def organize_documents():
    """Scans the Downloads folder and moves matching PDF/DOCX files into categorized folders."""
    if not os.path.exists(DOWNLOADS_DIR):
        print(f"Directory not found: {DOWNLOADS_DIR}")
        return

    moved_count = 0

    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        # Skip folders and only check PDF or Word documents
        if not os.path.isfile(file_path):
            continue
        if not filename.lower().endswith((".pdf", ".docx", ".doc")):
            continue

        lower_name = filename.lower()
        matched_category = "Other_Documents"

        # Check which category matches the keywords in the filename
        for category, keywords in CATEGORY_RULES.items():
            if any(keyword in lower_name for keyword in keywords):
                matched_category = category
                break

        # Create the target subfolder if it does not exist yet
        target_folder = os.path.join(BASE_DEST_DIR, matched_category)
        os.makedirs(target_folder, exist_ok=True)

        # Move the file safely without overwriting existing files
        dest_path = os.path.join(target_folder, filename)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            timestamp_tag = datetime.now().strftime("%H%M%S")
            dest_path = os.path.join(target_folder, f"{base}_{timestamp_tag}{ext}")

        shutil.move(file_path, dest_path)
        log_action(f"MOVED: '{filename}' -> '{matched_category}/'")
        print(f"Moved: {filename} -> {matched_category}/")
        moved_count += 1

    print(f"\nDone! Organized {moved_count} document(s). Check {LOG_FILE} for audit logs.")


if __name__ == "__main__":
    organize_documents()
