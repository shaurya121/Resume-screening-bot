import PyPDF2
import re
import pandas as pd
from IPython.display import display		# to display in tabular form
import matplotlib.pyplot as plt
import numpy as np

file_loaction="/home/shaurya/Desktop/Downloads/Roberto Salazar - Resume.pdf"
# creating a pdf file object
pdf_obj = open(file_loaction, 'rb')
# creating a pdfReader object
pdf_reader_obj=PyPDF2.PdfFileReader(pdf_obj)
# storing text of pdf file, page-by-page
text=''
for i in range(0, pdf_reader_obj.numPages):
    # creating a page object
    pageObj = pdf_reader_obj.getPage(i)
    # extracting text from page
    text=text+pageObj.extractText()
# Convert all strings to lowercase
text = text.lower()
# removing digits
text=re.sub(r"[\d]+", " ", text)
#text=re.sub(r"[^A-Za-z0-9 @\w.\w]", " ", text)
text=re.sub(r"[ ]+", " ", text)

# skills
dict_={'PROGRAMMING': ['c#', 'java', 'python', 'c++', 'r', 'ruby', 'scala', 'go', 'c'], 
		'SOFT SKILLS': ["time management", "communication", "adaptability", "problem solving", "teamwork", "creativity", "leadership", "interpersonal skills", "redesigned"],
		'DATA SCIENCE': ['analytics', 'api', 'aws', 'big data', 'clustering','code','data mining', 'deep learning', 'hadoop',
                          'hypothesis test' ,'machine learning','modeling', 'nlp','predictive', 'tableau', 'text mining', 'visualuzation'],
        'WEB DEVELOPMENT': ['css', 'sql', 'javascript', 'web development', 'php', 'html', 'mysql', 'jquery', 'html5', 'laravel', 'wordpress', 'bootstrap',
							'web design', 'react.js', 'agile', 'node.js']}

# score counters
score_lst=[]
programming=0
soft_skills=0
data_science=0
web_development=0
for key in dict_.keys():
	if key=='PROGRAMMING':
		for y in dict_[key]:
			if y in text:
				programming+=1
		score_lst.append(programming)
	elif key=='SOFT SKILLS':
		for y in dict_[key]:
			if y in text:
				soft_skills+=1
		score_lst.append(soft_skills)
	elif key=='DATA SCIENCE':
		for y in dict_[key]:
			if y in text:
				data_science+=1
		score_lst.append(data_science)
	elif key=='WEB DEVELOPMENT':
		for y in dict_[key]:
			if y in text:
				web_development+=1
		score_lst.append(web_development)
		
# visualizing in tabular form
dataframe_dict={"SKILL": list(dict_.keys()),
				"SCORE": score_lst}
summary = pd.DataFrame(dataframe_dict)
display(summary)

# showing a pie chart
y = np.array(score_lst)
mylabels = list(dict_.keys())
plt.pie(y, labels = mylabels, autopct='%1.0f%%')
plt.show()




