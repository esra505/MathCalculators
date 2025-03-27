# (c) 2025 Esra MarieM. Managbanag, Valerie Joyce C. Quigao
# Cement Slurry Dilution

def main():
    volume_2 = float(input("Enter the final volume (L): "))
    concentration_1 = float(input("Enter initial concentration (g/L): "))
    concentration_2 = float(input("Enter final concentration (g/L): "))
    volume_1 = (concentration_2 * volume_2) / concentration_1
    
    print(f"\nSo, you need {volume_1:.2f} liters of the original slurry.")

if __name__ == "__main__":
    main()