# 3rd party
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', 
                            bg_img='home-bg.jpg',
                            title_on_img='Slawomir Tulski',
                            subheading_img='Big Data Engineer')

@app.route('/about')
def about():
    return render_template('about.html', 
                            bg_img='about-bg.jpg',
                            title_on_img='About Me',
                            subheading_img="If you'd like to know me better...")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html',
                           bg_img='contact-bg.jpg',
                           title_on_img='Contact Me',
                           subheading_img='If you have any question... Just ask.')

@app.route('/proxy_harvester')
def proxy_harvester():
    return render_template('proxy_harvester.html', 
                            bg_img='b.jpg',
                            title_on_img='Proxy Harvester',
                            subheading_img='')

@app.route('/creepy_scraper')
def creepy_scraper():
    return render_template('creepy_scraper.html', 
                            bg_img='b.jpg',
                            title_on_img='Creepy Scraper',
                            subheading_img='')

@app.route('/more_than')
def more_than():
    return render_template('more_than_parsing.html', 
                            bg_img='b.jpg',
                            title_on_img='Web Scraping',
                            subheading_img='more than just parsing HTML')

if __name__ == '__main__':
    app.run(debug=True)