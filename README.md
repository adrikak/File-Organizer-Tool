# File Organizer Tool

A Python-based automation utility that automatically organizes files into structured category folders based on their file types. The tool scans a user-specified directory, categorizes files using predefined extension mappings, creates folders dynamically, handles duplicate filenames, generates statistics, and maintains error logs for failed operations.

This project was developed to demonstrate practical applications of Python file handling, automation, exception handling, directory traversal, and system utilities.

---

## Project Overview

Managing large directories with hundreds of mixed file types can be time-consuming and inefficient. The File Organizer Tool addresses this problem by automatically sorting files into categorized folders such as Documents, Images, Videos, Audio, Archives, Code, and Executables.

The application improves directory organization, enhances file accessibility, and reduces manual effort through automation.

---

## Key Features

### Automatic File Categorization
Files are automatically classified based on their extensions and moved into dedicated folders.

Supported Categories:

- Documents
  - PDF, DOC, DOCX, TXT, XLSX, PPTX, etc.

- Images
  - JPG, JPEG, PNG, GIF, BMP, SVG, WEBP, etc.

- Videos
  - MP4, AVI, MKV, MOV, WEBM, etc.

- Audio
  - MP3, WAV, FLAC, AAC, OGG, etc.

- Archives
  - ZIP, RAR, 7Z, TAR, GZ, etc.

- Code Files
  - Python, C, C++, Java, HTML, CSS, SQL, JSON, XML, etc.

- Executables
  - EXE, MSI, APK, DMG, etc.

- Others
  - Any unsupported or unidentified file types

---

### Recursive Directory Scanning

The tool scans all files within the selected directory and its subdirectories using recursive traversal.

Benefits:
- Organizes deeply nested files
- Processes large directory structures efficiently
- Reduces manual searching and sorting effort

---

### Automatic Folder Creation

Category folders are created automatically when required.

Examples:

Documents/
Images/
Videos/
Audio/
Archives/
Code/
Executables/
Others/

No unnecessary folders are created.

---

### Duplicate Filename Handling

If a file with the same name already exists in the destination folder, the system automatically generates a unique filename using a timestamp.

Example:

report.pdf
report_1765234512.pdf

This prevents accidental overwriting and ensures data integrity.

---

### Error Handling & Logging

The application includes robust exception handling for common file system issues.

Handled Scenarios:

- Invalid directory paths
- Permission denied errors
- Files currently in use
- Operating system errors
- Insufficient disk space
- Unexpected runtime exceptions

All issues are recorded in:

error_log.txt

for later review and debugging.

---

### Organization Statistics

After completion, the tool generates a detailed summary including:

- Total files processed
- Files successfully organized
- Total storage organized
- Number of folders created
- Execution time
- Error count
- Category-wise file distribution

Example Output:

Organization Summary
====================
Total Files Processed: 156
Files Organized: 156
Folders Created: 7
Execution Time: 2.3 seconds

---

## Technical Implementation

### Core Concepts Used

- File Handling
- Directory Management
- Recursive Traversal
- Exception Handling
- Data Structures
- Modular Programming
- Automation Scripting

### Python Libraries Used

```python
os
shutil
time
pathlib
collections
```

### Data Structures

```python
dictionary
set
defaultdict
list
```

Used for:

- File category mapping
- Statistics generation
- Folder tracking
- Summary reporting

---

## Project Workflow

1. User enters a directory path.
2. Path validity is verified.
3. All files are scanned recursively.
4. File extensions are analyzed.
5. Appropriate category is determined.
6. Destination folder is created if necessary.
7. Duplicate names are resolved.
8. Files are moved to their respective folders.
9. Statistics are generated.
10. Errors are logged.
11. Summary report is displayed.

---

## Skills Demonstrated

This project demonstrates proficiency in:

- Python Programming
- Automation Development
- File System Operations
- Exception Handling
- Data Organization
- Problem Solving
- Software Design
- Modular Programming
- Debugging and Testing

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Building real-world automation tools
- Managing files and directories programmatically
- Designing maintainable Python applications
- Implementing robust error handling
- Working with recursive file operations
- Generating analytical reports from processed data

---

## Future Improvements

Potential enhancements include:

- Graphical User Interface (GUI)
- Drag-and-Drop Folder Selection
- Undo Functionality
- Custom Category Configuration
- Cloud Storage Integration
- Real-Time File Monitoring
- Multi-threaded Processing

---

## Project Information

Project Code: FO-2025-001

Project Type: Academic / Portfolio Project

Language: Python 3

Development Approach: Modular and Object-Oriented Design Principles

---

## Author

Adrika Kumari

Computer Engineering Student
JSPM Rajarshi Shahu College of Engineering, Pune
