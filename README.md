# Amazon Electronics Review Search

This repo uses data of Amazon product & their reviews (specifically for the Electronics category) to compare 2 different retrievals systems: BM25 (keyword-based) and Semantic (embedding-based), to search and compare product results via user queries.

## Description of Dataset

This project uses the [Amazon Reviews 2023](https://amazon-reviews-2023.github.io/) dataset, focusing on the **Electronics** category. This can also be found in [Hugging Face Website]( https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-202). It combines two data sources:

- **Reviews** (`Electronics.jsonl.gz`): dataset of individual user reviews with fields including `rating`, `text`, `asin`, `parent_asin`, `user_id`, `timestamp`, `helpful_vote`, and `verified_purchase`
- **Metadata** (`meta_Electronics.jsonl.gz`): dataset of product-level information including `title`, `price`, `average_rating`, `main_category`, and `store`

These two sources are joined on `parent_asin` to produce a merged dataset (reproducing the work flow instructions below). 

### Preprocessing:

Via EDA done in `milestone_exploration.ipynb`, some columns were dropped or converted in a more palatable way for document creation/pipeline requirements. More explanation can be found there. 

In short: the following columns were dropped in meta `["images", "videos", "subtitle", "author", "bought_together", "rating_number", "average_rating", "price", "store"]` and only `["title", "helpful_vote", "parent_asin"]` was retained in reviews. The dropped columns either do not work well in the retrieval pipeline without serious extra steps (images/videos) or would increase the document size without meaningful additions. The second reason (lack of meaningful additions) is also the main reason why so many of the review columns were dropped - as the document size would explode - but only add noise.

## Current Types of Retrieval Systems:

Currently there are 2 types of retrieval systems being explored:
1. BM25 -> Keyword TF-IDF based. Expected to preform the best when there's high exact-word matching between a query and the products.
2. Semantic -> Embedding-based. Expected to preform the best when there's a more abstract query and the products semantic best match the overall meaning and intent of the user query.

Comming soon:
- Hybrid of BM25 and Semantic
- RAG

## Recreating Project Workflow

1. Clone the repo into the desired folder using this command in a new terminal window:
```bash
git clone git@github.com:UBC-MDS/DSCI_575_project_dianacor_roccolee.git
```

2. Make and activate the enviroment using the command below in the same terminal: 
```bash
conda env create -f environment.yml 
```

3. Download the data set by running (assuming you are in the root project directory) 
```bash 
python ./src/direct_datadownload.py
``` 
or alternatively:
1. Manually download the data from [here](https://amazon-reviews-2023.github.io/)
- Download both the reviews and meta of the *Electronics* category
2. Move zip files to the data/raw directory
3. Extract (unzip) files in the same directory
- This will take very long to download. Please be patient, (ETA 45-1hr, + longer from the direct download method b/c of the server bottleneck)

4. Run bellow code to convert from .jsonl / .json.gz to parquet
```bash
python src/convert_parquet.py \
  --reviews data/raw/Electronics.jsonl.gz \
  --meta data/raw/meta_Electronics.jsonl.gz \
  --subset_sample_size 500 
```
- By default, the parquet file output will be saved in `./data/processed`
- this will take a while (~ 10mins)

4. Create documents from the data set using:
```bash
python src/create_documents.py
```

5. To use BM25 search, run the `bm25.py` file with the appropriate arguments, or just call it plainly to use default arguments
```bash
python ./src/bm25.py --query "sony headphones"
```

6. To use semantic search, run the `semantic.py` fule with the appropriate arguments, or just call it plainly to use default arguments
```bash
python ./src/semantic.py --query "sony headphones"
```

7. Alternatively, experiment with the search through a web app by running:
```bash
shiny run ./app/app.py
```