#Taste of Italy

## Purpose of the project

The purpose of this project was to build a Full-Stack site based on business logic used to control a centrally-owned dataset. Aim was to set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product

## Wireframes
- [Home page](readme_media/wireframe1.PNG) For the front page, not much has changed during the production from the original idea apart from some layout changes.
- [Menu](readme_media/wireframe2.PNG) The menu has stayed as planned from the beginning, however, I removed the checkout box as it was causing a lot of responsive issues with the menu cards
-[Checkout](readme_media/wireframe3.PNG) The check out has stayed true to the wireframe plan, a simple form with details of the order next to the form.
- A lot of desing change has happened during the building of the website as I was heavily influenced by a templated, but tried to stay with original desings.

## Agile Methodology
- While working on this project I used Agile tools provided by github such as the project board, which helped focus on prioritising and seeing what user stories are left to do, in progress or done.
![Project board](readme_media/projectboard.PNG)

- Another tool that I used was the Milestones that can be set in github, by creating the milestones I was able to group certain user stories together that worked along each other and allowed me to focus on particular side of the design 
![Milestones](readme_media/sprints.PNG)

## User stories and their features
(User stories can be accessed by clicking user stories id number)

- Visiting user
    - As a visitng site user I would like to easily register for an account to have a personal account [#1](https://github.com/kcichy37/fifth_portfolio_project/issues/1)
    - As a shopper I would like to be able to view the products the business has to offer for purchase [#6](https://github.com/kcichy37/fifth_portfolio_project/issues/6)
    - As a shopper I would like to able to see the details of individual products [#7](https://github.com/kcichy37/fifth_portfolio_project/issues/7)
    - As a shopper I would like to easily view the items I am purchasing and the total amount I’m spending [#8](https://github.com/kcichy37/fifth_portfolio_project/issues/8)
    - As a shopper I can sort the products by categories so I can sort through what I want [#9](https://github.com/kcichy37/fifth_portfolio_project/issues/9)
    - As a shopper I would like to be able to increase quantity of my chosen products [#10](https://github.com/kcichy37/fifth_portfolio_project/issues/10)
    - As a shopper I would like to be able to delete products I don’t want anymore [#11](https://github.com/kcichy37/fifth_portfolio_project/issues/11)
    - As a shopper I would like to have my transaction go through securely no matter of what happens [#12](https://github.com/kcichy37/fifth_portfolio_project/issues/12)
    - As a shopper I would like to receive email confirming my purchase, so I know my order is processed [#13](https://github.com/kcichy37/fifth_portfolio_project/issues/13)

- Registered ser
    - As a registered site user I would like to easily log in and log out so I can view my personal information [#2](https://github.com/kcichy37/fifth_portfolio_project/issues/2)
    - As a registered site user I would like to easily reset my password in case I forget it to recover access to my account [#3](https://github.com/kcichy37/fifth_portfolio_project/issues/3)
    - As a registered site user I would like to receive an email confirmation to verify my account [#4](https://github.com/kcichy37/fifth_portfolio_project/issues/4)
    - As a registered site user I would like my account to be secure so no one else has access to it [#5](https://github.com/kcichy37/fifth_portfolio_project/issues/5)
    - As a registered site user I would like my account to be secure so no one else has access to it [#15](https://github.com/kcichy37/fifth_portfolio_project/issues/15)
    - As a registered site user I would like to be able to save my details, so I don’t have to re-enter them if I order again [#16](https://github.com/kcichy37/fifth_portfolio_project/issues/16)
    - As a registered site user I want the site to show if my interactions were successful or failed so I know if its all working [#17](https://github.com/kcichy37/fifth_portfolio_project/issues/17)
    - As a registered site user I would like to be able to add products to my favourites for quick access to my favourite products [#18](https://github.com/kcichy37/fifth_portfolio_project/issues/18)
    - As a registered site user I would like to be able to add favourite products straight to the bag from the page so I dont have to browse [#19](https://github.com/kcichy37/fifth_portfolio_project/issues/19)
    - As a registered site user I would like to be able to delete my favourites if I dont like them anymore [#20](https://github.com/kcichy37/fifth_portfolio_project/issues/20)
    - As a registered site user I would like to be able to leave a review [#21](https://github.com/kcichy37/fifth_portfolio_project/issues/21)
    - As a registered site user I would like to be able to delete my reviews [#23](https://github.com/kcichy37/fifth_portfolio_project/issues/23)

- Admin
    - As an admin I would like to be able to view the orders so that they can be processed [#14](https://github.com/kcichy37/fifth_portfolio_project/issues/14)
    - As an admin I would like to be able to control users reviews incase they are inappropriate [#24](https://github.com/kcichy37/fifth_portfolio_project/issues/24)


## Additional features 

- Home page
    - Home page consists of a nav bar which includes the companies logo as well as 3 navigation buttons, a dropdown button which is a 'My Account' dropdown with login or register options. after login in the options become tabs for users, Admin user have extra tabs such as Product management and adding a product and finally a bag button with the total.
    - Home page consists of 4 sections, first the greeting section with a background and short description of Taste of Italy as well as the opening hours. Second the about us section which gives a background to the company. Third is the brief takeaway menu description with a button that navigates to the menu. Last section is the Testimonial section were registered user can leave a review, the reviews are in a carousel that switches between all reviews.
    ![Section 1](readme_media/section1.PNG "First Section")
    ![Section 2](readme_media/section2.PNG "Second Section")
    ![Section 3](readme_media/section3.PNG "Third Section")
    ![Section 4](readme_media/section4.PNG "Fourth Section")

- Takeaway page
    - The takeaway page is divide into 9 categories that represent the food eg. starters or pizza. For quick navigation theres a navbar at the top which jumps to the category selected by user.
    ![Takeaway page](readme_media/takeaway.PNG "Takeaway page")
    - Products on the takeway page are shown in a card with all details such us description - if description is too long then it will hide and show 'read more' - in addition the price and calories. With these you also get the option to choose your quantity and then Add button that adds to the bag, updating the bag total on the nav bar.
    [Updated Bag](readme_media/bagupdate.PNG)

- Bag page
    - After adding products from the takeaway page, they show up on the bag page where user can still update the quantity of product they want or delete products they dont want anymore.
    - Theres 2 buttons, to go back to the menu page in case user wants to add more products, and a checkout button navigating to checkout. 
    ![Bag page](readme_media/bag.PNG "Bag page")

- Checkout page
    - After user confirms his order in the bag, they will be presented with a checkout page, where theres two section, one to input delivery and payment details and second one recaps users order. 
    ![Checkout page](readme_media/checkout.PNG "Checkout page")
    - If user is satisfied with his order and input correct details, the page will process his payment via Stripe. After successful payment the site shows a order summery page confirming the order.
    ![Order confirmation](readme_media/orderconfirmation.PNG "Order confirmation")

- Footer
    - Footer contains a brief repeat of main information such as opening hours, about the company,social media links, and contact us, as well as a newsletter sign up.
    ![Footer](readme_media/footer.PNG "Footer")
