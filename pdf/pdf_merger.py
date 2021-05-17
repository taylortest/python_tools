from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

def merge_pdfs(file_odd, file_even, output):
    '''
    Assume file_odd is in ascending order, e.g. 1,3,5,7,9
    file_even is in descending order, e.g. 10,8,6,4,2
    [param]
    file_odd -- path of odd pages
    file_even -- path of even pages
    output -- path of output
    [return]
    None
    '''

    merged = PdfFileWriter()

    file_odd_reader = PdfFileReader(file_odd)
    file_even_reader = PdfFileReader(file_even)
    
    page_count = file_odd_reader.getNumPages()

    for idx in range(page_count):
        merged.addPage(file_odd_reader.getPage(idx))
        merged.addPage(file_even_reader.getPage(page_count-idx-1))
    
    
    # Write out the merged PDF
    with open(output, 'wb') as out:
        merged.write(out)

    return


def main():
    '''
    Pathlib does not work here
    FILE_ODD = Path(__file__).parent / 'input' / 'odd_asc.pdf'
    FILE_EVEN = Path(__file__).parent / 'input' / 'even_desc.pdf'
    FILE_OUTPUT = Path(__file__).parent / 'output' / 'output.pdf'
    '''

    FILE_ODD = './input/odd_asc.pdf'
    FILE_EVEN = './input/even_desc.pdf'
    FILE_OUTPUT = './output/output.pdf'

    merge_pdfs(FILE_ODD, FILE_EVEN, FILE_OUTPUT)
    print('done')
    return

if __name__ == '__main__':
    main()