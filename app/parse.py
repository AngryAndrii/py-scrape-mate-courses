from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup, Tag

URL = "https://mate.academy/"

@dataclass
class Course:
    name: str
    short_description: str
    duration: str


def parse_single_course(course: Tag) -> Course:
    print(dict(
        name=course.select_one("h3 span").text,
        short_description=course.select_one(".ProfessionCard_description__K8weo").text,
        duration=course.select_one(".ProfessionCard_duration__13PwX").text
    ))

def get_all_courses() -> list[Course]:
    text = requests.get(URL).content
    soup = BeautifulSoup(text, "html.parser")
    cards = soup.select(".ProfessionCard_content__mPiVi")
    return [parse_single_course(card) for card in cards]


def main():
    get_all_courses()

if __name__ == "__main__":
    main()

#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > h3 > span
#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > p.typography_paragraphMedium__FWO7K.ProfessionCard_text___l0Du.ProfessionCard_description__K8weo
#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > p.typography_paragraphMedium__FWO7K.ProfessionCard_text___l0Du.ProfessionCard_duration__13PwX