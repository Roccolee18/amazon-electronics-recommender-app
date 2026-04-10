import argparse
import requests
from tqdm import tqdm
from pathlib import Path

# pip install requests tqdm

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--base_url",  
                   default="https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw", 
                   help="Download base URL source")
    p.add_argument("--out-dir",  
                   default="data/raw", 
                   help="Directory to save downloaded files.")
    p.add_argument("--subset",   
                   default="Electronics", 
                   help="Category subset to download (e.g. Electronics, Books).")
    p.add_argument("--meta",     
                   action=argparse.BooleanOptionalAction,  #Mentioned by Clause to properly parse True/False flag for downloading 
                   default=True, 
                   help="Download the meta file.")
    p.add_argument("--reviews",  
                   action=argparse.BooleanOptionalAction, 
                   default=True, 
                   help="Download the reviews file.")
    return p.parse_args()

def file_name_source_map(base_url, subset, meta, reviews):
    files = {}
    if reviews:
        files[f"{subset}.jsonl.gz"] = f"{base_url}/review_categories/{subset}.jsonl.gz" # to match the same file naming as if manually downloaded from website
    if meta:
        files[f"meta_{subset}.jsonl.gz"] = f"{base_url}/meta_categories/meta_{subset}.jsonl.gz" # to match the same file naming as if manually downloaded from website
    return files


def download(url, output, filename):
    pass

if __name__ == "__main__":
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True) # in case someone just deletes the whole folder

    files = file_name_source_map(args.subset, args.meta, args.reviews)
    for filename, url in files.items():
        print(f"Downloading: {filename}")
        download(url, output, filename)
    print("All raw files downloaded")