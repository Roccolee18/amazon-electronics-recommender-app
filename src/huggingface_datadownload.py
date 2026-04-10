import argparse
import requests
from tqdm import tqdm
from pathlib import Path
import os
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


def download_request(specific_url, output, filename):
    fullpath = os.path.join(output, filename)

    if fullpath.exists(): # prevent from a taxing re-download
        print(f"Already exists, skipped: {filename}")
        return

    print(f"Downloading: {filename}")
    request = requests.get(specific_url, stream=True) #
    request.raise_for_status()

    # Following code below that handles request-downloads is from Claude as it's a nice-to-have and out of scope of assignment
    total = int(request.headers.get("content-length", 0))
    with open(fullpath, "wb") as f, tqdm(
        total=total, unit="B", unit_scale=True, unit_divisor=1024, desc=fullpath.name
    ) as bar:
        for chunk in request.iter_content(chunk_size=1024 * 1024):  # 1 MB chunks
            f.write(chunk)
            bar.update(len(chunk))

    print(f"Saved: {filename} in {output}")


if __name__ == "__main__":
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True) # in case someone just deletes the whole folder

    files_map = file_name_source_map(args.base_url,args.subset, args.meta, args.reviews)
    for filename, specific_url in files_map.items():
        print(f"Request to download: {filename}")
        download_request(specific_url, out_dir, filename)
    print("All raw files downloaded")