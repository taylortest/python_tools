from pathlib import Path
import pandas as pd
import csv

def main():
    INPUT_PATH = Path('./input')
    OUTPUT_PATH = Path('./output')

    for f in INPUT_PATH.glob('./*.xlsx'):
        print('working on: ' + str(f))

        df = pd.read_excel(f, dtype = str, na_filter=False)
        print(df.head())
        df.to_csv(str(OUTPUT_PATH / str(f.stem + ".csv")), encoding='utf-8', index=False, header=True, quoting=csv.QUOTE_ALL) # quoting=csv.QUOTE_ALL -- add double-quotes

    print('done')

    return

if __name__ == '__main__':
    main()