from dataclasses import dataclass
from pathlib import Path
import sys

from dotenv import dotenv_values
import requests


@dataclass
class Asteroid:
    name: str
    asteroid_id: str
    url: str
    potentially_hazardous: bool

    def summary(self) -> str:
        hazard = "Yes" if self.potentially_hazardous else "No"
        return (
            f"Near-Earth asteroid: {self.name}\n"
            f"ID: {self.asteroid_id}\n"
            f"Potentially hazardous: {hazard}\n"
            f"NASA details: {self.url}"
        )


def main() -> int:
    env_path = Path(__file__).with_name(".env")
    api_key = dotenv_values(env_path).get("NASA_API_KEY")
    if not api_key:
        print(f"Error: set NASA_API_KEY in {env_path}.", file=sys.stderr)
        return 1

    try:
        response = requests.get(
            "https://api.nasa.gov/neo/rest/v1/neo/browse",
            params={"api_key": api_key, "size": 1},
            timeout=15,
        )
    except requests.RequestException:
        print("Error: could not connect to NASA's API.", file=sys.stderr)
        return 1

    if not response.ok:
        print(f"Error: NASA's API returned HTTP {response.status_code}.", file=sys.stderr)
        return 1

    try:
        data = response.json()
        item = data["near_earth_objects"][0]
        asteroid = Asteroid(
            name=item["name"],
            asteroid_id=item["id"],
            url=item["nasa_jpl_url"],
            potentially_hazardous=item["is_potentially_hazardous_asteroid"],
        )
        if not (
            all(isinstance(value, str) for value in (asteroid.name, asteroid.asteroid_id, asteroid.url))
            and isinstance(asteroid.potentially_hazardous, bool)
        ):
            raise ValueError("Unexpected field types")
    except (ValueError, KeyError, TypeError, IndexError):
        print("Error: NASA's API returned an unexpected JSON response.", file=sys.stderr)
        return 1

    print(asteroid.summary())
    return 0


if __name__ == "__main__":
    sys.exit(main())
