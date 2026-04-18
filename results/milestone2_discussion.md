## LLM Model Choice Rationale

For building RAG functionality in our project, we decided to use the Qwen/Qwen2.5-1.5B model. We chose this model because of our relatively limited local computing power and its reliable performance in basic tasks such as retrieving product recommendations. There was an even lighter version of this model (Qwen/Qwen2.5-0.5B) which we decided not to go for because the performance tradeoff would be too high. We've done some research on model performance and found that models of the 0.5B category would struggle to gather information from multiple documents, which is what we plan to do with our RAG model. Further, The chosen model being a decoder-only model makes it well suited for the task of a RAG. Some alternative decoder-only models we could have chosen include: microsoft/phi-2, microsoft/phi-3/mini-4k-instruct or google/gemma-2-2b-it

## Manual / Qualitative Evaluation for Hybrid RAG Workflow

| # | Query | Product Title |
|---|-------|---------------|
| 0 | wireless bluetooth headphones | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear with Immersive So |
| 1 | wireless bluetooth headphones | Parrot Zik 2.0 Wireless Noise Cancelling Headphones (Black) |
| 2 | wireless bluetooth headphones | Long Range Bluetooth Adapter 2.0 for car V2.0 EDR Support Windows8.1 (Sky Blue) |
| 3 | wireless bluetooth headphones | Beats BT ON WIRELS BLK Wireless On-Ear Headphone (Black-Discontinued by Manufacturer) |
| 4 | wireless bluetooth headphones | DOBOPO Wireless Earbuds Bluetooth 5.3 Headphones 50Hrs Playtime Sports Earphones Over-Ear Earhooks |
| 5 | wireless bluetooth headphones | DOBOPO Wireless Earbuds Bluetooth 5.3 Headphones 50Hrs Playtime Sports Earphones Over-Ear Earhooks |
| 6 | wireless bluetooth headphones | JVC HAF250BTB in-Ear Headphone, Bluetooth, Gumy - Black |
| 7 | wireless bluetooth headphones | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 8 | wireless bluetooth headphones | Wireless Earbuds, Bluetooth Headphones IPX7 Waterproof Wireless Bluetooth Earphone with Microphone |
| 9 | wireless bluetooth headphones | Beats BT ON WIRELS BLK Wireless On-Ear Headphone (Black-Discontinued by Manufacturer) |
| 10 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 11 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 12 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 13 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 14 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 15 | 1080p gaming monitor | ASUS TUF Gaming 23.8" 1080P Monitor (VG249Q1R) - Full HD, IPS, 165Hz, 1ms |
| 16 | 1080p gaming monitor | Sceptre IPS 27" 4K UHD LED Monitor up to 75Hz DisplayPort HDMI DVI Build-in Speakers, Frameless |
| 17 | 1080p gaming monitor | Acer XG270HU omidpx 27-inch WQHD AMD FREESYNC (2560 x 1440) Widescreen Monitor |
| 18 | 1080p gaming monitor | BenQ ScreenBar Monitor Light, LED Computer, Auto-Dimming, Hue Adjustment Features |
| 19 | 1080p gaming monitor | HP Elite Desktop PC Computer Intel Core i5 3.1-GHz, 8GB Ram, 1TB Hard Drive, 19 Inch LCD Monitor |
| 20 | 13 inch chromebook | ASUS C300 ChromeBook 13.3 Inch (Intel Celeron, 2 GB, 16GB SSD, Red) |
| 21 | 13 inch chromebook | ASUS C300 ChromeBook 13.3 Inch (Intel Celeron, 2 GB, 16GB SSD, Red) |
| 22 | 13 inch chromebook | ASUS C300 ChromeBook 13.3 Inch (Intel Celeron, 2 GB, 16GB SSD, Red) |
| 23 | 13 inch chromebook | ASUS C300 ChromeBook 13.3 Inch (Intel Celeron, 2 GB, 16GB SSD, Red) |
| 24 | 13 inch chromebook | Belkin 11 Inch Laptop Case - Laptop Sleeve - Computer Accessories For Chromebook |
| 25 | 13 inch chromebook | Belkin 11 Inch Laptop Case - Laptop Sleeve - Computer Accessories For Chromebook |
| 26 | 13 inch chromebook | 90W/65W USB C Charger Power Adapter for HP Spectre x360 13-AE015DX |
| 27 | 13 inch chromebook | MOSISO Compatible with MacBook Air 13 inch Case (Models: A1466 & A1369, 2010-2017) |
| 28 | 13 inch chromebook | JSAUX Magnetic USB C Adapter 20Pins Type C Connector, Support PD 100W Fast Charging |
| 29 | 13 inch chromebook | GABraden Compatible with MacBook Air 13 inch Case, 2020 2019 2018 Release (A2337 M1 A2179 A1932) |
| 30 | noise cancelling headphones | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 31 | noise cancelling headphones | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 32 | noise cancelling headphones | Parrot Zik 2.0 Wireless Noise Cancelling Headphones (Black) |
| 33 | noise cancelling headphones | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 34 | noise cancelling headphones | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 35 | noise cancelling headphones | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 36 | noise cancelling headphones | Parrot Zik 2.0 Wireless Noise Cancelling Headphones (Black) |
| 37 | noise cancelling headphones | House of Marley EM-DH003-PS TTR Noise-Cancelling Over-Ear Headphones (Black) |
| 38 | noise cancelling headphones | Wireless Earbuds, Bluetooth Headphones IPX7 Waterproof Wireless Bluetooth Earphone with Microphone |
| 39 | noise cancelling headphones | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 40 | high performance work laptop | Lenovo 15.6" HD Premium Laptop, Intel Pentium Silver N5000 Quad-Core |
| 41 | high performance work laptop | ASUS ROG Strix Scar 15 (2022) Gaming Laptop, 15.6" 300Hz IPS FHD, NVIDIA GeForce RTX 3070 Ti |
| 42 | high performance work laptop | Acer Aspire 5 A515-46-R3CZ Slim Laptop, 15.6" Full HD IPS, AMD Ryzen 7 3700U |
| 43 | high performance work laptop | ASUS ROG Strix Scar 15 (2022) Gaming Laptop, 15.6" 300Hz IPS FHD, NVIDIA GeForce RTX 3070 Ti |
| 44 | high performance work laptop | Acer Aspire 5 A515-46-R3CZ Slim Laptop, 15.6" Full HD IPS, AMD Ryzen 7 3700U |
| 45 | high performance work laptop | Acer Aspire 5 A515-46-R3CZ Slim Laptop, 15.6" Full HD IPS, AMD Ryzen 7 3700U |
| 46 | high performance work laptop | AINOPE USB 3.0 Cable, USB to USB Cable, USB A Male to Male Cable |
| 47 | high performance work laptop | Kingston Technology HyperX Impact 32GB 2933MHz DDR4 CL17 SODIMM Memory |
| 48 | high performance work laptop | NETGEAR N900 Dual Band Wi-Fi USB Adapter (WNDA4100) |
| 49 | high performance work laptop | ICE COOREL Laptop Cooling Pad with 6 Cooling Fans for 14-17 Inch Gaming Laptops |
| 50 | super fast wireless charger | USB Type C Cable, Anker 2-Pack 6Ft Premium Nylon USB-C to USB-A Fast Charging Cable |
| 51 | super fast wireless charger | USB Type C Cable, Anker 2-Pack 6Ft Premium Nylon USB-C to USB-A Fast Charging Cable |
| 52 | super fast wireless charger | Rankie Micro USB Cable High Speed Data and Charging, Nylon Braided Charger Cord, 3-Pack, 3 Feet |
| 53 | super fast wireless charger | iPhone Charger Nylon Braided 5 Pack MFi Certified Lightning Cable High Speed USB Fast Charging |
| 54 | super fast wireless charger | Rankie Micro USB Cable High Speed Data and Charging, Nylon Braided Charger Cord, 3-Pack, 3 Feet |
| 55 | super fast wireless charger | Power Strip, Surge Protector with 4 AC Outlets and 4 USB Charging Ports, 6 Feet Long Extension Cord |
| 56 | super fast wireless charger | USB Type C Cable, Anker 2-Pack 6Ft Premium Nylon USB-C to USB-A Fast Charging Cable |
| 57 | super fast wireless charger | iXCC Element 6 Feet Micro USB to USB 2.0 Charge and Sync Cable |
| 58 | super fast wireless charger | Bose SoundLink Color II: Portable Bluetooth, Wireless Speaker with Microphone - Coral Red |
| 59 | super fast wireless charger | AINOPE USB C to USB C Cable, 2-Pack 10ft, 60W 3.1A Type C Charger Cord |
| 60 | battery pack for charging laptops | Universal Laptop Charger with LCD - Premium Quality, 45W Ultra Slim AC Adapter Power Supply |
| 61 | battery pack for charging laptops | RUCYEN Lunch Backpack, Insulated Cooler Backpack Lunch Box for Women, 15.6 Inch Laptop |
| 62 | battery pack for charging laptops | Universal Laptop Charger with LCD - Premium Quality, 45W Ultra Slim AC Adapter Power Supply |
| 63 | battery pack for charging laptops | Universal Laptop Charger with LCD - Premium Quality, 45W Ultra Slim AC Adapter Power Supply |
| 64 | battery pack for charging laptops | Universal Laptop Charger with LCD - Premium Quality, 45W Ultra Slim AC Adapter Power Supply |
| 65 | battery pack for charging laptops | ENEGON NP-BX1 Battery 2-Pack and Rapid Dual Charger for Sony NP-BX1 and Sony ZV-1 |
| 66 | battery pack for charging laptops | EBL Quick AA AAA Battery Charger with 1A USB Input Port for Ni-MH Ni-CD Rechargeable Batteries |
| 67 | battery pack for charging laptops | Wireless Earbuds, Bluetooth Headphones IPX7 Waterproof Wireless Bluetooth Earphone with Microphone |
| 68 | battery pack for charging laptops | TalentCell Mini UPS Uninterrupted Power Supply 27000mAh 98Wh Lithium ion Backup Battery |
| 69 | battery pack for charging laptops | Belkin 11 Inch Laptop Case - Laptop Sleeve - Computer Accessories For Chromebook |
| 70 | extension cord for usb-a to usb-c | AINOPE USB C to USB C Cable, 2-Pack 10ft, 60W 3.1A Type C Charger Cord |
| 71 | extension cord for usb-a to usb-c | Power Strip, Surge Protector with 4 AC Outlets and 4 USB Charging Ports, 6 Feet Long Extension Cord |
| 72 | extension cord for usb-a to usb-c | USB C to USB C Cable 60W, 3.3Ft 2 Pack UPoweradd Fast Charging Cable, Durable Braided Nylon Type C |
| 73 | extension cord for usb-a to usb-c | USB Type C Cable, Anker 2-Pack 6Ft Premium Nylon USB-C to USB-A Fast Charging Cable |
| 74 | extension cord for usb-a to usb-c | Belkin USB |
| 75 | extension cord for usb-a to usb-c | Baseus 8-in-1 USB C Hub Docking Station, USB C Adapter with 4K HDMI, 3 USB 3.0, TF/SD Reader |
| 76 | extension cord for usb-a to usb-c | WildHD DC Power Extension Cable 33ft 2.1mm x 5.5mm Compatible with 12V DC Adapter for CCTV |
| 77 | extension cord for usb-a to usb-c | TNP Ethernet Cable Extender Extension Cable Adapter (1.5FT) - Cat7 Cat6 Cat5e Cat5 RJ45 |
| 78 | extension cord for usb-a to usb-c | iMBAPrice 3 Ft Power Cable for Samsung LED/LCD TV UN40EH5300 and Other Models |
| 79 | extension cord for usb-a to usb-c | AINOPE USB C to USB C Cable, 2-Pack 10ft, 60W 3.1A Type C Charger Cord |
| 80 | active noise cancelling bluetooth sony wm-1000xm4 | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 81 | active noise cancelling bluetooth sony wm-1000xm4 | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 82 | active noise cancelling bluetooth sony wm-1000xm4 | Parrot Zik 2.0 Wireless Noise Cancelling Headphones (Black) |
| 83 | active noise cancelling bluetooth sony wm-1000xm4 | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 84 | active noise cancelling bluetooth sony wm-1000xm4 | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 85 | active noise cancelling bluetooth sony wm-1000xm4 | Avantree ANC032 Active Noise Cancelling Headphones Over Ear with Microphone for Home Office |
| 86 | active noise cancelling bluetooth sony wm-1000xm4 | Wireless Earbuds, Bluetooth Headphones IPX7 Waterproof Wireless Bluetooth Earphone with Microphone |
| 87 | active noise cancelling bluetooth sony wm-1000xm4 | Parrot Zik 2.0 Wireless Noise Cancelling Headphones (Black) |
| 88 | active noise cancelling bluetooth sony wm-1000xm4 | House of Marley EM-DH003-PS TTR Noise-Cancelling Over-Ear Headphones (Black) |
| 89 | active noise cancelling bluetooth sony wm-1000xm4 | Wireless Earbud, Sport Bluetooth 5.3 Earbud with Earhook Wireless Earphones in-Ear |
| 90 | white gaming mouse for left handed people | Logitech Anywhere Mobile Mouse MX, Wireless Mouse for PC and Mac |
| 91 | white gaming mouse for left handed people | Razer Naga MMO PC Gaming Mouse |
| 92 | white gaming mouse for left handed people | Logitech Anywhere Mobile Mouse MX, Wireless Mouse for PC and Mac |
| 93 | white gaming mouse for left handed people | Logitech Anywhere Mobile Mouse MX, Wireless Mouse for PC and Mac |
| 94 | white gaming mouse for left handed people | Razer Naga MMO PC Gaming Mouse |
| 95 | white gaming mouse for left handed people | Logitech Anywhere Mobile Mouse MX, Wireless Mouse for PC and Mac |
| 96 | white gaming mouse for left handed people | Razer Naga MMO PC Gaming Mouse |
| 97 | white gaming mouse for left handed people | ELECOM EX-G Trackball Mouse, Wired, Thumb Control, Sculpted Ergonomic Design |
| 98 | white gaming mouse for left handed people | Zotech Bondidea N86 Wireless Mouse for PC and MAC, 6 Buttons, 3 Adjustable DPI Levels |
| 99 | white gaming mouse for left handed people | Rechargeable Vertical Mice Ergonomic Wireless Mouse, Vertical Mouse Ergonomic Design with 2.4G USB |

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