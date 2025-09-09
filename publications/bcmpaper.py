from pyalex import Works
from pyalex import config

config.email = "natapol.p@chula.ac.th"

class Paper(dict):

    def __init__(self, work: dict):
        super().__init__(dict(work))

    def id(self) -> str:
        return self["id"]

    def doi(self) -> str:
        return self["doi"]
    
    def title(self) -> str:
        return self["title"]
    
    def publication_year(self) -> str:
        return self["publication_year"]
    
    def publication_date(self) -> str:
        return self["publication_date"]
    
    def type(self) -> str:
        return self["type"]
    
    def type_crossref(self) -> str:
        return self["type_crossref"]
    
    def indexed_in(self) -> tuple:
        return self["indexed_in"]
    
    def countries_distinct_count(self) -> int:
        return self["countries_distinct_count"]
    
    def institutions_distinct_count(self) -> int:
        return self["institutions_distinct_count"]
    
    def apc_list(self) -> dict:
        return self["apc_list"]
    
    def apc_paid(self) -> dict:
        return self["apc_paid"]
    
    def fwci(self) -> float:
        return self["fwci"]
    
    def has_fulltext(self) -> bool:
        return self["has_fulltext"]
    
    def fulltext_origin(self) -> str:
        return self["fulltext_origin"]
    
    def cited_by_count(self) -> int:
        return self["cited_by_count"]
    
    def citation_normalized_percentile(self) -> dict:
        return self["citation_normalized_percentile"]
    
    def cited_by_percentile_year(self) -> dict:
        return self["cited_by_percentile_year"]

    def biblio(self) -> dict:
        return self["biblio"]
    
    def biblio_volume(self) -> str:
        return self["biblio"]["volume"]
    
    def biblio_issue(self) -> str:
        return self["biblio"]["issue"]
    
    def biblio_pages(self) -> tuple:
        return (str(self["biblio"]["first_page"]), str(self["biblio"]["last_page"]))
    
    def is_retracted(self) -> bool:
        return self["is_retracted"]
    
    def is_paratext(self) -> bool:
        return self["is_paratext"]
    
    def primary_topic(self) -> dict:
        return self["primary_topic"]
    
    def topics(self) -> dict:
        return self["topics"]
    
    def keywords(self) -> dict:
        return self["keywords"]
    
    def concepts(self) -> dict:
        return self["concepts"]
    
    def locations_count(self) -> int:
        return self["locations_count"]

    def locations(self) -> tuple:
        return self["locations"]
    
    def best_oa_location(self) -> tuple:
        return self["best_oa_location"]
    
    def referenced_works_count(self) -> int:
        return self["referenced_works_count"]
    
    def referenced_works(self) -> tuple:
        return self["referenced_works"]
    
    def related_works(self) -> tuple:
        return self["related_works"]
    
    def abstract_inverted_index(self) -> dict:
        return self["abstract_inverted_index"]
    
    def cited_by_api_url(self) -> str:
        return self["cited_by_api_url"]
    
    def cited_counts_by_year(self) -> dict:
        return self["counts_by_year"]

    def updated_date(self) -> str:
        return self["updated_date"]

    def created_date(self) -> str:
        return self["created_date"]
    
    def sustainable_development_goals(self) -> list:
        return self["sustainable_development_goals"]
    
    # authorships
    
    def authors(self) -> tuple:
        return tuple([name["author"]["display_name"] for name in self["authorships"]])
    
    def author_ids(self) -> dict:
        pair = {}
        for name in self["authorships"]:
            pair[name["author"]["id"]] = name["author"]["display_name"]
        return pair
    
    def institutions(self) -> tuple:
        return tuple([(inst["display_name"] for inst in name["institutions"]) for name in self["authorships"]])
    
    def institution_ids(self) -> dict:
        ids = []
        for name in self["authorships"]:
            pair = {}
            for ints in name["institutions"]:
                pair[ints["id"]] = ints["display_name"]
            ids.append(pair)
        return ids
    
    def affiliations(self) -> tuple:
        return (name["affiliations"] for name in self["authorships"])

    # primary location
    def is_oa(self) -> bool:
        return self["primary_location"]["is_oa"] if "is_oa" in self["primary_location"] else None
    
    def landing_page_url(self) -> str:
        return self["primary_location"]["landing_page_url"]
    
    def pdf_url(self) -> str:
        return self["primary_location"]["pdf_url"]
    
    def license(self) -> str:
        return str(self["primary_location"]["license"])
    
    def is_accepted(self) -> bool:
        return self["primary_location"]["is_accepted"]
    
    def is_published(self) -> bool:
        return self["primary_location"]["is_published"]
    
    # source

    def source(self) -> dict:
        if "source" in self["primary_location"]:
            return self["primary_location"]["source"]
        else:
            return {}
    
    def source_id(self) -> str:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["id"]
        else:
            return ""
    
    def source_display_name(self) -> str:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["display_name"]
        else:
            return ""
    
    def source_issn_l(self) -> str:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["issn_l"]
        else:
            return ""
    
    def source_issn(self) -> tuple:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["issn"]
        else:
            return tuple()
    
    def source_type(self) -> str:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["type"]
        else:
            return ""
    
    def source_host_organization_name(self) -> str:
        if "source" in self["primary_location"] and self["primary_location"]["source"]:
            return self["primary_location"]["source"]["host_organization_name"]
        else:
            return ""
    
    def create_quarto(self):
        biblio = {}
        biblio['id'] = self.id()
        biblio['type'] = self.type_crossref()
        biblio['container_title'] = self.source_display_name()
        biblio['DOI'] = self.doi()
        biblio['ISSN'] = self.source_issn_l()
        biblio['issue'] = self.biblio()["issue"]
        biblio['license'] = self.license()
        biblio['note'] = self.source_host_organization_name()
        biblio['page'] = " - ".join(self.biblio_pages())
        biblio['title'] = self.title()
        biblio['URL'] = self.landing_page_url()
        biblio['volume'] = self.biblio_volume()
        biblio['author'] = list(self.authors())
        biblio['year'] = self.publication_year()
        biblio['issued'] = {
            "date-parts": self.publication_date()
        }

        return biblio
    
    

    
import yaml
from pathlib import Path 

alexid = [
    "A5064401818", # NP
    "A5003745838", # WA
    "A5008542098", # PL
    "A5005440015", # PT
]

works = Works() \
    .filter(
        author={
            "id": "|".join(alexid)
        }
    ) \
    .filter(
        from_publication_date = "1990-01-01"
    ) \
    .get()


for work in works:
    paper = Paper(work)

    id = paper.id().split('/')[-1]
    data = paper.create_quarto()
    data["categories"] = []

    Path(f"web/{id}").mkdir(parents=True, exist_ok=True)
    

    with open(f"web/{id}/{id}.qmd", "w") as file:
        yaml_string=yaml.dump(data)
        file.write("---\n")
        file.write(yaml_string)
        file.write("---")
