# MY_CHOICES = (
#         ("News", _("News")),
#         ("Yangiliklar", _("Yangiliklar")),
#         ("Articles", _("Articles")),
#         ("Maqolalar", _("Maqolalar")),
#         ("CountryImage", _("Image of the Country")),
#         ("Mamlakat_Imiji", _("Mamlakat Imiji")),
#         ("Scientific_Articles", _("Scientific Articles")),
#         ("Ilmiy_Maqolalar", _("Ilmiy Maqolalar")),
#         ("Books", _("Books")),
#         ("Kitoblar", _("Kitoblar")),
#         ("International_Projects", _("International Projects")),
#         ("Xalqaro_Loyihalar", _("Xalqaro Loyihalar")),
#         ("Announcement", _("Announcement")),
#         ("Anons", _("Anons")),
#         ("Phd_Aftoreferati", _("Phd Aftoreferati")),
#         ("Phd_Aftoreferati", _("Phd Aftoreferati")),
#         ("Scientific_Research", _("Scientific Research")),
#         ("Ilmiy_tadqiqot", _("Ilmiy Tadqiqot")),
#         ("Magazines", _("Magazines")),
#         ("Jurnallar", _("Jurnallar")),
#         ("Foreign_Journals", _("Foreign Journals")),
#         "Xorijiy_jurnallar", _("Xorijiy jurnallar")),
#         ("Collections", _("Collections")),
#         ("Kolleksiyalar", _("Kolleksiyalar")),
#         ("Training", _("Training")),
#         ("Trening", _("Trening")),
#         ("Workshops", _("Workshops")),
#         ("Workshoplar", _("Workshoplar")),
#         ("Speeches", _("Speeches")),
#         ("Nutqlar", _("Nutqlar")),
#         ("Presentations", "Presentations")
#         ("Prezentatsiyalar", _("Prezentatsiyalar"))
#     )

def pair_language(lang):
    # if lang is 'en':
        news = "News" if lang == 'en' else "Yangiliklar"
        articles = "Articles" if lang == 'en' else "Maqolalar"
        countryimage = "CountryImage" if lang == 'en' else "Mamlakat_Imiji"
        scientific_articles = "Scientific_Articles" if lang == 'en' else "Ilmiy_Maqolalar"
        books = "Books" if lang == 'en' else "Kitoblar"
        international_projects = "International_Projects" if lang == 'en' else "Xalqaro_Loyihalar"
        announcement = "Announcement" if lang == 'en' else "Anons"
        phd_aftoreferat = "Phd_Aftoreferati" if lang == 'en' else "Phd_Aftoreferati"
        scientific_research="Scientific_Research" if lang == 'en' else "Ilmiy_tadqiqot"
        magazines = "Magazines" if lang == 'en' else "Jurnallar"
        foreign_journals = "Foreign_Journals" if lang == 'en' else "Xorijiy_jurnallar"
        collections = "Collections" if lang == 'en' else "Kolleksiyalar"
        training = "Training" if lang == 'en' else "Trening"
        workshops = "Workshops" if lang == 'en' else "Workshoplar"
        speeches = "Speeches" if lang == 'en' else "Nutqlar"
        presentation = "Presentations" if lang == 'en' else "Prezentatsiyalar"
        return [news, articles, countryimage, scientific_articles, books, international_projects]