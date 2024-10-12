<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]

![Product Name Screen Shot][product-screenshot]
<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">Bulk queries with ShopifyAPI / GraphQL / Python / Pandas</h1>

</div>



<!-- ABOUT THE PROJECT -->
## 📁 About The Project



This is a project you can do bulk queries to extract data from your Online Shopify Store, Making bulk queries through [Shopify API](https://shopify.dev/docs/api/usage/bulk-operations/queries) using GraphQL queries and Python.


<p align="right">(<a href="#top">back to top</a>)</p>



### 🚀 Built With

* [Python](https://github.com/Shopify/shopify_python_api)
* [Jupyter Note](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## ✅ Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### 🖥️ Installation

1. Clone the repo

   ```sh
   git clone https://github.com/paolobang/bulk-shopify-python.git
   ```

2. Create your ACCESS TOKEN

    You must create your ACCESS TOKEN in Shopify Dashboard, you can follow all steps from the [official documentation](https://help.shopify.com/es/manual/apps/app-types/custom-apps?shpxid=534cde3b-B4F8-4753-D4E0-CCA3640020E9). 


3. Install NPM packages
    
    Install [ShopifyAPI](https://pypi.org/project/ShopifyAPI/) or upgrade it to the last version.
    ```bash
    pip3 install ShopifyAPI
    ```

    Install [Pandas](https://pypi.org/project/pandas/).

    ```bash
    pip3 install pandas
    ```

    Install [python-dotenv](https://pypi.org/project/python-dotenv/).

    ```bash
    pip3 install python-dotenv
    ```

4. Replace variables in .env file

    ```env
    MERCHANT = 'YourStoreName.myshopify.com'
    TOKEN = 'shpat_123a4sca....' 
    API_VERSION = '2023-01'
    ```
    
5. Open "main.ipynb" file and restart kernel before to run it.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## ✏️ Usage

You can use to extract data from your Online Shopify Store and make any type of analysis you want.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## 🎯 Roadmap

See the [open issues](https://github.com/paolobang/bulk-shopify-python/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## 👋 Contact

[Linkedin](https://www.linkedin.com/in/juniorhuamanr/) - juniorhuamanro@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/paolobang/bulk-shopify-python.svg?style=for-the-badge
[contributors-url]: https://github.com/paolobang/bulk-shopify-python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/paolobang/bulk-shopify-python.svg?style=for-the-badge
[forks-url]: https://github.com/paolobang/bulk-shopify-python/network/members
[stars-shield]: https://img.shields.io/github/stars/paolobang/bulk-shopify-python.svg?style=for-the-badge
[stars-url]: https://github.com/paolobang/bulk-shopify-python/stargazers
[issues-shield]: https://img.shields.io/github/issues/paolobang/bulk-shopify-python.svg?style=for-the-badge
[issues-url]: https://github.com/paolobang/bulk-shopify-python/issues
[license-shield]: https://img.shields.io/github/license/paolobang/bulk-shopify-python.svg?style=for-the-badge
[license-url]: https://github.com/paolobang/bulk-shopify-python/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/juniorhuamanr/
[product-screenshot]: /assets/screen.png
