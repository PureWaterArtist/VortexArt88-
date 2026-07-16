import os
import sys
import subprocess

def get_root_directory():
    """Calculates the absolute root path where this orchestrator is executed."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def execute_sub_module(relative_path_to_script):
    """
    Safely executes a sub-module script via a controlled subprocess pipeline,
    passing the system executable down to maintain environment continuity.
    """
    root_dir = get_root_directory()
    absolute_script_path = os.path.join(root_dir, relative_path_to_script)
    
    # Isolate the targeted directory to allow local file references (.json files) to resolve
    target_working_directory = os.path.dirname(absolute_script_path)
    script_filename = os.path.basename(absolute_script_path)
    
    print(f"[*] Dispatching Sub-Pipeline: {relative_path_to_script}")
    
    if not os.path.exists(absolute_script_path):
        print(f"[❌] CRITICAL ERROR: Target execution script missing at: {absolute_script_path}")
        return False
        
    try:
        # Run using the same active Python interpreter shell instance
        subprocess.run(
            [sys.executable, script_filename],
            cwd=target_working_directory,
            check=True,
            text=True
        )
        print(f"[✅] STEP COMPLETE: {script_filename} executed successfully.\n")
        return True
    except subprocess.CalledProcessError as err:
        print(f"[❌] EXECUTION CRASH: Subprocess {script_filename} exited with code {err.returncode}\n")
        return False

def main():
    print("=" * 60)
    print("VORTEXART88: MASTER UNIFIED SIMULATION ORCHESTRATOR")
    print("=" * 60)
    
    # 1. Verify Global Data Profile Context First
    root_path = get_root_directory()
    global_config_path = os.path.join(root_path, "config", "data-card.json")
    
    print("[*] Validating Global Ecosystem Profiles...")
    if os.path.exists(global_config_path):
        print("[+] Standard Configuration Frame verified: /config/data-card.json loaded.\n")
    else:
        print("[⚠️] WARNING: Global data-card.json configuration profile missing inside /config/.")
        print("    ↳ Execution paths will fall back onto component hardware defaults.\n")

    # 2. Sequential Execution Pipeline Matrix (Modular Component Paths)
    pipeline_steps = [
        "components/transcendental-flow-regulator/run_component.py",
        "components/flower-of-life-mesh/generate_fol_mesh.py",
        "components/figure-eight-mixer/mixer_vectors.py",
        "components/singularity-navigation-core/navigation_vectors.py"
        "components/singularity-navigation-core/junction_matrix.py"
        "components/manifold-distribution-plenum/plenum_vectors.py"
        "components/outer-pressure-casing/casing_vectors.py"
        "components/end-cap-collars/collar_threads.py"
        "components/chiral-mesh-filter/chiral_engine.py"
        "components/hyper-cylindrical-plenum/hyper_engine.py"
        "components/toroidal-helical-diffuser/diffuser_vectors.py"
        "components/dodecahedral-flow-harmonizer/harmonizer_vectors.py"
    ]
    
    success_count = 0
    for step in pipeline_steps:
        if execute_sub_module(step):
            success_count += 1
            
    # 3. Final Execution Diagnostics Summary
    print("=" * 60)
    print("SIMULATION ENGINE EXECUTION SUMMARY")
    print("=" * 60)
    print(f"[-] Total Pipeline Modules Dispatched: {len(pipeline_steps)}")
    print(f"[-] Total Modules Completed Cleanly:  {success_count}")
    
    if success_count == len(pipeline_steps):
        print("[🎉] STATUS COMPLETE: Unified simulation canvas fully built without errors.")
    else:
        print("[⚠️] STATUS UNRESOLVED: One or more architectural layers failed to initialize.")
    print("=" * 60)

if __name__ == "__main__":
    main()
    
