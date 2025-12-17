#import necessary modules
import sys
import os
import inspector
import Document_Scanner  
import virtual_id_card   

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n=========================================")
        print("   OPENCV COMPUTER VISION TOOLKIT v1.0")
        print("=========================================")
        print("1. Real-Time Inspection (Webcam)")
        print("2. Document Scanner (Perspective Warp)")
        print("3. Synthetic ID Generator (ROI & Shapes)")
        print("q. Quit")
        
        choice = input("\nSelect Module [1-3]: ").lower()

        try:
            if choice == '1':
                print("Launch: Inspector... (Press 'q' to return)")
                inspector.run()
            elif choice == '2':
                print("Launch: Document Scanner...")
                Document_Scanner.run()
            elif choice == '3':
                print("Launch: ID Generator...")
                virtual_id_card.run()
            elif choice == 'q':
                print("Exiting Toolkit.")
                break
            else:
                print("[ERROR] Invalid selection. Please try again.")
                input("Press Enter to continue...")
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to menu...")

if __name__ == "__main__":
    main()