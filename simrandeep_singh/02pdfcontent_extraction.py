# miner_text_generator.py

import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
from PyPDF2 import PdfFileReader
import io
from tika import parser
yearstart= 1997

filename = str(yearstart) + ".txt"
url2=[]
file1 = open("listfile.txt", encoding="utf-8")
line = file1.read()
words= line.split()
for x  in words:
      print(x)
           
      if(x=="thisyearends"):
                 yearstart= yearstart+1
                 filename= str(yearstart) + ".txt"
                 continue
      
      
            
    
      url= x
      url1= url[:-3]
      url2= "https://www.bis.org" + url1 + "pdf"
      def extract_text_by_page(pdf_path):
          response = requests.get(pdf_path)
          with io.BytesIO(response.content) as fh:
              for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=False):
                  resource_manager = PDFResourceManager()
                  fake_file_handle = io.StringIO()
                  converter = TextConverter(resource_manager, fake_file_handle)
                  page_interpreter = PDFPageInterpreter(resource_manager, converter)
                  
                  try:
                        pass
                        page_interpreter.process_page(page)
                  except:
                        print("Error Occured for pdf "+ pdf_path )
                           
                  text = fake_file_handle.getvalue()
                  yield text
    
                  # close open handles
                  converter.close()
                  fake_file_handle.close()
    
      def extract_text(pdf_path,filepath):
            with open(filepath, mode='a',encoding='utf-8') as f:
                  for page in extract_text_by_page(pdf_path):
                        f.write("%s\n" % page)
            
             
      if __name__ == '__main__':
         extract_text(url2,filename)

      
      
