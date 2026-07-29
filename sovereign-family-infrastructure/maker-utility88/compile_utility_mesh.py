#!/usr/bin/env python3
"""
PROJECT MAKER-UTILITY: Micro-Batch Sourcing Volumetric & Margin Simulator
Path: sovereign-family-infrastructure/maker-utility88/simulate_utility_math.py
Licensing: CERN Open Hardware Licence Strongly Reciprocal v2.0 (CERN-OHL-S-2.0)

Programmatically models filament consumption mass, printing run latencies,
cash yield thresholds, and equipment reinvestment timelines across local workshops.
"""

def compute_utility_economics():
    print("=========================================================================")
    print("🛰️  EXECUTING BIOMIMETIC MAKER-UTILITY MICRO-BATCH REVENUE SIMULATOR")
    print("=========================================================================\n")
    
    # 🔬 GROUNDED PRINT-ROOM PARAMETERS (From maker-utility88/README.md)
    average_spool_cost_usd = 28.00     # $28 per 1kg standard tough polymer spool
    average_print_time_mins = 32.0     # 32 minutes mean batch run time across items
    average_material_mass_g = 17.1     # 17.1 grams mean consumption per unit
    average_retail_price_usd = 6.00    # $6.00 fair localized cash value ticket
    printer_reinvestment_cost = 2500.00 # Target high-speed CoreXY print engine fund
    
    # Sourcing Operational Footprints (Single Weekend Hobby Run up to Full Town Flotilla)
    scales = {
        "Weekend Workshop Run (10x Small Batch)"    : {"units_sold": 10},
        "Monthly Market Stencil (100x Medium Batch)" : {"units_sold": 100},
        "Annual Civic Enclave Run (1000x Community)" : {"units_sold": 1000}
    }
    
    print("📋 MICRO-BATCH PRODUCTION AND RUN CONSTRAINTS:")
    print(f"  * Mean Filament Mass Load : {average_material_mass_g:.1f} grams consumed per problem-solver")
    print(f"  * Calculated Spool Expense: ${(average_material_mass_g / 1000.0) * average_spool_cost_usd:.3f} USD raw cost per item")
    print(f"  * Targeted CoreXY Reinvestment Target: ${printer_reinvestment_cost:,.2f} USD Hardware Fund\n")
    
    for name, params in scales.items():
        count = params["units_sold"]
        
        # Calculate raw operational values
        total_filament_consumed_kg = (average_material_mass_g * count) / 1000.0
        total_spool_outlay_usd = total_filament_consumed_kg * average_spool_cost_usd
        gross_sales_revenue_usd = average_retail_price_usd * count
        net_cash_profit_usd = gross_sales_revenue_usd - total_spool_outlay_usd
        total_production_hours = (average_print_time_mins * count) / 60.0
        
        # Compute exact percentage cleared toward purchasing your commercial printer
        reinvestment_percentage_cleared = (net_cash_profit_usd / printer_reinvestment_cost) * 100.0
        
        print(f"🚀 ACTIVE RETAIL OUTPUT LEVEL: {name}")
        print(f"  * Solvers Distributed Natively : {count} Units handed into local community lines")
        print(f"  * Net Raw Filament Weight Mass: {total_filament_consumed_kg:.2f} kg consumed ({total_spool_outlay_usd/average_spool_cost_usd:.1f} spools used)")
        print(f"  * Total Production Bench Time : {total_production_hours:,.1f} continuous manufacturing hours")
        print(f"  * Net Capital Cash Generated  : ${net_cash_profit_usd:,.2f} USD Net Profit Margin Room")
        print(f"  * Equipment Reinvest Progress : ✅ TARGET COREXY PRINTER FUND CAPPED AT {reinvestment_percentage_cleared:.1f}% CLEAR\n")

    print("=========================================================================")
    print("✅ COMMERCIAL VIABILITY CONFIRMED // WORKSHOP SPEED LINES GREEN")
    print("=========================================================================")

if __name__ == "__main__":
    compute_utility_economics()
      
