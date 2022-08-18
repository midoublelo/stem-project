import pipeline

'''
1. Take data from csv
2. Compile daily data into weeks or months
3. Turn into a graph
'''

def main():
    print("""
    Region Selection

    Regions:
    - LWM: London Westminster (PM2.5, Nitrogen Dioxide)
    - NCC: Newcastle Centre(Ozone, PM10, PM2.5, Nitrogen Dioxide)
    """)
    selRegion = input("Select a region: ").upper()
    if selRegion not in ('LWM', 'NCC'):
        print("Error: That is not an available region.")
        main()
    else:
        print("""
    Time Selection

    Timescale:
    - Weekly
    - Monthly
        """)
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
            """)
            selMode = input("Select a mode: ").upper()
            if selMode not in ('HTML', 'HTML-OFFLINE', 'PNG'):
                if selMode == "":
                    selMode = "HTML"
                    print(f"Pipeline: Preparing {selTime.lower()} data for region '{selRegion}' in mode '{selMode}'")
                    pipeline.prepare(selRegion, selTime, selMode)
                else:
                    print("Error: That is not an available timescale.")
                    main()
            else:
                print(f"Pipeline: Preparing {selTime.lower()} data for region '{selRegion}' in mode '{selMode}'")
                pipeline.prepare(selRegion, selTime, selMode)

main()