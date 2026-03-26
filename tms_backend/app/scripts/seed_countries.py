import pycountry

from app.core.database import SessionLocal
from app.models import Country


def seed_countries():
    db = SessionLocal()
    try:
        existing = db.query(Country).count()
        if existing > 0:
            print(f"Countries already seeded ({existing} records). Skipping.")
            return

        countries = [
            Country(name=c.name, code=c.alpha_3)
            for c in pycountry.countries
        ]

        db.add_all(countries)
        db.commit()
        print(f"Successfully seeded {len(countries)} countries.")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_countries()