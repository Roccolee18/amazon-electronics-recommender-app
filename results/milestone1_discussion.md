## Top 5 Results Comparison
Here is a visual representation of the top 5 results of each search algorithm per query:

| # | Query | Semantic Search Results | BM25 Search Results |
|---|-------|------------------------|---------------------|
| 1 | 1080p gaming monitor | Sceptre IPS 27" 4K UHD LED Monitor | ASUS TUF Gaming 23.8" 1080P Monitor |
| 2 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor | Sceptre IPS 27" 4K UHD LED Monitor |
| 3 | 1080p gaming monitor | Acer XG270HU omidpx 27-inch WQHD | Acer XG270HU omidpx 27-inch WQHD |
| 4 | 1080p gaming monitor | Sapphire Radeon Nitro+ Rx 480 4GB | Razer Kiyo Full HD 1080p Camera |
| 5 | 1080p gaming monitor | Anbear DisplayPort to HDMI Adapter | BenQ ScreenBar Monitor Light |
| 6 | noise cancelling headphones | Avantree ANC032 Active Noise Cancelling | Avantree ANC032 Active Noise Cancelling |
| 7 | noise cancelling headphones | House of Marley TTR Noise-Cancelling | Parrot Zik 2.0 Wireless Noise Cancelling |
| 8 | noise cancelling headphones | Audeze LCD-X Over Ear Open Back Headphone | Wireless Earbud Sport Bluetooth 5.3 |
| 9 | noise cancelling headphones | RevoNext In Ear Monitor Earbuds HiFi | House of Marley TTR Noise-Cancelling |
| 10 | noise cancelling headphones | Jabra STONE Bluetooth Headset | Wireless Earbuds Bluetooth Headphones IPX7 |
| 11 | super fast wireless charger | iPhone Charger Nylon Braided 5 Pack | ilikable MFi Certified iPhone Cable |
| 12 | super fast wireless charger | Netgear AC1600 Smart WiFi Router | Power Strip Surge Protector |
| 13 | super fast wireless charger | TPLTECH Extra Long 5Ft 2A AC Adapter | Jabra STONE Bluetooth Headset |
| 14 | super fast wireless charger | AINOPE USB C to USB C Cable 10ft | Soarking Charging Base for Sonos Move |
| 15 | super fast wireless charger | USB Type C Cable Anker 2-Pack 6Ft | PANASONIC Lumix FZ80 4K Camera |
| 16 | active noise cancelling bluetooth sony wm-1000 | Avantree ANC032 Active Noise Cancelling | Avantree ANC032 Active Noise Cancelling |
| 17 | active noise cancelling bluetooth sony wm-1000 | DOBOPO Wireless Earbuds Bluetooth 5.3 | Wireless Earbud Sport Bluetooth 5.3 |
| 18 | active noise cancelling bluetooth sony wm-1000 | Jabra STONE Bluetooth Headset | Wireless Earbuds Bluetooth Headphones IPX7 |
| 19 | active noise cancelling bluetooth sony wm-1000 | Wireless Earbuds Bluetooth Headphones IPX7 | Parrot Zik 2.0 Wireless Noise Cancelling |
| 20 | active noise cancelling bluetooth sony wm-1000 | SoundBot SB221 HD Wireless Bluetooth 4.0 | House of Marley TTR Noise-Cancelling |
| 21 | white gaming mouse for left handed people | Razer Naga MMO PC Gaming Mouse | ELECOM EX-G Trackball Mouse |
| 22 | white gaming mouse for left handed people | Logitech Anywhere Mobile Mouse MX | Logitech Anywhere Mobile Mouse MX |
| 23 | white gaming mouse for left handed people | ELECOM EX-G Trackball Mouse | Razer Naga MMO PC Gaming Mouse |
| 24 | white gaming mouse for left handed people | Rechargeable Vertical Mice Ergonomic Wireless | Zotech Bondidea N86 Wireless Mouse |
| 25 | white gaming mouse for left handed people | Logitech mk620 Wireless Keyboard & Mouse | Rechargeable Vertical Mice Ergonomic Wireless |

Query 1: "1080p gaming monitor"
For this query, BM25 seems to have done better than semantic search. While not all products in the results were perfect, it did have results that were more closely related to the query than the products returned by semantic search. An example of this is semantic search returning a GPU and a HDMI adapter while the worse results of BM25 were a camera that contained the resoultion mentioned in the query, and a monitor light, which also contained vocabulary used in the query.

Query 2: "noise cancelling headphones"
Here, BM25 still does better than semantic search. With this query, both methods returned good results, but semantic search included a set of headphones that were open-ear, which is not noise cancelling at all. 

Query 3: "super fast wireless charger"
Both search methods struggled with this query, however semantic search returned results that are more useful to the user's query. BM25 returned some non-sensical results like a set of headsets and a 4K camera. We suspect the reason for this is that this query is more abstract, which requires more context inference in order to return better results. It is probably also rare for the exact words of the query to be used in any reviews for products, so BM25 may not be able to find those exact words and therefore miss some useful products.

Query 4: "active noise cancelling bluetooth sony wm-1000xm4"
The goal of this query was to test how the methods perform with queries with more specific keywords, and suprisingly both methods returned decent results. Perhaps becuase of the first half of the query, semantic search was able to find better results. Overall, almost all the results do seem to be useful for the user.

Query 5: "white gaming mouse for left handed people"
Finally, both methods seem to have handled the complexity of this query fairly well. The top 5 results of both methods have almost the exact same results, just in different order. Based on the ordering, we believe semantic search edges out BM25 in returning products that are more useful to the user. All but one of the returned products have an ambidexterous version. For the one mouse missing a left-handed version (ELECOM EX-G Trackball Mouse), we suspect that there could be users asking for a left-handed version of this mouse in the reviews, explaining why it is included in the results.

## Overall Insights
In general, both algorithms performed decently well with the test queries. All results returned products that were somewhat close to the test query. The hardest one for both algorithms seemed to have been "super fast wireless charger", where results varied from headsets to wifi routers between both search algorithms. For more complex queries, like "white gaming mouse for left handed people", the algoritms seemed to have picked up even the ambidextrous requrirement of the query, as most of the mice returned had an ambidextrous version. While the result itself may not have been ambidextrous, it is possible that there were reviews mentioning an ambidextrous version of the product, hence why it was included as a result depsite not being directly ambidextrous.

The strength of the BM25 method seems to be finidng matches that exactly match the query, and for semantic search, it is being able to handle more abstract queries like Query 5. BM25 would struggle with being user friendly, as it requires the user not only not make any typos in their query, but also guess what exact verbage would be used to describe the item they are looking for. Semantic search is more computationally expensive and can suffer from context drift if the user's query is too vague (e.g. returning a GPU when the query was asking for a gaming monitor)

RAG would be better at handling queries that are more posed as a question, as it can pull context from multiple retrieved documents and generate a coherent recommendation with reasoning, rather than just returning ranked product titles. Reranking would outperform both in cases where the initial retrieval pool has the right products but in the wrong order. Both BM25 and semantic search use relatively shallow scoring — (BM25 relies on term frequency and semantic search on a single embedding similarity), whereas a reranker looks at the query and each document together.