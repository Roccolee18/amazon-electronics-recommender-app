# Final Discussion

## Step 1: Improve Your Workflow

### Dataset Scaling
- Number of products used - 10,000
- Changes to sampling strategy (if any) - None

### LLM Experiment
- Models compared (name, family, size)
- Qwen/Qwen2.5-0.5B 
- microsoft/Phi-3-mini-4k-instruct

- Results and discussions
    - Prompt used (copy it here)
    - You are a helpful Amazon shopping assistant.
    Answer the question using ONLY the following context (which contains real product reviews + metadata). 
    Include the product's average rating as part of your reasoning for selecting a certain product, the higher the rating the better the product.
    Always cite the product ASIN when possible. If the answer isn't in the context, say so.

    - Results (found in ./results/final_query_results_v2.csv)
    - For most of the Microsoft model's responses, it seems like the responses are clearer and more relevant to the user's queries. Unlike Qwen, the Microsoft model never returned an empty response due to a lack of context. It performed especially will with the "1080p gaming monitor" query, where it successfully identified not only the highest rated product, but also gave rationale specific to that product's features as to why it would be ideal for 1080p gaming. However, it seemed to struggle with the last and most complex query of "white gaming mouse for left-handed people". At first, it recommeneded a product that was completely unrelated, but caught and corrected itself mid-response to a mouse that made more sense for the given query. With a more powerful model like this one, the bottleneck comes from compute and crafting the appropriate prompt for the model to make use of. Because both our computers don't have compatable GPU's for LLM models, we struggled with long wait times for responses to be returned. Given more time, we would certianly have continued experimenting with prompts and post-processing techniques to not only better isolate the model's response, but also put the appropriate constraints on the model through the system prompt to guide it toward better responses.

- Which model you chose and why
- We chose to experiment with the microsoft/Phi-3-mini-4k-instruct model because it can be used with our existing code, meaning no extensive code refactoring is needed for further testing. This model is also known follow instructions and better reasoning given its relatively smaller size.

## Step 2: Additional Feature (state which option you chose)

### What You Implemented

- Description of the feature
- Cloud deployment of local web app through the Posit Cloud platform, accessible via this [link](https://roccolee18-amazon-electronics-recommender-app.share.connect.posit.cloud)

- Key results or examples
- We successfully published our local Shiny web app onto the Posit Cloud platform. Achieving this required creating a fork of our repo and refactoring the file structure to only include the web app related code. The biggest challenge was scanning through our web-app code to find file dependancies and ensure those were transfered/kept in the forked repo to maintain functionality.

## Step 3: Improve Documentation and Code Quality

### Documentation Update
- Summary of `README` improvements

### Code Quality Changes
- Summary of cleanups

## Step 4: Cloud Deployment Plan
- Data Storage
Due to the large size of our database, we created helper functions that conver the raw metadata and reviews into parquet files which are much smaller and easier store. Because of this optimization, we believe we can store the parquet files on AWS S3.

The raw data itself can also live on an AWS S3 bucket, as they won't be accessed frequently during processing, and S3 has scalable storage to meet the space needed for the larger, raw JSONL files.

Since we've only tested our app with 1 or 2 users at a time, loading the indexes (both semantic vectors and BM25) onto memory worked well enough. If we are expecting a higher volume of traffic once our app gets deployed, we may consider also bringing the indexes onto a cloud service like AWS OpenSearch to allow mulitple app instances to query the same index without requiring each device to load it into memory.

- Compute
Regarding the computation of our programs, due to the large number of specific requirements needed, a containerizer like Docker would help improve usability and ensure package versions don't conflict, which is an issue we briefly ran into. The container can then be hosted on cloud services like AWS ECS. 

A potential limitation of using Shiny for Python to build our app is that having multiple users may block each other during larger RAG queries. In those instances, our options are either to run mulitple app instances, which may require more compute resources and redundant loading, or offloading the LLM inference onto another cloud service like AWS SQS so the app can still be responsive while inference is handled in the background.

In terms of handling the LLM inference itself, that depends on the size of model we choose as our final one. In our Milestones, we experimented with lighter Qwen and Microsoft models, so that is what we will assume the full deployed app will also use. Hosting those models will require a GPU instance so users aren't stuck waiting a long time for a single query, however that is an expensive option to keep running all the time. Therefore, we believe using the HuggingFace API or AWS Bedrock is a better alternative, as the payment scheme is only per token rather than per hour. It also offloads the responsibility of managing GPU infastructure as well.

- Streaming/Updates
To continually process new data, a scheduled job on the cloud platform (for example, AWS Lambda) will monitor the S3 bucket for new data drops and trigger the appropriate scripts to process the new data and create new indexes for the RAG to reference. 

Keeping the pipeline up to date can be done by building a CI/CD pipeline with Github Actions to automatically redeploy the app when new code is pushed. As mentioned above, the indexes can be updated with new product information by having a AWS Lambda function monitor for new data drops in the S3 bucket and trigger a run of the pre-processing pipeline to get the updated index into the RAG pipeline.