1.environment: 
python 3.7
2. installation:
1) jupyter notebook: 
pip install notebook
or
conda install -c conda-forge notebook
2)packages:
pip install nltk
pip install pandas
pip install matplotlib
pip install numpy
pip install spacy

3.2
most frequent noun-adj pair:
simply run all cells in 3.2 noun-adj pair .ipynb on jupyter notebook
pos tagging:
simply run all cells in pos tagging.ipynb on jupyter notebook
Tokenization code: A1.py
(1)enter command line interface:
$ pip3 install nltk matplotlib
(2)Enter Python 3 environment and download corpus
>>> import nltk
>>> nltk.download()
(3)In order to demo the result, I randomly select a business with business_id:PEnMU_He_qHoCfdoAKmjDQ(line 23)
Comment line 23 and uncomment line 22 to get random every run time

3.3 Development of a Simple Search Engine
Download Apache Lucene 8.10.0 zip file using the first link below and unzip it. Download json-20210307.jar file using the second link below. Put the LuceneTester.java, QAIndexer.java and AQSearcher.java files in a same folder. 

To run our search engine in a terminal, you need first move Lucene jar files(lucene-core, lucene-analyzers-common) and json-20210307 jar file to your Java jre/lib/ext folder. Change the current working directory to the location you put the three java files in the terminal. Run "javac LuceneTester.java" command. Then type "java LuceneTester" in the command line and the program would start.

To run our search engine in Eclipse, you need to create a project and import the three java files. Add Lucene jar files(lucene-core, lucene-analyzers-common) and json-20210307 jar file to your project as external JARs. Then you can start to run the program.

Our search engine will first prompt and ask the search content. You can type a single keyword query, a boolean query or a phrase query. Then the program will ask you how many results you'd like to return. You can type a positive integer N. It will return the Top-N results. Next it would ask you how would you like to rank your results. Type 0 will rank by Lucene's scores; type 1 will rank by stars; type 2 will rank by useful; type 3 will rank by funny; type 4 will rank by cool. Since our search engine can search in text field, date field and business_id field, it would ask you three times to rank your results and return results in each field separately. If there's no results returned for a field, it means the search engine cannot find any related things in this field. Detailed examples are shown in Appendix.

Lucene Download Link: https://archive.apache.org/dist/lucene/java/8.10.0/
Json Download Link: https://repo1.maven.org/maven2/org/json/json/20210307/

3.4 Extraction of Indicative Adjective Phrases
To run the python program, you need first put the file, 'yelp_academic_dataset_review.json', and the python file,'ExtractAdjPhrases.py' in the same folder. Then download averaged_perceptron_tagger.zip file to your python path Pythonxx/Lib/nltk_data/taggers folder and punkt.zip file to your Pythonxx/Lib/nltk_data/tokenizers folder, and then unzip them. Make sure you have installed the nltk package. Then type "python ExtractAdjPhrases.py" in the command line and the program would start.
Our program will first prompt and ask the business_id. You can make your choice according to the prompt. There will be some prompt and results displayed in the terminal if the business_id is correct.
averaged_perceptron_tagger.zip: https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/taggers/averaged_perceptron_tagger.zip
punkt.zip: https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip