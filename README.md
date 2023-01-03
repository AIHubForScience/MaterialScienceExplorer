<h1 align="center">MaterialsScienceExplorer</h1>
<h3 align="center">Text-mined Academic Interests in Materials Science</h3>

</p>


This study is a successful example :star2: of applying natural language processing and unsupervised learning for materials science trend analysis. 
We applied the document embedding and density-based clustering to materials science literature.
We obtained the comprehensive understanding of scientific topics in materials science without any insertion of expertise.
We defined the topic relevance of each paper and identified main topics and academic interests of organisations in a quantitative and time-aware manner.
This repository contains the source code and dataset for the following publication:
- :page_facing_up: [Text-mined academic interests in materials science](Link) accepted in .

## Dataset
Dataset used in this study is available [here](Link), and unzip in your own directory.

- temp_mat_abstract.txt : Sample of the abstract of materials science literature used in this study, which is published between 2017 and 2021.

- temp_mat_bib.txt : Sample of the bibliographic information of the collected papers, of which columns are doi, title, journal, year.

## Requirements
Our experiment setting is as follows:

- gensim : 4.1.2

- spacy : 3.2.4

- hdbscan : 0.8.28

```bash
pip install -r requirements.txt
```
## Run

```bash
python code/run.py -dataset <dataset>
```



## Visualization

**Topic Map of Materials Science**

![](./image/embd.png)

**National Interests of Materials Science**



**Heatmap of Nature Materials**




## Tutorial
**Coming soon!**


## Citation
If you utilise our findings, methods, or results, please consider citing the following paper.
- Choi, J., & Lee, B.* (2023). Text-mined academic interests in materials science [(Link)]()
