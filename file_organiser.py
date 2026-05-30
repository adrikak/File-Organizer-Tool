"""
File Organizer Tool v1.1
Project Code: FO-2025-001
---------------------------------
Automatically organizes files (recursively)
into category-based subfolders (Documents, Images, etc.)
and provides a complete summary with error handling.

Author: <Your Name>
Date: <Submission Date>
"""

import os
import shutil
import time
from pathlib import Path
from collections import defaultdict

# --- File Categories ---
CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".php", ".sql", ".json", ".xml"],
    "Executables": [".exe", ".msi", ".apk", ".deb", ".dmg"]
}


def get_category(file_ext):
    """Return category name for a given file extension."""
    for cat, ext_list in CATEGORIES.items():
        if file_ext.lower() in ext_list:
            return cat
    return "Others"


def organize_files(folder_path):
    """Organizes files inside folder and all subfolders (recursive)."""
    start_time = time.time()
    base_path = Path(folder_path)

    # --- 1. Invalid Path ---
    if not base_path.exists():
        print("❌ Error: Folder path not found. Please check again.")
        return

    print("\nScanning directory (including subfolders)...")

    # 🔁 Recursive scanning of all subfolders
    all_files = [f for f in base_path.rglob("*") if f.is_file()]
    total_files = len(all_files)

    if total_files == 0:
        print("No files found in the directory.")
        return

    print(f"Found {total_files} files to organize.\nOrganizing files...")

    # --- Track stats ---
    summary = defaultdict(list)
    folder_created = set()
    total_size = 0
    organized_count = 0
    errors = 0

    # Create an error log file
    error_log_path = base_path / "error_log.txt"
    error_log = open(error_log_path, "w", encoding="utf-8")

    for file in all_files:
        try:
            ext = file.suffix
            cat = get_category(ext)
            dest_folder = base_path / cat

            # Create folder if needed
            dest_folder.mkdir(exist_ok=True)
            folder_created.add(cat)

            # Handle duplicate names (5. Duplicate Filenames)
            dest_file = dest_folder / file.name
            if dest_file.exists():
                name_part = file.stem
                dest_file = dest_folder / f"{name_part}_{int(time.time())}{file.suffix}"

            # Try moving file
            shutil.move(str(file), str(dest_file))

            size = dest_file.stat().st_size
            total_size += size
            summary[cat].append(size)
            organized_count += 1

        # --- 2. Permission Denied ---
        except PermissionError:
            errors += 1
            msg = f"⚠️  Permission denied for: {file.name}\n"
            print(msg.strip())
            error_log.write(msg)

        # --- 3. Disk Space Full or other OS errors ---
        except OSError as e:
            if "No space" in str(e):
                print("❌ Disk space full! Stopping organization.")
                error_log.write("❌ Disk space full! Stopping organization.\n")
                break
            else:
                errors += 1
                msg = f"⚠️  OS error on {file.name}: {e}\n"
                print(msg.strip())
                error_log.write(msg)

        # --- 4. File In Use or unexpected error ---
        except Exception as e:
            errors += 1
            msg = f"⚠️  Skipped: {file.name} - {e}\n"
            print(msg.strip())
            error_log.write(msg)

    error_log.close()

    # --- Summary Section ---
    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    total_mb = total_size / (1024 * 1024)

    print("\nOrganization Summary")
    print("=" * 40)
    print(f"Total Files Processed : {total_files}")
    print(f"Files Organized        : {organized_count}")
    print(f"Total Size Organized   : {total_mb:.2f} MB")
    print(f"Execution Time         : {elapsed} seconds")
    print(f"Folders Created        : {len(folder_created)}")
    print(f"Errors Logged          : {errors}")

    print("\nFiles by Category:")
    for cat, sizes in summary.items():
        count = len(sizes)
        size_mb = sum(sizes) / (1024 * 1024)
        print(f"  {cat:12}: {count} files ({size_mb:.2f} MB)")

    print(f"\n✅ Organization complete! Files are now neatly arranged.")
    print(f"🧾 Error log saved as: {error_log_path.name}")


def main():
    print("Welcome to File Organizer Tool v1.1")
    print("=" * 40)
    folder_path = input("Enter folder path to organize: ").strip()

    if not folder_path:
        print("❌ Please enter a valid folder path.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
