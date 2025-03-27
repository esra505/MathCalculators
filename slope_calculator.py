# (c) 2025 Esra Marie M. Managbanag, Valerie Joyce C. Quigao
#  Slope of a Road

def main():
    rise = float(input("Enter the rise of the road (m): "))
    run = float(input("Enter the horizontal distance of the road (m): "))
    
    slope = (rise / run) * 100
    
    print(f"\nSo, the slope of the road is {slope:.2f} %.")

if __name__ == "__main__":
    main()