from pathlib import Path
import datetime
import time

def main():
    '''
    rename and place the files from INPUT_PATH TO OUTPUT_PATH
    '''
    
    
    INPUT_PATH = Path('./input')
    OUTPUT_PATH = Path('./output')

    for f in INPUT_PATH.glob('./*.gz'):
        new_name = 'my_prefix' + '_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + f.name
        #print(new_name)
        f.rename(Path(OUTPUT_PATH, new_name))
        time.sleep(2)
    print('done')

    return

if __name__ == '__main__':
    main()