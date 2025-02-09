
agents_data = {
        "Consumer": {
            "personas" : [
                {
                    "user_id": "Anil",
                    "access": ["HDFCBank","ICICIBank"],
                    "about": """Anil is a premium user with a high credit score of 750. His primary interests lie in Electronics and Toys, and he prefers flexible EMI options along with Cashback offers. With 10,000 points redeemable, he enjoys top-tier benefits and access to exclusive deals""",
                },
                {
                    "user_id": "Prahastha",
                    "access": ["HDFCBank","ICICIBank"],
                    "about": """Prahastha, with a credit score of 630, is a medium-risk user who focuses on Home Appliances. His preferred payment plans are EMI and Cash, and he has 3,200 redeemable points. He enjoys standard offers, with a solid foundation for financing options.""",
                },
                {
                    "user_id": "Ayushman",
                    "access": ["ICICIBank"],
                    "about": """Ayushman is a medium-risk user with a credit score of 690. He is interested in Fitness Equipment and prefers payment plans like EMI and Points Redemption. With 4,800 points available for redemption, Ayushman enjoys balanced benefits for his purchases.""",
                },
            ],
            "system_message" : """You are a dedicated personal banking assistant for {user_id}. You are responsible for managing all aspects of your user/operator's banking needs related to purchase requests. This includes handling all communication with bank agents, managing tasks, and scheduling reminders.

    1. Task Management & Communication:
    - Process incoming messages and scheduled reminders without user/operator intervention when possible
    - Create and manage tasks autonomously based on known patterns
    - Schedule reminders and follow-ups automatically using the schedule tool
    - Contact bank agents directly for information you need without user/operator involvement

    2. Communication Rules:
    - Handle all routine tasks independently
    - Only involve your user/operator when:
        * You encounter an unknown situation requiring judgment
        * You need approval for important decisions
        * You've completed a significant task
    - All messages must be through the tool call reponse
    - When you are communicating with bank agents, they know that you are an AI assistant

    3. Agent Interactions:
    - Contact bank agents to send purchase requests and receive payment plans and discount details
    - Rank offers based on the best terms and remove duplicate offers from different banks
    - Only notify user/operator of final results or if you need guidance

    4. Final Response format:
    - Use bullet points or numbered lists for better readablility and clarity.\
    - Highlight key points in **bold** or *italics*.\
    - Make the response more readable by making it concise and information dense based on the the user's query requirements.\
    - Use **bold** formatting for mentions of products, brands, or features.\
    - Prioritize the most relevant information from the user's perspective.\
    - Aim for structured, concise responses with clear formatting and only necessary information mentioned.

    User/Operator ID: {user_id}
"""
        },
        "Issuer" : {
            "personas" : [
                {
                    "user_id" : "HDFCBank",
                    "access" : ["Anil", "Amazon", "Croma"],
                    "about" : """HDFC Bank communicates with merchants to find products and create payment plans for consumers""",
                    "user_details" : """
    | User Id | Credit Score | Risk Profile | Category Preferences    | Payment Plan Preferences| Points Redeemable| User Profile |
    |---------|--------------|--------------|-------------------------|-------------------------|------------------|--------------|
    | Anil    | 750          | Good         | Electronics, Toys       | EMI, Cashback           | 10,000           | Premium      |
    |Prahastha| 630          | Medium       | Home Appliances         | EMI, Cash               | 3,200            | Standard     |
    | Ayushman| 690          | Medium       | Fitness Equipment       | EMI, Points Redemption  | 4,800            | Standard     |
                """,
                    "payment_plans" : """
    | Offer Type                     | Payment Plan Type        | EMI Available| EMI Tenure Available | Min Credit Score | Applicable User Profiles | Interest Rate | Points Redeemable Discount | Base Price Min| Base Price Max| Special Conditions                  |
    |--------------------------------|--------------------------|--------------|----------------------|------------------|--------------------------|---------------|----------------------------|---------------|---------------|-------------------------------------|
    | **Premium No-Cost EMI**        | EMI                      | Yes          | 12, 18, 24 months    | 720              | Premium                  | 10.0%         | 12% off if >9000 points    | 1000          | 2000          | iPhones, Laptops, High-End Smart TVs |
    | **Loyalty Cashback EMI**       | EMI + Cashback           | Yes          | 6, 12 months         | 690              | Standard, Premium        | 11.5%         | 8% cashback if >6000 points | 500           | 1500          | Available for Smartwatches, Headphones |
    | **Buy-Now-Pay-Later (BNPL)**   | BNPL                     | No           | N/A                  | 670              | Standard, Basic          | N/A           | 5% discount if >3000 points | 200           | 800           | Smartwatches, Fitness Bands, Wearables |
    | **Limited Stock EMI**          | EMI                      | Yes          | 3, 6 months          | 710              | Premium, Standard        | 12.8%         | 6% off if >4000 points     | 1000          | 1800          | For PS5, Razer Laptops, Low-Stock Collectibles |
    | **Upgrade & Trade-In Plan**    | Trade-In + EMI Option    | Yes          | 6, 12, 18 months     | 700              | Standard, Premium        | 10.5%         | 9% off if >7000 points     | 1000          | 2000          | Upgrade iPhones, Samsung Galaxy, Gaming Laptops |
    | **Exclusive Star Wars EMI**    | EMI                      | Yes          | 6, 12 months         | 680              | Standard, Premium        | 11.2%         | 7% off if >5000 points     | 150           | 500           | Star Wars collectibles, LEGO, Hasbro |
    | **Zero Down Payment EMI**      | EMI + No Down Payment    | Yes          | 12, 18, 24 months    | 750              | Premium                  | 9.5%          | 15% off if >10,000 points  | 1200          | 2500          | Available for MacBooks, iPads, Microsoft Surface |
    | **Cashback on Cash Purchases** | Cash                     | No           | N/A                  | 660              | Standard, Basic          | N/A           | 4% cashback if >3000 points | 200           | 700           | Available for Small Appliances, Echo Dot |
                    """
                },
                {
                    "user_id" : "ICICIBank",
                    "access" : ["Anil", "Amazon", "Croma"],
                    "about" : """ICICI Bank communicates with merchants to find products and create payment plans for consumers""",
                    "user_details" : """
    | User Id | Credit Score | Risk Profile | Category Preferences    | Payment Plan Preferences| Points Redeemable| User Profile |
    |---------|--------------|--------------|-------------------------|-------------------------|------------------|--------------|
    | Anil    | 750          | Good         | Electronics, Toys       | EMI, Cashback           | 10,000           | Premium      |
    |Prahastha| 630          | Medium       | Home Appliances         | EMI, Cash               | 3,200            | Standard     |
    | Ayushman| 690          | Medium       | Fitness Equipment       | EMI, Points Redemption  | 4,800            | Standard     |
                    """,
                    "payment_plans" : """
    | Offer Type                     | Payment Plan Type        | EMI Available| EMI Tenure Available | Min Credit Score | Applicable User Profiles | Interest Rate | Points Redeemable Discount | Base Price Min| Base Price Max| Special Conditions |
    |--------------------------------|--------------------------|--------------|----------------------|------------------|--------------------------|---------------|----------------------------|---------------|---------------|--------------------|
    | **iPhone Partnered EMI Plan**  | EMI + Apple Partnered    | Yes          | 12, 18, 24 months    | 730              | Premium                  | 9.8%          | 15% off if >10,000 points  | 1000          | 2000          | Only on Apple products |
    | **Flexible EMI Option**        | EMI                      | Yes          | 3, 6, 9, 12 months   | 680              | Standard, Premium        | 11.5%         | 8% off if >6000 points     | 500           | 1800          | Available for Gaming Consoles, Laptops |
    | **Trade-In & Upgrade Plan**    | Trade-In + EMI           | Yes          | 6, 12, 18 months     | 700              | Standard, Premium        | 10.5%         | 9% off if >7000 points     | 900           | 2000          | Upgrade Samsung Galaxy, iPhones, MacBooks |
    | **Cashback Festive Offer**     | EMI + Cashback           | Yes          | 3, 6, 9 months       | 690              | Standard, Premium        | 12.5%         | 10% cashback if >5000 points | 300         | 1200          | Limited to Festive Season |
    | **Buy-Now-Pay-Later (BNPL)**   | BNPL                     | No           | N/A                  | 660              | Standard, Basic          | N/A           | 6% discount if >4000 points | 200          | 800           | BNPL option for small gadgets, home devices |
    | **Zero Processing Fee EMI**    | EMI                      | Yes          | 6, 12, 18 months     | 720              | Premium, Standard        | 10.2%         | 7% off if >6000 points     | 1000          | 2200          | Available for TVs, Cameras, Laptops |
    | **Limited Inventory Discount** | Cash                     | No           | N/A                  | 640              | Standard, Basic          | N/A           | 5% off if >3000 points     | 150           | 500           | Applies to last-stock items |
                    """
                },
            ],
            "system_message" : """You are a banking/issuer assistant for {user_id}. You are responsible for managing purchase requests, interacting with merchants, managing finanicial transactions and providing tailored payment options to users.  

    1. Core Responsibilities:  
    - Process purchase intents from Consumer agents and verify required details.  
    - Communicate with Merchant agent to inquire about product availability, pricing, and alternatives. Retrieve all relevant product details and assess available payment plans.  
    - Apply the best possible payment options, including EMI, BNPL, cashback, and trade-in deals based on your bank available payment plans.  

    2. Task Management & Agent Communication Interactions:
    - Process incoming messages and scheduled reminders without user/operator intervention when possible
    - Create and manage tasks autonomously based on known patterns
    - Schedule reminders and follow-ups automatically using the schedule tool
    - Consumer Agent: Receive purchase requests and user requirements.  
    - Merchant Agent: Request product availability and alternatives.  
    - Banking System: Analyze all the applicable/available payment plans, ensuring they align with the user’s profile.  
    - Consumer Agent: Return finalized product + payment plan details.  
    - User/Operator: Only involve your user/operator when:
        * You encounter an unknown situation requiring judgment
        * You need approval for important decisions
        * You've completed a significant task
    - All messages must be through the tool call reponse
    - When you are communicating with Merchant and Consumer agents, they know that you are an AI assistant

    3. Offer & Plan Selection Rules:
    - Select the best payment plans by matching product details, user information, risk profile, and category preferences etc.  
    - Ensure stock availability before finalizing an offer.  
    - Apply relevant discounts, loyalty-based offers, and limited-time deals** when applicable.  
    - Rank offers based on:  
        - Lowest Interest Rate
        - Best Cashback/Discounts**  
        - Highest Point Redemption Value**  

    Refer to the **tables below** for detailed conditions and select the **best-suited plan** for the user.  

    **{user_id}'s Available Payment Plans**
    {payment_plans}
            
    **{user_id}'s Customers Information**
    {user_details}

    User/Operator ID: {user_id}
"""
        },
        "Merchant" : {
            "personas" : [
                {
                    "user_id" : "Amazon",
                    "access" : ["HDFCBank", "ICICIBank"],
                    "about" : "Amazon is an e-commerce platform that sells a variety of products and adds discounts.",
                    "products_inventory" : """
    | Product_ID | Product_Name                                     | Category                  | Base_Price | Offer_Percentage | Offer_Type | Warranty_Extension_Months | Additional_Offers                               | Availability | Stock_Count | Merchant | Rating | Brand         |Offer_Expiry|
    |------------|--------------------------------------------------|---------------------------|------------|------------------|------------|---------------------------|------------------------------------------------|--------------|-------------|----------|--------|----------------|------------| 
    | A1001      | Star Wars Lego Death Star Set                    | Toys & Games              | 250        | 10               | Loyalty    | N/A                       | Loyalty points applicable                      | In Stock     | 15          | Amazon   | 4.8    | LEGO           | Ongoing    |
    | A1002      | Star Wars Lego Millennium Falcon                 | Toys & Games              | 300        | 18               | Time       | N/A                       | Limited time offer                             | In Stock     | 5           | Amazon   | 4.7    | LEGO Star Wars | 30 minutes    |
    | A2001      | iPhone 14 Pro                                    | Electronics/Smartphones   | 1200       | 5                | Warranty   | 24                        | Extended warranty available                    | In Stock     | 8           | Amazon   | 4.9    | Apple          | Ongoing    |
    | A2002      | iPhone 14                                        | Electronics/Smartphones   | 1000       | 0                | Inventory  | N/A                       | Last items left                                | In Stock     | 2           | Amazon   | 4.6    | Apple          | Until stock lasts |
    | A9023      | Star Wars Lightsaber Replica                     | Toys & Games              | 150        | 20               | Time       | N/A                       | Limited edition offer                          | In Stock     | 12          | Amazon   | 4.9    | Hasbro       | 1 hour |
    | A9024      | Star Wars Stormtrooper Helmet                    | Toys & Games              | 200        | 10               | Loyalty    | N/A                       | Exclusive collector's item                     | Out of Stock  | 0           | Amazon   | 4.8    | Sideshow     | Ongoing |
    | A9025      | Star Wars R2-D2 Action Figure                    | Toys & Games              | 80         | 20               | Time       | N/A                       | Festive discount on limited edition            | In Stock     | 20          | Amazon   | 4.7    | Mattel       | 2 days |
    | A9026      | iPhone 14 Pro Max                                | Electronics/Smartphones   | 1400       | 15               | Time       | N/A                       | Limited time exclusive deal                    | In Stock     | 10          | Amazon   | 4.9    | Apple        | 5 minutes    |
    | A9027      | iPhone 14 Plus                                   | Electronics/Smartphones   | 1100       | 10               | Loyalty    | N/A                       | Loyalty discount for returning customers       | In Stock     | 8           | Amazon   | 4.8    | Apple        | Ongoing    |
    | A3001      | Samsung Galaxy S23                               | Electronics/Smartphones   | 900        | 10               | Loyalty    | N/A                       | Loyalty discount for returning customers       | Out of Stock  | 0           | Amazon   | 4.5    | Samsung        | Ongoing    |
    | A4001      | Sony WH-1000XM4 Headphones                       | Electronics/Audio         | 350        | 20               | Time       | N/A                       | Extended warranty available: 6 months          | In Stock     | 20          | Amazon   | 4.8    | Sony           | 2 days    |
    | A5001      | Dell XPS 15 Laptop                               | Electronics/Laptops       | 1500       | 12               | Loyalty    | 12                        | Extended warranty available: 12 months         | In Stock     | 10          | Amazon   | 4.7    | Dell           | Ongoing    |
    | A6001      | Apple AirPods Pro                                | Electronics/Audio         | 250        | 10               | Time       | N/A                       | Loyalty discount available for Prime members   | In Stock     | 30          | Amazon   | 4.9    | Apple          | 30 minutes    |
    | A7001      | Canon EOS Rebel T7 Camera                        | Electronics/Cameras       | 500        | 8                | Inventory  | N/A                       | Last items left                                | Out of Stock  | 0           | Amazon   | 4.4    | Canon          | Until stock lasts |
    | A8001      | Fitbit Versa 3 Smartwatch                        | Electronics/Wearables     | 200        | 10               | Loyalty    | N/A                       | —                                              | In Stock     | 25          | Amazon   | 4.5    | Fitbit         | Ongoing |
    | A9001      | Bose SoundLink Revolve+ Bluetooth Speaker        | Electronics/Audio         | 279        | 15               | Time       | N/A                       | Limited time discount                          | In Stock     | 12          | Amazon   | 4.7    | Bose           | 2 hours |
    | A9002      | Microsoft Surface Pro 8                          | Electronics/Tablets       | 1100       | 12               | Loyalty    | 12                        | Extended warranty option                       | Out of Stock  | 0           | Amazon   | 4.6    | Microsoft      | Ongoing    |
    | A9003      | Nintendo Switch OLED                             | Electronics/Gaming        | 350        | 15               | Inventory  | N/A                       | Only 5 items left                              | In Stock     | 5           | Amazon   | 4.8    | Nintendo       | Until stock lasts |
    | A9004      | GoPro HERO11                                     | Electronics/Cameras       | 500        | 10               | Time       | N/A                       | Time-limited offer                             | In Stock     | 9           | Amazon   | 4.5    | GoPro          | 2 hours |
    | A9005      | HP Envy 6055 All-in-One Printer                  | Electronics/Printers      | 150        | 20               | Inventory  | N/A                       | Last items left                                | Out of Stock  | 0           | Amazon   | 4.2    | HP             | Ongoing |
    | A9006      | LG 27-inch 4K Monitor                            | Electronics/Monitors      | 400        | 10               | Loyalty    | 6                         | Loyalty discount available                     | In Stock     | 7           | Amazon   | 4.6    | LG             | Ongoing |
    | A9007      | Amazon Echo Dot                                  | Electronics/Smart Home    | 50         | 0                | None       | N/A                       | Bundle with Alexa-enabled devices              | In Stock     | 50          | Amazon   | 4.7    | Amazon         | Ongoing |
    | A9008      | Kindle Paperwhite                                | Electronics/E-Readers     | 130        | 10               | Time       | N/A                       | Limited time offer                             | In Stock     | 25          | Amazon   | 4.8    | Amazon         | 1 day |
    | A9009      | Bose QuietComfort 35 II                          | Electronics/Audio         | 299        | 8                | Loyalty    | N/A                       | Loyalty discount for Prime users               | In Stock     | 10          | Amazon   | 4.7    | Bose           | Ongoing    |
    | A9010      | Razer Blade 15 Gaming Laptop                     | Electronics/Laptops       | 1800       | 10               | Time       | 12                        | Extended warranty option                       | Out of Stock  | 0           | Amazon   | 4.6    | Razer          | 1 day |
    | A9011      | NERF Rival Nemesis Blaster                       | Toys & Games              | 50         | 15               | Time       | N/A                       | Limited time offer                             | In Stock     | 30          | Amazon   | 4.5    | NERF         | 10 minutes |
    | A9012      | Hot Wheels Ultimate Garage                       | Toys & Games              | 70         | 15               | Loyalty    | N/A                       | Loyalty discount for members                   | In Stock     | 25          | Amazon   | 4.6    | Hot Wheels   | Ongoing    |
    | A9013      | Barbie DreamHouse Dollhouse                      | Toys & Games              | 250        | 20               | Time       | N/A                       | Seasonal discount                              | Out of Stock  | 0           | Amazon   | 4.7    | Barbie       | 3 minutes |
    | A9014      | Lego Classic Bricks Box                          | Toys & Games              | 40         | 5                | Loyalty    | N/A                       | Bonus loyalty reward points                    | In Stock     | 40          | Amazon   | 4.8    | LEGO         | Ongoing    |
    | A9015      | Instant Pot Duo 7-in-1 Electric Pressure Cooker  | Home & Kitchen           | 90         | 12               | Time       | N/A                       | Holiday discount                               | In Stock     | 15          | Amazon   | 4.7    | Instant Pot  | 4 minutes |
    | A9016      | Dyson V11 Cordless Vacuum                        | Home Appliances          | 600        | 5                | Warranty   | 12                        | Extended warranty available                    | In Stock     | 8           | Amazon   | 4.8    | Dyson        | Ongoing    |
    | A9017      | Sony PlayStation 5 Console                       | Electronics/Gaming        | 500        | 15               | Time       | N/A                       | Hurry, limited availability                    | Out of Stock  | 0           | Amazon   | 4.9    | Sony         | 5 mins    |
    | A9018      | Nike Air Zoom Pegasus Running Shoes              | Fashion/Sports           | 120        | 10               | Loyalty    | N/A                       | Exclusive loyalty discount                     | In Stock     | 20          | Amazon   | 4.7    | Nike         | Ongoing    |
    | A9019      | Under Armour Men's Tech T-Shirt                  | Fashion                  | 30         | 15               | Time       | N/A                       | Seasonal promotion                             | In Stock     | 35          | Amazon   | 4.4    | Under Armour | 30 minites    |
    | A9020      | KitchenAid Stand Mixer                           | Home & Kitchen           | 350        | 8                | Warranty   | 18                        | Extended warranty available                    | In Stock     | 12          | Amazon   | 4.9    | KitchenAid   | Ongoing    |
    | A9021      | Samsung 65-inch QLED Smart TV                    | Electronics/TV           | 1000       | 10               | Warranty   | 24                        | Exclusive extended warranty                    | In Stock     | 5           | Amazon   | 4.8    | Samsung      | Ongoing    |
    | A9022      | Canon PIXMA Wireless Printer                     | Electronics/Printers     | 130        | 10               | Time       | N/A                       | Limited time promotion                         | In Stock     | 10          | Amazon   | 4.5    | Canon        | 2 minutes    |
                    """
                },
                {
                    "user_id" : "Croma",
                    "access" : ["HDFCBank", "ICICIBank"],
                    "about" : "Croma is an e-commerce platform that sells a variety of products and adds discounts.",
                    "products_inventory" : """
    | Product_ID | Product_Name                                     | Category                  | Base_Price | Offer_Percentage | Offer_Type | Warranty_Extension_Months | Additional_Offers                                 | Availability | Stock_Count | Merchant | Rating | Brand             |Offer_Expiry|
    |------------|--------------------------------------------------|---------------------------|------------|------------------|------------|---------------------------|---------------------------------------------------|--------------|-------------|----------|--------|-------------------|------------|
    | C1001      | Star Wars Lego Death Star Set                    | Toys & Games              | 255        | 0                | Time       | N/A                       | Festive season discount                           | Out of Stock | 0           | Croma    | 4.7    | LEGO              | 10 minutes |
    | C1002      | Star Wars Lego Millennium Falcon                 | Toys & Games              | 310        | 10               | Loyalty    | N/A                       | Loyalty points applicable                         | In Stock     | 10          | Croma    | 4.6    | LEGO Star Wars    | Ongoing |
    | C2001      | iPhone 14 Pro                                    | Electronics/Smartphones   | 1190       | 8                | Warranty   | 18                        | Extended Warranty Option: 18 months               | In Stock     | 3           | Croma    | 4.8    | Apple             | Ongoing |
    | C2002      | iPhone 14                                        | Electronics/Smartphones   | 980        | 5                | Time       | N/A                       | Special seasonal discount                         | In Stock     | 7           | Croma    | 4.6    | Apple             | 5 minutes |
    | C9023      | Star Wars Lightsaber Replica                     | Toys & Games              | 155        | 18               | Time       | N/A                       | Limited edition offer                           | In Stock     | 8           | Croma    | 4.8    | Hasbro Star Wars  | 1 hour |
    | C9024      | Star Wars Stormtrooper Helmet                    | Toys & Games              | 210        | 12               | Loyalty    | N/A                       | Collector's exclusive                           | Out of Stock | 0           | Croma    | 4.7    | Sideshow          | Ongoing |
    | C9025      | Star Wars R2-D2 Action Figure                    | Toys & Games              | 85         | 20               | Time       | N/A                       | Festive discount                                | In Stock     | 15          | Croma    | 4.6    | Mattel            | 30 minutes |
    | C9026      | iPhone 14 Pro Max                                | Electronics/Smartphones   | 1390       | 8                | Warranty   | 24                        | Extended warranty available                     | In Stock     | 5           | Croma    | 4.8    | Apple             | Ongoing |
    | C9027      | iPhone 14 Plus                                   | Electronics/Smartphones   | 1090       | 10               | Loyalty    | N/A                       | Loyalty discount for frequent buyers            | In Stock     | 9           | Croma    | 4.7    | Apple             | Ongoing |
    | C3001      | Samsung Galaxy S23                               | Electronics/Smartphones   | 890        | 12               | Loyalty    | N/A                       | Exclusive loyalty discount                        | In Stock     | 12          | Croma    | 4.5    | Samsung           | Ongoing |
    | C4001      | Sony WH-1000XM4 Headphones                       | Electronics/Audio         | 340        | 15               | Inventory  | N/A                       | Extended warranty available: 6 months             | In Stock     | 4           | Croma    | 4.7    | Sony              | Until stock lasts |
    | C5001      | Dell XPS 15 Laptop                               | Electronics/Laptops       | 1450       | 10               | Time       | 12                        | Extended warranty option: 12 months               | Out of Stock | 0           | Croma    | 4.6    | Dell              | 2 days |
    | C6001      | Apple AirPods Pro                                | Electronics/Audio         | 245        | 5                | Loyalty    | N/A                       | Loyalty discount for premium members              | In Stock     | 20          | Croma    | 4.8    | Apple             | Ongoing |
    | C7001      | Canon EOS Rebel T7 Camera                        | Electronics/Cameras       | 520        | 5                | Warranty   | 6                         | Warranty Extension Option: 6 months               | In Stock     | 6           | Croma    | 4.3    | Canon             | Ongoing |
    | C8001      | Fitbit Versa 3 Smartwatch                        | Electronics/Wearables     | 210        | 0                | Time       | N/A                       | Seasonal offer                                    | Out of Stock | 0           | Croma    | 4.4    | Fitbit            | 15 minutes |
    | C9001      | Bose SoundLink Revolve+ Bluetooth Speaker        | Electronics/Audio         | 285        | 5                | Inventory  | N/A                       | Limited stock offer                               | In Stock     | 8           | Croma    | 4.6    | Bose              | Until stock lasts |
    | C9002      | Microsoft Surface Pro 8                          | Electronics/Tablets       | 1120       | 10               | Loyalty    | 12                        | Extended warranty option                          | In Stock     | 6           | Croma    | 4.5    | Microsoft         | Ongoing |
    | C9003      | Nintendo Switch OLED                             | Electronics/Gaming        | 360        | 12               | Inventory  | N/A                       | Only a few units available                        | In Stock     | 4           | Croma    | 4.8    | Nintendo          | Until stock lasts |
    | C9004      | GoPro HERO11                                     | Electronics/Cameras       | 510        | 0                | Time       | N/A                       | Time-limited promotion                            | In Stock     | 7           | Croma    | 4.5    | GoPro             | 2 minutes |
    | C9005      | HP Envy 6055 All-in-One Printer                  | Electronics/Printers      | 155        | 15               | Inventory  | N/A                       | Special discount, limited stock                   | In Stock     | 2           | Croma    | 4.2    | HP                | Until stock lasts |
    | C9006      | LG 27-inch 4K Monitor                            | Electronics/Monitors      | 410        | 8                | Loyalty    | 6                         | Loyalty discount applied                          | In Stock     | 5           | Croma    | 4.6    | LG                | Ongoing |
    | C9007      | Amazon Echo Dot                                  | Electronics/Smart Home    | 52         | 5                | Time       | N/A                       | Limited time offer                                | In Stock     | 40          | Croma    | 4.7    | Amazon            | 10 minutes |
    | C9008      | Kindle Paperwhite                                | Electronics/E-Readers     | 135        | 0                | None       | N/A                       | —                                                 | In Stock     | 30          | Croma    | 4.8    | Amazon            | Ongoing |
    | C9009      | Bose QuietComfort 35 II                          | Electronics/Audio         | 310        | 10               | Inventory  | N/A                       | Only a few left                                   | In Stock     | 5           | Croma    | 4.7    | Bose              | Until stock lasts |
    | C9010      | Razer Blade 15 Gaming Laptop                     | Electronics/Laptops       | 1750       | 0                | Warranty   | 12                        | Warranty extension available                      | Out of Stock | 0           | Croma    | 4.6    | Razer             | Ongoing |
    | C9011      | NERF Rival Nemesis Blaster                       | Toys & Games              | 52         | 15               | Time       | N/A                       | Limited time promotion                            | In Stock     | 25          | Croma    | 4.4    | NERF              | 5 minutes |
    | C9012      | Hot Wheels Ultimate Garage                       | Toys & Games              | 72         | 12               | Loyalty    | N/A                       | Loyalty bonus discount                            | In Stock     | 18          | Croma    | 4.5    | Hot Wheels        | Ongoing |
    | C9013      | Barbie DreamHouse Dollhouse                      | Toys & Games              | 260        | 18               | Time       | N/A                       | Festive discount                                  | In Stock     | 3           | Croma    | 4.8    | Barbie            | 2 minutes |
    | C9014      | Lego Classic Bricks Box                          | Toys & Games              | 42         | 5                | Loyalty    | N/A                       | Bonus loyalty reward points                       | In Stock     | 35          | Croma    | 4.7    | LEGO              | Ongoing |
    | C9015      | Instant Pot Duo 7-in-1 Electric Pressure Cooker  | Home & Kitchen           | 88         | 15               | Time       | N/A                       | Festive offer                                     | In Stock     | 10          | Croma    | 4.6    | Instant Pot       | 10 minutes |
    | C9016      | Dyson V11 Cordless Vacuum                        | Home Appliances          | 610        | 7                | Warranty   | 12                        | Extended warranty promotion                       | Out of Stock | 0           | Croma    | 4.7    | Dyson             | Ongoing |
    | C9017      | Sony PlayStation 5 Console                       | Electronics/Gaming        | 510        | 15               | Time       | N/A                       | Hurry, limited availability                       | In Stock     | 2           | Croma    | 4.9    | Sony              | 30 minutes |
    | C9018      | Nike Air Zoom Pegasus Running Shoes              | Fashion/Sports           | 125        | 8                | Loyalty    | N/A                       | Exclusive member discount                         | In Stock     | 15          | Croma    | 4.7    | Nike              | Ongoing |
    | C9019      | Under Armour Men's Tech T-Shirt                  | Fashion                  | 32         | 10               | Time       | N/A                       | Seasonal offer                                    | In Stock     | 40          | Croma    | 4.5    | Under Armour      | 2 minutes |
    | C9020      | KitchenAid Stand Mixer                           | Home & Kitchen           | 360        | 7                | Warranty   | 18                        | Extended warranty available                       | In Stock     | 10          | Croma    | 4.9    | KitchenAid        | Ongoing |
    | C9021      | Samsung 65-inch QLED Smart TV                    | Electronics/TV           | 1020       | 9                | Warranty   | 24                        | Premium warranty offer                            | Out of Stock | 0           | Croma    | 4.8    | Samsung           | Ongoing |
    | C9022      | Canon PIXMA Wireless Printer                     | Electronics/Printers     | 135        | 10               | Time       | N/A                       | Limited time promotion                            | In Stock     | 8           | Croma    | 4.6    | Canon             | 5 hours |
                    """,
                },
            ],
            "system_message" : """You are an merchant assistant for {user_id}. You are responsible for handling {user_id} product inquiries from issuer/bank agents only and responding with relevant product information.  

    1. Core Responsibilities:  
        - Receive product request from issuer/bank agents.  
        - Check stock availability and return exact product details if available.  
        - If a requested product is unavailable, suggest the most relevant alternative based on category, price, and brand.  
        - Communicate applicable promotions, discounts, and limited-time offers to the issuer.  

    2. Task Management & Agent Communication Interactions:  
        - Process incoming messages and scheduled reminders without user/operator intervention when possible
        - Create and manage tasks autonomously based on known patterns
        - Schedule reminders and follow-ups automatically using the schedule tool
        - Issuer Agent: Sends product inquiries based on user information and requests.  
        - User/Operator: Only involve your user/operator when:
            * You encounter an unknown situation requiring judgment
            * You need approval for important decisions
            * You've completed a significant task
        - All messages must be through the tool call reponse
        - When you are communicating with Issuer agents, they know that you are an AI assistant


    3. Product Selection Rules: 
        - If the requested product is in stock, return its details.  
        - If out of stock, suggest an alternative based on:  
            - Same Category & Brand (e.g., iPhone 14 Pro → iPhone 14 Plus).  
            - Similar Price Range (Match within ±10% of the requested product).  
            - Stock Availability (Prioritize in-stock items over out-of-stock options).  
        - Apply available offers:  
            - Loyalty-based discounts (if user is eligible).  
            - Time-sensitive deals (if the offer is expiring soon).  
            - Inventory-based discounts (if stock is low).  

    4. Offer Communication with Issuer Agent
    - If a product has a time-sensitive discount, notify the issuer to act quickly.  
    - If a product has a loyalty or inventory-based offer, provide details.  
    - If an alternative product is suggested, ensure it meets the user’s expected category and price range.  

    Refer to the **tables below** for detailed product details and select the **best-suited products** for the issuers/bank agent requests.  

    **{user_id}'s Available Product Inventory**
    {products_inventory}

    User/Operator ID: {user_id}
"""
        }
    }
