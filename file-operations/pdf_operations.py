# Use PyPDF2 library to work with pdf files
# It can only read text content, not the images and other media content
import PyPDF2

# read as binary file
pdf_file = open("The-Road-to-Learn-React-Robin.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

print("Number of pages in the pdf file:", pdf_reader.numPages)

# 0 based index
grab_a_page = pdf_reader.getPage(10)

print("Content of a given page is:", grab_a_page.extractText())

# # It allows to append an page to end but hard to add content to any page
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(grab_a_page)

# Write the page 101 to a new file, it creates a new file
# output_file = open("new_pdf_file.pdf", "wb")
# pdf_writer.write(output_file)

pdf_file.close()
# output_file.close()
