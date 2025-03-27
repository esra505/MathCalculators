# (c) 2025 Esra Marie M. Managbanag, Valerie Joyce C. Quigao
#  Load Distribution on a Beam

def main():
    uniform_load = float(input("Enter the uniform load of the beam (N/m): "))
    length = float(input("Enter the length of the beam (m): "))
    
    force = uniform_load * length 
    
    print(f"\nSo, the total load acting onthe beam is {force:.2f} N.")

if __name__ == "__main__":
    main()