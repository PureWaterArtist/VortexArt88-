import os
import json
import sys

def validate_json_files():
    target_dir = "Documentation/Workbench-Logs"
    required_keys = ["$schema", "contributor", "hardware", "protocol_1_singularity", "protocol_2_suction", "protocol_3_metrics"]
    
    # Check if directory exists
    if not os.path.exists(target_dir):
        print(f"❌ Error: Directory '{target_dir}' not found.")
        sys.exit(1)
        
    failed = False
    json_count = 0

    # Walk through the folder to find all JSON files
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".json"):
                json_count += 1
                file_path = os.path.join(root, file)
                print(f"🔍 Auditing ledger entry: {file_path}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"❌ Syntax Error in {file}: Invalid JSON formatting. Details: {e}")
                    failed = True
                    continue

                # Enforce core structure parameters
                missing_keys = [key for key in required_keys if key not in data]
                if missing_keys:
                    print(f"❌ Schema Error in {file}: Missing critical top-level keys: {missing_keys}")
                    failed = True
                    
                # Enforce specific metrics data types if keys exist
                try:
                    if "protocol_3_metrics" in data:
                        metrics = data["protocol_3_metrics"]
                        if not isinstance(metrics.get("loop_duration_minutes", 0), (int, float)):
                            print(f"❌ Data Type Error in {file}: 'loop_duration_minutes' must be a numeric value.")
                            failed = True
                except Exception as e:
                    print(f"❌ Processing Error in {file}: {e}")
                    failed = True

    if json_count == 0:
        print("💡 Notice: No ledger data cards found to validate in this commit.")
        return

    if failed:
        print("\n❌ Ledger validation failed. Please correct the schema errors listed above.")
        sys.exit(1)
    else:
        print(f"\n✅ Success! All {json_count} ledger data cards parsed flawlessly.")

if __name__ == "__main__":
    validate_json_files()
  
