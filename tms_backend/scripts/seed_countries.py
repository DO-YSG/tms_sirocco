import pycountry
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.core.database import SessionLocal
from app.models import Country


def seed_countries():
    db = SessionLocal()
    try:
        existing = db.query(Country).count()
        if existing > 0:
            print(f"Countries already seeded ({existing} records). Skipping.")
            return

        countries = []
        for c in pycountry.countries:
            countries.append(Country(
                name=c.name,
                code=c.alpha_3
            ))

        db.bulk_save_objects(countries)
        db.commit()
        print(f"Successfully seeded {len(countries)} countries.")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_countries()