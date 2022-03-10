from asyncio.windows_events import NULL
import time


while True:
    file = NULL
    
    progress = 0
    
    # This means Percent Progress it's meant to go from 0-20
    percentP = 0
    
    print("\n" * 50, "=========Tyler's Download Simulation=========", "\n" * 3)

    # Determines the fake file's size
    file = input("Enter a file size: ")

    # Determines how fast the fake file will download
    dSpeed = input("Enter a download speed (Default: 1): ")

    # If file variable is valid this block of code wil run
    try:
        # Turns the string varibles into float varibles.
        file = float(file)
        dSpeed = float(dSpeed) / 100

        print("\n" * 50)
        print("Downloading File...")
        
        # At it's base, this means 5 percent of file variable.
        percent = file * 0.05

        # Giant wall of most likly unnessasary code incoming!
        while percentP < 20:
            progress = progress + dSpeed

            

            # Triggers if progress value is 5 percent of file variable
            if progress >= percent and percentP == 0:
                print("FILE IS 5% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 10 percent of file variable
            elif progress >= percent * 2 and percentP == 1:
                print("FILE IS 10% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 15 percent of file variable
            elif progress >= percent * 3 and percentP == 2:
                print("FILE IS 15% INSTALLED")
                percentP = percentP + 1

            # Triggers if progress value is 20 percent of file variable
            elif progress >= percent * 4 and percentP == 3:
                print("FILE IS 20% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 25 percent of file variable
            elif progress >= percent * 5 and percentP == 4:
                print("FILE IS 25% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 30 percent of file variable
            elif progress >= percent * 6 and percentP == 5:
                print("FILE IS 30% INSTALLED")
                percentP = percentP + 1
                
            # Triggers if progress value is 35 percent of file variable
            elif progress >= percent * 7 and percentP == 6:
                print("FILE IS 35% INSTALLED")
                percentP = percentP + 1

            # Triggers if progress value is 40 percent of file variable
            elif progress >= percent * 8 and percentP == 7:
                print("FILE IS 40% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 45 percent of file variable
            elif progress >= percent * 9 and percentP == 8:
                print("FILE IS 45% INSTALLED")
                percentP = percentP + 1
                
            # Triggers if progress value is 50 percent of file variable
            elif progress >= percent * 10 and percentP == 9:
                print("FILE IS 50% INSTALLED")
                percentP = percentP + 1


            # Triggers if progress value is 55 percent of file variable
            elif progress >= percent * 11 and percentP == 10:
                print("FILE IS 55% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 60 percent of file variable
            elif progress >= percent * 12 and percentP == 11:
                print("FILE IS 60% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 65 percent of file variable
            elif progress >= percent * 13 and percentP == 12:
                print("FILE IS 65% INSTALLED")
                percentP = percentP + 1

            # Triggers if progress value is 70 percent of file variable
            elif progress >= percent * 14 and percentP == 13:
                print("FILE IS 70% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 75 percent of file variable
            elif progress >= percent * 15 and percentP == 14:
                print("FILE IS 75% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 80 percent of file variable
            elif progress >= percent * 16 and percentP == 15:
                print("FILE IS 80% INSTALLED")
                percentP = percentP + 1
                
            # Triggers if progress value is 85 percent of file variable
            elif progress >= percent * 17 and percentP == 16:
                print("FILE IS 85% INSTALLED")
                percentP = percentP + 1

            # Triggers if progress value is 90 percent of file variable
            elif progress >= percent * 18 and percentP == 17:
                print("FILE IS 90% INSTALLED")
                percentP = percentP + 1
            
            # Triggers if progress value is 95 percent of file variable
            elif progress >= percent * 19 and percentP == 18:
                print("FILE IS 95% INSTALLED")
                percentP = percentP + 1
                
            # Triggers if progress value is 100 percent of file variable
            elif progress >= percent * 20 and percentP == 19:
                print("FILE IS 100% INSTALLED")
                percentP = percentP + 1           
            time.sleep(0.01)

        #Triggers if fake download is completed
        if percentP == 20:
            print("\nDownload Completed!")
            time.sleep(3)

    # If file variable is invalid than an error message will play
    except:
        print("\nERROR! One of your responses was invalid. Please enter a number and ONLY the number.")
        time.sleep(2)
        print("\n" * 50)
        

    exit = input("Enter <y> if you want to exit: ")
            
    if exit == "y":
        break
