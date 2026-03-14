"""
Industrial Weigh Feeder: Interactive TPH & Control Calculator
Author: Prince
Description: A functional tool to calculate TPH, 4-20mA signals, and VFD scaling.
"""

def calculate_tph(belt_load, belt_speed):
    # Formula: TPH = Load (kg/m) * Speed (m/s) * 3.6 [cite: 48]
    return belt_load * belt_speed * 3.6

def map_tph_to_current(current_tph, max_tph):
    # Formula: 4 + (Current/Max) * 16 [cite: 59]
    return 4 + (current_tph / max_tph) * 16

def calculate_vfd_frequency(current_freq, current_tph, target_tph):
    # Proportional Scaling for VFD [cite: 63]
    return current_freq * (target_tph / current_tph)

if __name__ == "__main__":
    print("--- Industrial Weigh Feeder Interactive Tool ---")
    
    try:
        # User Inputs
        load = float(input("Enter Belt Load (kg/m): "))
        speed = float(input("Enter Belt Speed (m/s): "))
        
        # 1. TPH Output
        tph = calculate_tph(load, speed)
        print(f"\n[RESULT] Calculated Flow Rate: {tph:.2f} TPH")

        # 2. Signal Mapping
        max_cap = float(input("\nEnter Maximum System Capacity (TPH): "))
        ma_signal = map_tph_to_current(tph, max_cap)
        print(f"[RESULT] Analog Signal to PLC/DCS: {ma_signal:.2f} mA")

        # 3. Control Logic
        target = float(input("\nEnter Target TPH for the process: "))
        current_f = float(input("Enter Current VFD Frequency (Hz): "))
        new_f = calculate_vfd_frequency(current_f, tph, target)
        print(f"[RESULT] Adjust VFD Frequency to: {new_f:.2f} Hz")

    except ValueError:
        print("Error: Please enter valid numerical data.")
    except ZeroDivisionError:
        print("Error: Current TPH cannot be zero for frequency scaling.")
