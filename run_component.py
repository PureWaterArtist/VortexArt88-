import json
from transcendental_engine import build_regulator_matrix

def main():
    print("=" * 60)
    print("INITIALIZING: π/Φ TRANSCENDENTAL FLOW REGULATOR")
    print("=" * 60)
    
    # Define physical scaling constraint
    component_scale = 1.0 
    resolution_steps = 360
    
    print(f"[*] Extracting geometric layers at scale factor: {component_scale}")
    print(f"[*] Calculating vector paths across {resolution_steps} points of rotation...")
    
    # Execute calculations from the engine file
    structural_matrix = build_regulator_matrix(component_scale, resolution_steps)
    
    # Isolate a snapshot of the midpoint to verify inversion balance
    midpoint_sample = structural_matrix[180]
    
    print("\n[+] SUCCESS: Alignment matrix compiled successfully.")
    print(f"[-] Structural nodes created: {len(structural_matrix)}")
    print(f"[-] Midpoint Core Alignment Check (Step 180):")
    print(f"    ↳ Outer Channel Path (X, Y, Z): {midpoint_sample['outer_stream']}")
    print(f"    ↳ Inner Channel Path (X, Y, Z): {midpoint_sample['inner_stream']}")
    print("=" * 60)

if __name__ == "__main__":
    main()
  
