import pipeline

def main():
    print("""
    Region Selection

    Regions:
    - LWM: London Westminster (PM2.5, Nitrogen Dioxide)
    - NCC: Newcastle Centre (Ozone, PM2.5, Nitrogen Dioxide)
    - LEC: Leeds Centre (Ozone, PM2.5, Nitrogen Dioxide)
    """) # Prints options of regions along with the pollutants available
    selRegion = input("Select a region: ").upper() # Converts the user input to uppercase for ease of use in later code
    if selRegion not in ('LWM', 'NCC', 'LEC'): # Checks if user input is in this list of regions
        print("Error: That is not an available region.")
        main()
    else:
        print("""
    Time Selection

    Timescale:
    - Weekly
    - Monthly
        """) # If the user chooses an available region, move onto the timescale option
        selTime = input("Select a timescale: ").upper()
        if selTime not in ('WEEKLY', 'MONTHLY'):
            print("Error: That is not an available timescale.")
            main()
        else:
            print("""
        Mode Selection

        Timescale:
        - HTML (default)
        - HTML-OFFLINE (larger file size, doesn't need internet connection)
        - PNG
            """) # ... continues from timescale selection
            selMode = input("Select a mode: ").upper() # User input for output mode
            if selMode not in ('HTML', 'HTML-OFFLINE', 'PNG'): # HTML-OFFLINE includes the plotlyjs api into the HTML file, which bloats the filesize
                if selMode == "":
                    selMode = "HTML" # This is done as HTML is chosen as the default option
                    print(f"Pipeline: Preparing {selTime.lower()} data for region '{selRegion}' in mode '{selMode}'")
                    pipeline.prepare(selRegion, selTime, selMode) # All of the user's selections are sent to the data pipeline
                else:
                    print("Error: That is not an available timescale.")
                    main()
            else:
                print(f"Pipeline: Preparing {selTime.lower()} data for region '{selRegion}' in mode '{selMode}'")
                pipeline.prepare(selRegion, selTime, selMode)

if __name__ == "__main__":
    main()