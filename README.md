# CompareHack - [Single Digital Gateway 2019](http://hackforgood.net)
>:trophy: Project distinguished with the *Jury's Coup de Coeur* award at the [Single Digital Gateway Hackathon](https://hackforgood.net/premios-hackforgood-globales-2017/) in Barcelona, an event organized by the [European Commission](https://ec.europa.eu/growth/content/single-digital-gateway-hackathon-barcelona-edition_en) in collaboration with [Garage 48](https://garage48.org/events/single-digital-gateway-or-database). Read more about it [here](https://ec.europa.eu/docsroom/documents/35541/attachments/1/translations/en/renditions/native).

__Web searcher to help manufacturers and traders get the rules that apply to their products within the EU.__

There are two types of product rules: EU (harmonized) and National (non-harmonized). Since the information is not unified it is difficult for people and businesses to search for the regulations of the products that they are dealing with. **CompareHack** allows to select any product and two countries and then searches:
- The information available at [EU Trade Helpdesk](https://trade.ec.europa.eu/tradehelp/) to get the EU legislation.
- The notifications issued by the selected countries to the EU for the national regulations -`Spain`, `France` and `United Kingdom` at the moment. These notifications were provided by the EU Comission and can be found at [resources/pdfs/](/resources/pdfs/).

In order to make queries relevant **CompareHack** applies NLP (natural language processing) through the [nltk](https://www.nltk.org/).

## Getting started
A live version of the end result is hosted at Heroku: [comparehack.herokuapp.com](https://comparehack.herokuapp.com/).

### Usage steps

1. Once in [comparehack.herokuapp.com](https://comparehack.herokuapp.com/), fill every field:
    - **Product**: any product you want.
    - **Country of destination**: `Spain`, `France` or `United Kingdom`.
    - **Additional country**: `Spain`, `France` or `United Kingdom`.

3. Click **Search** to load the results. If the searched product has multiple definitions, a legal notice section will show up.

4. Below will be three blue buttons:
    - The first -**EU legislation**- containing links of the [EU Trade Helpdesk](https://trade.ec.europa.eu) about the product requirements.
    - The second -**_Country of destination_**- showing the PDF's of the notifications for the national regulations from the country of destination to the European Comission.
    - The third -**_Additional country_**- showing the PDF's of the notifications for the national regulations  from the additional country to the European Comission.
5. Under the buttons will be a form with an empty field:
    - **How has been your experience your far?**: once your text is submitted, a list of all past opinions will be shown.

### Screenshots
![screenshot](http://ignasioliver.com/public/CompareHack/all_fish_cut.png)

## Installation
To install **CompareHack** in your system, make sure [Python](https://www.python.org/downloads/) is installed.
1. [Clone/fetch/pull](https://help.github.com/en/articles/cloning-a-repository) the repository to your system.
2. It is recommended to run the application through a [virtual environment](https://docs.python.org/3/tutorial/venv.html). For example, [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). In a Linux a terminal:
    - `pip3 install virtualenv`
    - `virtualenv venv`
    - `source venv/bin/activate`
3. Install the requirements:
    - `pip3 install -r requirements.txt`<br>
    The code is proven to work with the following package versions:<br>
    `flask-1.0.3` `flask-bootstrap-3.3.7.1` `pyyaml-5.1.1` `nltk-3.4.3` 
4. Run the application:
    - `python3 app.py`
5. Open a web browser and go to [http://localhost:5000](http://localhost:5000).

>Keep in mind that the project was developed at a hackathon in 24 hours. The priority was to get the MVP up and running, so -in benefit of time- some best practices may have not been followed. See [**Contributing**](README.md#Contributing) to learn how you could add your bit.

## Built with
Front-end:
- [Jinja](http://jinja.pocoo.org/) + [Bootstrap](https://getbootstrap.com/docs/3.3/).

Back-end:
- [Flask](http://flask.pocoo.org/) + [Python](https://docs.python.org/3/library/) + [Natural Language Toolkit (nltk)](https://www.nltk.org/).

## Contributing
Pull requests are welcomed. Feel free to add the functionalities you wish. There are so many things that could make this project better such as applying error handling, making it scalable to add more country legislations, providing a more deep _Opinions_ section, etc.

## Authors
- [Ioana Stoica](https://www.linkedin.com/in/ioanastoicadpd/).
- [Brnd Karlsboeck](https://www.linkedin.com/in/bernd-karlsboeck-5712895a/).
- [Josep Romero](https://www.linkedin.com/in/josepromero/).
- [Alex Costin](https://www.linkedin.com/in/alex-costin/).
- [Ignasi Oliver](https://ignasioliver.com).

## License
This project is under the [MIT License](LICENSE).
 
