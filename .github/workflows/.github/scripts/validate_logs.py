import os
import json
import sys

def validate_and_compile():
    target_dir = "Documentation/Workbench-Logs"
    required_keys = ["$schema", "contributor", "hardware", "protocol_1_singularity", "protocol_2_suction", "protocol_3_metrics"]
    
    if not os.path.exists(target_dir):
        print(f"❌ Error: Directory '{target_dir}' not found.")
        sys.exit(1)
        
    failed = False
    valid_records = []

    # 1. VALIDATION PHASE
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except Exception as e:
                    print(f"❌ Syntax Error in {file}: {e}")
                    failed = True
                    continue

                missing_keys = [key for key in required_keys if key not in data]
                if missing_keys:
                    print(f"❌ Schema Error in {file}: Missing keys {missing_keys}")
                    failed = True
                    continue
                
                valid_records.append(data)

    if failed:
        print("\n❌ Errors found during audit. Stopping leaderboard generation.")
        sys.exit(1)

    if not valid_records:
        print("💡 No ledger records found to process.")
        return

    # 2. METRICS COMPILATION PHASE
    total_logs = len(valid_records)
    total_do_delta = 0.0
    total_ph_delta = 0.0
    regions = set()
    materials = {}
    leaderboard_rows = []

    for item in valid_records:
        username = item["contributor"]["username"]
        region = item["contributor"]["region"]
        regions.add(region)
        
        # Track materials used
        mat = item["hardware"]["nozzle_material"]
        materials[mat] = materials.get(mat, 0) + 1
        
        # Calculate quality deltas
        metrics = item["protocol_3_metrics"]
        base_do = float(metrics["baseline"]["dissolved_oxygen_mg_l"])
        post_do = float(metrics["post_singularity"]["dissolved_oxygen_mg_l"])
        do_delta = post_do - base_do
        total_do_delta += do_delta
        
        base_ph = float(metrics["baseline"]["ph"])
        post_ph = float(metrics["post_singularity"]["ph"])
        ph_delta = post_ph - base_ph
        total_ph_delta += ph_delta
        
        # Format a clean row for the leaderboard table
        leaderboard_rows.append(
            f"| @{username} | `{region}` | `{mat}` | {base_do} mg/L → {post_do} mg/L | **+{do_delta:.1f} mg/L** |"
        )

    avg_do = total_do_delta / total_logs
    avg_ph = total_ph_delta / total_logs
    top_material = max(materials, key=materials.get) if materials else "N/A"

    # 3. MARKDOWN COMPONENT GENERATION
    leaderboard_markdown = f"""
<!-- LEDGER_START -->
### 🌍 Global Impact Statistics
* 📊 **Total Validated Workshop Nodes:** `{total_logs}` active deployments
* 🫧 **Average Dissolved Oxygen Boost:** `+{avg_do:.2f} mg/L` toward saturation
* ⚖️ **Average pH Optimization Shift:** `+{avg_ph:.2f}` stabilization delta
* 🖨️ **Most Deployed Workshop Material:** `{top_material}`
* 🗺️ **Active Biome Footholds:** `{len(regions)}` global regions mapped

### 🏆 Decentralized Proof Leaderboard

| Contributor | Operational Biome | Material Matrix | Dissolved Oxygen Shift | Oxygenation Delta |
| :--- | :--- | :--- | :--- | :--- |
{chr(10).join(leaderboard_rows)}
<!-- LEDGER_END -->"""

    # 4. INJECT INTO MAIN README
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find our anchoring tags inside the main README
        start_tag = "<!-- LEDGER_START -->"
        end_tag = "<!-- LEDGER_END -->"
        
        if start_tag in content and end_tag in content:
            parts = content.split(start_tag)
            remains = parts[1].split(end_tag)
            new_content = parts[0] + leaderboard_markdown.strip() + remains[1]
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("✅ Main README.md Leaderboard successfully recompiled and updated!")
        else:
            print("⚠️ Notice: Anchor comments missing in README.md. Leaderboard data compiled but not injected.")

if __name__ == "__main__":
    validate_and_compile()
    
