import pipeline

'''
1. Take data from csv
2. Compile daily data into weeks or months
3. Turn into a graph
'''

def main():
    print("""
    Welcome

    Regions:
    - LWM: London Westminster (PM2.5, Nitrogen Dioxide)
    """)
    selRegion = input("Select a region: ").upper()
    if selRegion not in ('LWM'):
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
            print(f"Pipeline: Preparing {selTime.lower()} data for region '{selRegion}'")
            pipeline.prepare(selRegion, selTime)

main()