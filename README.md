# DSCI_575_project_dianacor_roccolee


```

python src/convert_parquet.py \
  --reviews data/raw/Electronics.jsonl.gz \
  --meta data/raw/meta_Electronics.jsonl.gz \
  --out-dir data/processed \
  --row_limit 20000 \
  --subset_sample_size 500 
  # add the col extra arguments
```