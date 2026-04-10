# DSCI_575_project_dianacor_roccolee

Data set up process:
1. manually download the data from the website (link), both the reviews and meta
2. move zip files to the data/raw directory
3. export files in the same directory
4. run bellow code to convert from .jsonl / .json.gz to parquet

```

python src/convert_parquet.py \
  --reviews data/raw/Electronics.jsonl.gz \
  --meta data/raw/meta_Electronics.jsonl.gz \
  --subset_sample_size 500 
  # add the col extra arguments
```

5.