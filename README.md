# llm-chatbot 
# Chatbot Testing
# Chatbot Test Results

This document contains the results of 20 test questions executed on the chatbot. Each test case includes the expected and actual responses, along with a status (Pass/Fail) and relevant screenshots.

## Test Results

### Test Case TQ001: Vegetarian Lasagna Recipes
**Test Scenario**: Retrieve vegetarian lasagna recipes.

- **Test Steps**:
  1. Launch the chatbot locally using `streamlit run chatbot.py`.
  2. Ask: "What are some vegetarian lasagna recipes?"
- **Expected Result**: A list of vegetarian lasagna recipes with links (e.g., “Vegetarian Lasagna With Easy Roasted Tomato Sauce” with the link).
- **Actual Result**: It did provide links to vegetarian lasagna recipes, but it thought the prompt was asking for smores recipes. 
- **Status**: Fail

![Response for TQ001](https://github.com/trodman201/llm-chatbot/blob/testing/TQ001_Response.png) 

---

### Test Case TQ002: Simple Pasta Recipe for Beginners
**Test Scenario**: Retrieve a simple pasta recipe suitable for beginners.

- **Test Steps**:
  Ask: "Can you give me a simple pasta recipe for beginners?"
- **Expected Result**: A pasta recipe suitable for beginners with a link (e.g., “Pasta with Tomato Sauce” with the link).
- **Actual Result**: Chatbot returned links to pasta recipes for beginners
- **Status**: Pass

![Response for TQ002](https://github.com/trodman201/llm-chatbot/blob/testing/TQ002_Response.png) 
---

### Test Case TQ003: Homemade Pizza Dough
**Test Scenario**: Retrieve a recipe for homemade pizza dough.

- **Test Steps**:
  Ask: "I need a recipe for homemade pizza dough."
- **Expected Result**: A recipe for pizza dough with the link (e.g., “Homemade Pizza Dough Recipe” with the link).
- **Actual Result**: Chatbot returned recommendations and links to making homemade pizza dough
- **Status**: Pass

![Response for TQ003](https://github.com/trodman201/llm-chatbot/blob/testing/TQ003_Response.png) 

---

### Test Case TQ004: Quick Weeknight Dinners
**Test Scenario**: Retrieve quick recipes for weeknight dinners.

- **Test Steps**:
  Ask: "What are some quick recipes for weeknight dinners?"
- **Expected Result**: A list of quick weeknight dinner recipes with links (e.g., “15-Minute Stir Fry” with the link).
- **Actual Result**: Chatbot returned recommendations and links to cooking quick weeknight dinners
- **Status**: Pass

![Response for TQ004](https://github.com/trodman201/llm-chatbot/blob/testing/TQ004_Response.png) 

---

### Test Case TQ005: Chicken Curry with Rice
**Test Scenario**: Retrieve a recipe for chicken curry with rice.

- **Test Steps**:
  Ask: "Can you give me a recipe for chicken curry with rice?"
- **Expected Result**: A recipe for chicken curry with rice and the link (e.g., “Easy Chicken Curry” with the link).
- **Actual Result**: Chatbot retunred recommendations and links to cooking chicken curry with rice
- **Status**: Pass

![Response for TQ005](https://github.com/trodman201/llm-chatbot/blob/testing/TQ005_Response.png) 

--- 
### Test Case TQ006: Cooking with Chicken Thighs
**Test Scenario**: Retrieve ideas for using chicken thighs as an ingredient. 

- **Test Steps**:
  Ask: "What can I make with chicken thighs?"
- **Expected Result**: A list of recipes using chicken thighs with links (e.g., “Braised Chicken Thighs” with the link).
- **Actual Result**: Chatbot returned recommendations and links to cooking with chicken thighs
- **Status**: Pass

![Response for TQ006](https://github.com/trodman201/llm-chatbot/blob/testing/TQ006_Response.png) 

---
### Test Case TQ007: Cooking with Tomatoes and Basil
**Test Scenario**: Retrieve recipes that use tomatoes and basil. 
- **Test Steps**:
  Ask: "What are some recipies that use tomatoes and basil?"
- **Expected Result**: A list of recipes that use tomatoes and basil with links (e.g., “Tomato Basil Salad” with the link).
- **Actual Result**: The chatbot returned both recommendations and links to cooking with tomatoes/basil
- **Status**: Pass

![Response for TQ007](https://github.com/trodman201/llm-chatbot/blob/testing/TQ007_Response.png) 
---
### Test Case TQ008: Cooking with Mushrooms
**Test Scenario**: Retrieve recipes that use mushrooms. 
- **Test Steps**:
  Ask: "Can you show me recipes with mushrooms as the main ingredient?"
- **Expected Result**: A list of mushroom-based recipes with links (e.g., “Mushroom Risotto” with the link).
- **Actual Result**: The chatbot returned both recommendations and links to cooking with mushrooms
- **Status**: Pass

![Response for TQ008](https://github.com/trodman201/llm-chatbot/blob/testing/TQ008_Response.png) 

---
### Test Case TQ009: Cooking with Sweet Potatoes
**Test Scenario**: Retrieve recipes that use sweet potatoes. 
- **Test Steps**:
  Ask: "What dishes can I make with sweet potatoes?"
- **Expected Result**:  A list of recipes using sweet potatoes with links (e.g., “Sweet Potato Fries” with the link).
- **Actual Result**: The chatbot returned both recommendations and links for cooking with sweet potatoes
- **Status**: Pass

![Response for TQ009](https://github.com/trodman201/llm-chatbot/blob/testing/TQ009_Response.png) 

---
### Test Case TQ010: Cooking with Dark Chocolate
**Test Scenario**: Retrieve recipes that use dark chocolate.  
- **Test Steps**:
  Ask: "Can you give me some dessert ideas with dark chocolate?"
- **Expected Result**: A list of dessert recipes with dark chocolate and links (e.g., “Chocolate Lava Cake” with the link). 
- **Actual Result**: The chatbot returned both recommendations and links for cooking with dark chocolate
- **Status**: Pass

![Response for TQ010](https://github.com/trodman201/llm-chatbot/blob/testing/TQ010_Response.png) 


--- 
### Test Case TQ011: Thanksgiving Dinner Menu 
**Test Scenario**: Retrieve ideas for a Thanksgiving dinner.  
- **Test Steps**:
  Ask: "Can you suggest a Thanksgiving dinner menu?"
- **Expected Result**: A suggested menu for Thanksgiving with recipe links (e.g., “Roast Turkey” with the link).
- **Actual Result**: The chatbot returned both recommendations and links for a Thanksgiving Dinner Menu
- **Status**: Pass

![Response for TQ011](https://github.com/trodman201/llm-chatbot/blob/testing/TQ011_Response.png) 

---
### Test Case TQ012: New Years Eve Party  
**Test Scenario**: Retrieve ideas for a New Year's Eve party menu.  
- **Test Steps**:
  Ask: "What should I make for a New Year's Eve party?"
- **Expected Result**: Recipe suggestions for a New Year’s Eve party with links (e.g., “Shrimp Cocktail” with the link).
- **Actual Result**: The chatbot returned both recommendations and links for a New Year's Eve Party menu
- **Status**: Pass

![Response for TQ012](https://github.com/trodman201/llm-chatbot/blob/testing/TQ012_Response.png) 

---
### Test Case TQ013: Summer Barbecue 
**Test Scenario**: Retrieve ideas for a summer barbecue.  
- **Test Steps**:
  Ask: "I need some ideas for a summer barbecue"
- **Expected Result**:  A list of barbecue recipes with links (e.g., “BBQ Ribs” with the link).
- **Actual Result**: The chatbot returned both recommendations and links to summer barbecue ideas
- **Status**: Pass

![Response for TQ013](https://github.com/trodman201/llm-chatbot/blob/testing/TQ013_Response.png) 

---
### Test Case TQ014: Romantic Dinner Recipes 
**Test Scenario**: Retrieve ideas for a romantic dinner.  
- **Test Steps**:
  Ask: "What are some romantic dinner ideas for two?"
- **Expected Result**:  A list of romantic dinner recipes with links (e.g., “Lobster Tail” with the link).
- **Actual Result**: The chatbot returned both recommendations and links to romantic dinner recipes
- **Status**: Pass

![Response for TQ014](https://github.com/trodman201/llm-chatbot/blob/testing/TQ014_Response.png) 

--- 
### Test Case TQ015: Christmas Desserts
**Test Scenario**: Retrieve ideas for Christmas desserts.  
- **Test Steps**:
  Ask: "Can you give me ideas for Christmas Desserts?"
- **Expected Result**:  A list of Christmas dessert recipes with links (e.g., “Gingerbread Cookies” with the link).
- **Actual Result**: The chatbot returned both recommendations and links to Christmas dessert ideas
- **Status**: Pass

![Response for TQ015](https://github.com/trodman201/llm-chatbot/blob/testing/TQ015_Response.png) 

---
### Test Case TQ016: Best Pasta Maker
**Test Scenario**: Retrieve reccommendations for best pasta maker to use.  
- **Test Steps**:
  Ask: "What is the best pasta maker to use at home?"
- **Expected Result**:  A recommendation for the best pasta maker with explanations (e.g., “Marcato Atlas Pasta Maker” with details).
- **Actual Result**: While it did provide some recommendations, the retrived links returned a 404 error/didnt work
- **Status**: Fail 
![Response for TQ016](https://github.com/trodman201/llm-chatbot/blob/testing/TQ016_Response.png)  
---
### Test Case TQ017: Good Chef's Knife
**Test Scenario**: Retrieve recommendations for good chef's knife.  
- **Test Steps**:
  Ask: "Do you have reccomendations for a good chef's knife?"
- **Expected Result**:  A recommendation for a good chef's knife with details (e.g., “Wüsthof Classic Chef’s Knife” with explanations).
- **Actual Result**: While it did provide some recommendations, the retrived links returned a 404 error/didnt work
- **Status**: Fail 
![Response for TQ017](https://github.com/trodman201/llm-chatbot/blob/testing/TQ017_Response.png) 
---
### Test Case TQ018: Blenders for Smoothies
**Test Scenario**: Retrieve recommendations for blenders to use for smoothies.  
- **Test Steps**:
  Ask: "Which blenders are best for making smoothies?"
- **Expected Result**:  A list of recommended blenders for smoothies (e.g., “Vitamix 5200 Blender” with details).
- **Actual Result**: While it did provide some recommendations, the retrived links returned a 404 error/didnt work
- **Status**: Fail
![Response for TQ018](https://github.com/trodman201/llm-chatbot/blob/testing/TQ018_Response.png)

---
### Test Case TQ019: Kitchen Tools for Home Baker
**Test Scenario**: Retrieve reccomendations for kitchen tools that home bakers use.  
- **Test Steps**:
  Ask: "What kitchen tools are essential for a home baker?"
- **Expected Result**:  A list of essential kitchen tools for home bakers (e.g., “KitchenAid Stand Mixer” with details).
- **Actual Result**: While it did provide some recommendations, the retrived links returned a 404 error/didnt work
- **Status**: Fail
![Response for TQ019](https://github.com/trodman201/llm-chatbot/blob/testing/TQ019_Response.png) 

---
### Test Case TQ020: Cookware for Stews
**Test Scenario**: Retrieve reccomendations for cookware for stews.  
- **Test Steps**:
  Ask: "Whats the best cookware for making stews?"
- **Expected Result**:  A list of recommended cookware for stews (e.g., “Le Creuset Dutch Oven” with explanations). 
- **Actual Result**: While it did provide some recommendations, the retrived links returned a 404 error/didnt work 
- **Status**: Fail

![Response for TQ020](https://github.com/trodman201/llm-chatbot/blob/testing/TQ020_Response.png) 

---
## Summary
| Test Case ID | Question                                   | Status |
|--------------|-------------------------------------------|--------|
| TQ001        | Vegetarian Lasagna Recipes               | Fail |
| TQ002        | Simple Pasta Recipe for Beginners        | Pass  |
| TQ003        | Homemade Pizza Dough                     | Pass  |
| TQ004        | Quick Weeknight Dinners                  | Pass  |
| TQ005        | Chicken Curry with Rice                  | Pass   | 
| TQ006        | Cooking with Chicken Thighs              | Pass   | 
| TQ007        | Cooking with Tomatoes and Basil          | Pass   |
| TQ008        | Cooking with Mushrooms                   | Pass  |   
| TQ009        | Cooking with Sweet Potatoes              | Pass   | 
| TQ010        | Cooking with Dark Chocolate              | Pass   | 
| TQ011        | Thanksgiving dinner menu                 | Pass   |
| TQ012        | New Years Eve Party                      | Pass   | 
| TQ013        | Summer barbecue                          | Pass   | 
| TQ014        | Romantic Dinner Recipes                  | Pass   |
| TQ015        | Christmas Desserts                       | Pass   | 
| TQ016        | Best Pasta maker                         | Fail   |
| TQ017        | Good Chef's Knife                        | Fail   |
| TQ018        | Blenders for Smoothies                   | Fail   |
| TQ019        | Kitchen Tools for home baker             | Fail   |
| TQ020        | Cookware for Stews                       | Fail   | 

## Notes


## Limitations


---


