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

@app.route('/price_movement')
def price_movement():
    return render_template('price_movement.html', 
                            bg_img='b.jpg',
                            title_on_img='Price movement',
                            subheading_img='prediction using decision tree')

@app.route('/comparing_listening')
def comparing_listening():
    return render_template('comparing_listening.html', 
                            bg_img='b.jpg',
                            title_on_img='Comparing listening',
                            subheading_img='of music 2008 vs 2016')

@app.route('/lastfm_sqls')
def lastfm_sqls():
    return render_template('comparing_listening_sql.html', 
                            bg_img='b.jpg',
                            title_on_img='SQL for analysis',
                            subheading_img='Comparing listening of music: 2008 vs 2016')

@app.route('/hive_redshift_test')
def hive_vs_redshift():
    return render_template('hive_redshift_test.html', 
                            bg_img='b.jpg',
                            title_on_img='Hadoop/Hive vs. Redshift',
                            subheading_img='as ETL(ELT) tool')

@app.route('/hate_speech')
def hate_speech():
    return render_template('hate_speech.html', 
                            bg_img='b.jpg',
                            title_on_img='Recognition of hate speech',
                            subheading_img='in Facebook comments')


if __name__ == '__main__':
    app.run(debug=True)