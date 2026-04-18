## LLM Model Choice Rationale

For building RAG functionality in our project, we decided to use the Qwen/Qwen2.5-1.5B model. We chose this model because of our relatively limited local computing power and its reliable performance in basic tasks such as retrieving product recommendations. There was an even lighter version of this model (Qwen/Qwen2.5-0.5B) which we decided not to go for because the performance tradeoff would be too high. We've done some research on model performance and found that models of the 0.5B category would struggle to gather information from multiple documents, which is what we plan to do with our RAG model. Further, The chosen model being a decoder-only model makes it well suited for the task of a RAG. Some alternative decoder-only models we could have chosen include: microsoft/phi-2, microsoft/phi-3/mini-4k-instruct or google/gemma-2-2b-it

## Manual / Qualitative Evaluation for Hybrid RAG Workflow

| # | Query | Response |
|---|-------|---------------|
| 1 | wireless bluetooth headphones | "Based on the average ratings provided, wireless Bluetooth headphones with a rating of 3.8 is a suitable option for your needs. The higher average rating suggests that these headphones have received positive feedback from users, indicating that they meet the expectations set by consumers. However, it's always important to consider other factors such as comfort, battery life, and compatibility before making a final decision." |
| 2 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 3 | 13 inch chromebook | "To answer the question for a 13-inch Chromebook, I'll examine the average ratings of the products in the dataset provided. Here are the relevant details: This product has an average rating of 3.7, which is the highest among the options. It's a Meisohua Canvas Backpack with a wide range of features such as a USB charging port, making it suitable for college students and those who need extra space and convenience for their laptops. |
| 4 | noise cancelling headphones | "The Saramonic SR-BH600 Over-Ear Headphones, Active Noise Cancelling Bluetooth Headphones with Microphone have an average rating of 3.2 out of 5 stars. They are noise cancelling headphones, as indicated in the product description. Therefore, I would recommend these headphones to someone who is looking for noise cancelling headphones." |
| 5 | high performance work laptop | "Based on the provided context, I would recommend the product with the ASIN B00BN0LHF8, titled ""Samsung NP540U3C-A03UB Series 5 13.3"" Touch-Screen Laptop. This product has an average rating of 3.5, indicating that it has a reasonable level of performance for its intended purpose, which is a high performance work laptop." |
| 6 | super fast wireless charger | "I'm sorry, but I'm unable to provide a meaningful answer based on the provided context. The context only contains information about product ratings but does not mention any super fast wireless charger. Please provide additional context or clarify your question." |
| 7 | battery pack for charging laptops | "The product ""Battery Pack for Charging Laptops"" has an average rating of 3.9, which indicates that it is a good quality product. The product uses the USB charging port and has a TSA. The review says this product is very good and worth it." |
| 8 | extension cord for usb-a to usb-c | "The most suitable product for an extension cord to connect USB-A to USB-C is the one with the ASIN B08XB3B6FY. This product has an average rating of 4.5 stars, indicating a higher rating than the other options, suggesting it is more satisfactory in terms of its performance and customer satisfaction." |
| 9 | active noise cancelling bluetooth sony wm-1000xm4 | The product ""Wireless Bluetooth Headphones Waterproof IPX7, Best Sport in Ear Earbuds Earphones w/Remote and Mic"" (ASIN: B07H92ZDZL) is recommended based on the average rating of 4.3 out of 5." |
| 10 | white gaming mouse for left handed people | "White gaming mouse for left handed people: Logitech 910002698 M525 Wireless Mouse, Compact, Right/Left, Blue" |

Query 1:

| Dimension | What to assess | Yes/No |
|---|-------|-----|
| Accuracy | Is the answer factually correct based on the reviews? |  |
| Completeness | Does the answer address all aspects of the question? |  |
| Fluency | Is the answer natural, clear, and easy to read? |  |

- 
- 
- 

Query 2:

| Dimension | What to assess | Yes/No |
|---|-------|-----|
| Accuracy | Is the answer factually correct based on the reviews? |  |
| Completeness | Does the answer address all aspects of the question? |  |
| Fluency | Is the answer natural, clear, and easy to read? |  |

- 
- 
- 

Query 3:

| Dimension | What to assess | Yes/No |
|---|-------|-----|
| Accuracy | Is the answer factually correct based on the reviews? |  |
| Completeness | Does the answer address all aspects of the question? |  |
| Fluency | Is the answer natural, clear, and easy to read? |  |

- 
- 
- 

Query 4:

| Dimension | What to assess | Yes/No |
|---|-------|-----|
| Accuracy | Is the answer factually correct based on the reviews? |  |
| Completeness | Does the answer address all aspects of the question? |  |
| Fluency | Is the answer natural, clear, and easy to read? |  |

- 
- 
- 

Query 5:

| Dimension | What to assess | Yes/No |
|---|-------|-----|
| Accuracy | Is the answer factually correct based on the reviews? |  |
| Completeness | Does the answer address all aspects of the question? |  |
| Fluency | Is the answer natural, clear, and easy to read? |  |

- 
- 
- 