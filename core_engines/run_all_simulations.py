import os
import sys
import subprocess

def run_simulation_script(script_path):
    """Executes a sub-module python script and returns the status code."""
    script_dir = os.path.dirname(script_path)
    script_name = os.path.basename(script_path)
    
    # Calculate path relative to project root
    current_dir = os.getcwd()
    absolute_script_dir = os.path.abspath(os.path.join(current_dir, script_dir))
    
    print(f"\n[🔄] RUNNING PIPELINE STAGE: {script_name}")
    print(f"    ↳ Path: {script_dir}/")
    
    if not os.path.exists(os.path.join(absolute_script_dir, script_name)):
        print(f"[❌] ERROR: Target script file missing. Checked path: {script_dir}/{script_name}")
        return False
        
    try:
        # Run script in its localized directory environment
        result = subprocess.run(
            [sys.executable, script_name],
            cwd=absolute_script_dir,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[❌] PIPELINE STAGE CRASHED: {script_name}")
        print(e.output)
        return False

def main():
    print("=" * 70)
    print("🛸 VORTEXART88 MASTER RUNNER: UNIFIED 26-STAGE DIGITAL TWIN SIMULATION")
    print("=" * 70)
    
    # 2. Sequential Execution Pipeline Matrix (Modular Component Paths)
    pipeline_steps = [
        "components/manifold-distribution-plenum/plenum_vectors.py",
        "components/hyper-cylindrical-plenum/hyper_engine.py",
        "components/octachoric-hyper-plenum/octachoric_engine.py",
        "components/glome-hyper-manifold/glome_engine.py",
        "components/16-cell-orthoplex-plenum/orthoplex_engine.py",
        "components/24-cell-octaplex-plenum/octaplex_engine.py",
        "components/transcendental-flow-regulator/run_component.py",
        "components/figure-eight-mixer/mixer_vectors.py",
        "components/singularity-navigation-core/navigation_vectors.py",
        "components/singularity-navigation-core/junction_matrix.py",
        "components/dodecahedral-flow-harmonizer/harmonizer_vectors.py",
        "components/dual-braid-helical-core/braid_vectors.py",
        "components/clifford-torus-regulator/clifford_engine.py",
        "components/icosahedral-vector-harmonizer/harmonizer_vectors.py",
        "components/prolate-spheroidal-chamber/spheroid_engine.py",
        "components/trefoil-knot-blender/trefoil_engine.py",
        "components/hopf-fibration-regulator/hopf_engine.py",
        "components/catenoid-flow-regulator/catenoid_engine.py",
        "components/pseudospherical-regulator/pseudosphere_engine.py",
        "components/helicoid-flow-regulator/helicoid_engine.py",
        "components/paraboloidal-flow-regulator/paraboloid_engine.py",
        "components/hyperboloidal-flow-regulator/hyperboloid_engine.py",
        "components/hyperbolic-paraboloidal-regulator/saddle_engine.py",
        "components/klein-bottle-regulator/klein_engine.py",
        "components/cross-cap-flow-regulator/cross_cap_engine.py",
        "components/steiner-roman-regulator/roman_engine.py",
        "components/boy-surface-regulator/boy_engine.py",
        "components/schwarz-p-regulator/schwarz_engine.py",
        "components/gyroid-flow-regulator/gyroid_engine.py",
        "components/costa-surface-regulator/costa_engine.py",
        "components/chen-gackstatter-regulator/chen_engine.py",
        "components/lidinoid-flow-regulator/lidinoid_engine.py",
        "components/schwarz-d-regulator/schwarz_id_engine.py",
        "components/neovius-flow-regulator/neovius_engine.py",
        "components/flower-of-life-mesh/generate_fol_mesh.py",
        "components/cross-cap-regulator/cross_cap_engine.py",
        "components/outer-pressure-casing/casing_vectors.py",
        "components/end-cap-collars/collar_threads.py",
        "components/chiral-mesh-filter/chiral_engine.py",
        "components/toroidal-helical-diffuser/diffuser_vectors.py"
    ]
    
    success_count = 0
    total_stages = len(pipeline_steps)
    
    for step in pipeline_steps:
        if run_simulation_script(step):
            success_count += 1
        else:
            print("[⚠️] Pipeline execution interrupted due to stage structural imbalance.")
            sys.exit(1)
            
    print("=" * 70)
    print(f"🎉 PIPELINE COMPILED COMPLETELY: {success_count}/{total_stages} STAGES MATRIX PASSED")
    print("= SUCCESS: All multi-axial geometric modules mapped flawlessly. =")
    print("=" * 70)

if __name__ == "__main__":
    main()
    
