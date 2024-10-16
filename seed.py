"""sample data for adoption page"""

from app import app
from models import db, Pet

with app.app_context():
    db.drop_all()
    db.create_all()

    spot = Pet(name="Spot", species='Dog', photo_url='https://cdn.britannica.com/47/236047-050-F06BFC5E/Dalmatian-dog.jpg', age=2)

    abby = Pet(name="Abby", species='Cat', age=6, available=False)

    floof = Pet(name="Floof", species='Cat', photo_url='https://moderncat.com/wp-content/uploads/2015/12/Himalayan.jpg', age=1)

    pumpkin = Pet(name="Pumpkin", species='Rabbit', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy9nqjvGR-looTCqidnsnDqA6tNcRjg_OkCw&s')

    tweetie = Pet(name="Tweetie", species='Bird', photo_url='https://s3-us-west-1.amazonaws.com/assets.wagwalkingweb.com/media/wellness_articles/body/1677693014.1539369/pet-bird-health-tips-and-info.png')

    bubba = Pet(name="Bubba", species='Dog', photo_url='https://cdn.britannica.com/83/236683-050-84785C8B/Boston-Terrier-dog.jpg', age=5)

    db.session.add_all([spot, abby, floof, pumpkin, tweetie, bubba])
    db.session.commit()