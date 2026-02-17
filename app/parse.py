from dataclasses import dataclass
import requests

URL = "https://mate.academy/"

@dataclass
class Course:
    name: str
    short_description: str
    duration: str


def get_all_courses() -> list[Course]:
    text = requests.get(URL).content
    # print(text)
    print("hello")



def main():
    get_all_courses()

if __name__ == "__main__":
    main()

#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > h3 > span
#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > p.typography_paragraphMedium__FWO7K.ProfessionCard_text___l0Du.ProfessionCard_description__K8weo
#div.ProfessionsListSectionTemplate_cardsWrapper__un6ny.ProfessionsListSectionTemplate_cardsWrapperShowAll__kWdCD > a:nth-child(2) > div.ProfessionCard_content__mPiVi > p.typography_paragraphMedium__FWO7K.ProfessionCard_text___l0Du.ProfessionCard_duration__13PwX