import os
import re
import sys

def convert_pound_comments(yaml_content: str) -> str:
    """Converts £ comments into valid YAML # comments while protecting currency values."""
    # Matches '£' only if preceded by the start of a line or whitespace
    pattern = r'(?<=^|\s)£'
    return re.sub(pattern, '#', yaml_content)

def pardon_sir_logic(target_directory: str = "."):
    """Scans target directory for YAML files and cleanly updates their comments."""
    print(f"[pardon, sir] Scanning directory: '{os.path.abspath(target_directory)}'...")
    yaml_extensions = ('.yaml', '.yml')
    modified_count = 0

    for root, _, files in os.walk(target_directory):
        for file in files:
            if file.lower().endswith(yaml_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    updated_content = convert_pound_comments(original_content)
                    
                    if original_content != updated_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"Fixed comments in: {os.path.relpath(file_path)}")
                        modified_count += 1
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    print(f"\nDone. Cleaned up {modified_count} YAML file(s).")

def main():
    """CLI entry point accepting an optional folder pathway argument."""
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    pardon_sir_logic(target)

if __name__ == "__main__":
    main()
