
# Resume Screening Bot (ATS)

This project aims at building a software which can screen the applicant's resume based on certain keywords.


## Screenshots
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Resume-screening-bot/main/Screenshots/Screenshot_2022-09-25_20-03-33.png)
![App Screenshot](https://raw.githubusercontent.com/shaurya121/Resume-screening-bot/main/Screenshots/Screenshot_2022-09-25_19-56-50.png)



## Usage/Examples
Import the required modules:
```python
import PyPDF2
import re
import pandas as pd
```
Extract words from Resume (in PDF format):
```python
pdf_reader_obj=PyPDF2.PdfFileReader(pdf_obj)
text=''
for i in range(0, pdf_reader_obj.numPages):
    pageObj = pdf_reader_obj.getPage(i)
    text=text+pageObj.extractText()
```
 Display the count of keywords found:
```python
y = np.array(score_lst)
mylabels = list(dict_.keys())
plt.pie(y, labels = mylabels, autopct='%1.0f%%')
plt.show()
```

## Acknowledgements

 - [Resume Screening with Python](https://towardsdatascience.com/resume-screening-with-python-1dea360be49b)

