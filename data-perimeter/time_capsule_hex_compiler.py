# =============================================================================
# TIME CAPSULE DEEP-ARCHIVE HOUSING: HEXADECIMAL COMPILER ENGINE v1.0
# License: Open Source Hardware Association (OSHWA) Compliant / Copyleft
# Description: Converts text-based source files into a structured hex data
#              stream formatted to your strict 80-character margin limits.
# Format: Strict 80-Character Margin Constraints for Mobile Scannability
# =============================================================================

class HexTimeCapsuleCompiler:
    def __init__(self, line_character_limit=80):
        self.margin_limit = line_character_limit

    def compile_text_to_hex_stream(self, input_text_string):
        """Converts raw characters into sequential hexadecimal block arrays."""
        # Convert text string directly into raw byte tokens
        byte_data = input_text_string.encode('utf-8')
        
        # Translate bytes to raw hex string pairs
        raw_hex_string = byte_data.hex().upper()
        
        # Split the continuous stream into strict scannability columns
        formatted_lines = []
        chunk_size = self.margin_limit - 4  # Reserve space for line prefixes
        
        for i in range(0, len(raw_hex_string), chunk_size):
            line_chunk = raw_hex_string[i:i+chunk_size]
            # Group into clean pairs of bytes for easier optical scanning
            paired_chunk = " ".join(line_chunk[j:j+2] 
                                    for j in range(0, len(line_chunk), 2))
            formatted_lines.append(f"HEX> {paired_chunk}")
            
        return "\n".join(formatted_lines)

# =============================================================================
# EXECUTING TELEMETRY RAW DATA TRANSLATION LOOP
# =============================================================================
if __name__ == "__main__":
    compiler = HexTimeCapsuleCompiler(line_character_limit=80)
    
    # Test Payload: Your locked-in core 42.5-degree refraction constant profile
    test_payload = "PAVG REFRACTION BASELINE CONSTANT VECTOR VALUE = 42.500000"
    
    hex_output_stream = compiler.compile_text_to_hex_stream(test_payload)
    
    print("=====================================================================")
    print("        TIME CAPSULE ARCHIVE NODE: RAW HEXADECIMAL STREAM            ")
    print("=====================================================================\n")
    print(hex_output_stream)
    print("\n=====================================================================")
      
