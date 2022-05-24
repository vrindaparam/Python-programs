import PyPDF2

def extract_text(pdfReader, num_pages):
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    return {
        'code': 200,
        'message': 'Raw Text is extracted from the provided PDF file.',
        'text': text
    }

def main():
    filename = "RBC-10_questions_for_first_home-buyers.pdf"

    pdfFileObj = open(filename,'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    num_pages = pdfReader.numPages

    text = extract_text(pdfReader, num_pages)
    print(text)


if __name__ == "__main__":
    main()