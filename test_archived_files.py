import os
import zipfile
import wget

pdffile_url = 'https://www.quickpickdeal.com/files/SamplePdf_61kb_1page.pdf'
xlsxfile_url = 'https://www.quickpickdeal.com/files/Sample_Employee_data_xlsx.xlsx'
csvfile_url = 'https://www.quickpickdeal.com/files/Sample100.csv'

def test_download_n_archive_files():
    wget.download(pdffile_url, 'hw07.pdf')
    wget.download(xlsxfile_url, 'hw07.xlsx')
    wget.download(csvfile_url, 'hw07.csv')

    pdffile_withpath = os.path.abspath("hw07.pdf")
    xlsxfile_withpath = os.path.abspath("hw07.xlsx")
    csvfile_withpath = os.path.abspath("hw07.csv")

    uncompressed_pdf_size = os.path.getsize(pdffile_withpath)
    uncompressed_xlsx_size = os.path.getsize(xlsxfile_withpath)
    uncompressed_csv_size = os.path.getsize(csvfile_withpath)

    archfiles = [os.path.basename(pdffile_withpath),
                os.path.basename(xlsxfile_withpath),
                os.path.basename(csvfile_withpath)]
    archname = "archive.zip"

    with zipfile.ZipFile(archname, "w") as zf:
        for file in archfiles:
            zf.write(file)

    with zipfile.ZipFile(archname, "r") as zf:
        zipfile_list = zf.namelist()

        pdfzipfile_size = zf.getinfo(zipfile_list[0]).file_size
        xlsxzipfile_size = zf.getinfo(zipfile_list[1]).file_size
        csvzipfile_size = zf.getinfo(zipfile_list[2]).file_size

    assert pdfzipfile_size == uncompressed_pdf_size
    assert xlsxzipfile_size == uncompressed_xlsx_size
    assert csvzipfile_size == uncompressed_csv_size