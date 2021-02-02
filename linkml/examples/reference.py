# Auto generated from reference.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-20 09:23
# Schema: reference
#
# id: https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
import parse
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import URIorCURIE, XSDDate
from includes.types import Date, String, Uriorcurie

metamodel_version = "1.6.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('Alliance', 'http://alliancegenome.org/')
DOI = CurieNamespace('DOI', 'http://example.org/UNKNOWN/DOI/')
FB = CurieNamespace('FB', 'https://flybase.org')
MGI = CurieNamespace('MGI', 'http://www.informatics.jax.org/')
NLMID = CurieNamespace('NLMID', 'http://example.org/UNKNOWN/NLMID/')
ORCID = CurieNamespace('ORCID', 'http://example.org/UNKNOWN/ORCID/')
PMID = CurieNamespace('PMID', 'http://example.org/UNKNOWN/PMID/')
RGD = CurieNamespace('RGD', 'https://rgd.mcw.edu/')
SGD = CurieNamespace('SGD', 'http://www.yeastgenome.org/')
WB = CurieNamespace('WB', 'https://www.wormbase.org/')
ZFIN = CurieNamespace('ZFIN', 'https://zfin.org/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
ISBN = CurieNamespace('isbn', 'http://example.org/UNKNOWN/isbn/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/')


# Types

# Class references
class MeshTermId(URIorCURIE):
    pass


class ReferenceId(URIorCURIE):
    pass


class AgentId(URIorCURIE):
    pass


@dataclass
class MeshTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/MeshTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "mesh term"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/MeshTerm")

    id: Union[str, MeshTermId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, MeshTermId):
            self.id = MeshTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Tag(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/Tag")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "tag"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/Tag")

    name: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Reference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/Reference")

    id: Union[str, ReferenceId] = None
    title: Optional[str] = None
    date_published: Optional[Union[str, XSDDate]] = None
    arrived_in_pubmed: Optional[Union[str, XSDDate]] = None
    last_modified: Optional[Union[str, XSDDate]] = None
    volume: Optional[str] = None
    pages: Optional[str] = None
    abstract: Optional[str] = None
    citation: Optional[str] = None
    issue_name: Optional[str] = None
    issue_date: Optional[Union[str, XSDDate]] = None
    alliance_category: Optional[str] = None
    has_mod_reference_type: Optional[Union[str, List[str]]] = empty_list()
    has_author: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    has_tag: Optional[Union[str, List[str]]] = empty_list()
    has_mesh_term: Optional[Union[Union[str, MeshTermId], List[Union[str, MeshTermId]]]] = empty_list()
    has_cross_reference: Optional[Union[str, List[str]]] = empty_list()
    has_publisher: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    resource_abbreviation: Optional[str] = None
    date_published: Optional[str] = None
    arrived_in_PubMed: Optional[str] = None
    last_modified: Optional[str] = None
    issue_date: Optional[str] = None
    alliance_category: Optional[str] = None
    publisher: Optional[str] = None
    resource_abbreviation: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ReferenceId):
            self.id = ReferenceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.date_published is not None and not isinstance(self.date_published, XSDDate):
            self.date_published = XSDDate(self.date_published)

        if self.arrived_in_pubmed is not None and not isinstance(self.arrived_in_pubmed, XSDDate):
            self.arrived_in_pubmed = XSDDate(self.arrived_in_pubmed)

        if self.last_modified is not None and not isinstance(self.last_modified, XSDDate):
            self.last_modified = XSDDate(self.last_modified)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.pages is not None and not isinstance(self.pages, str):
            self.pages = str(self.pages)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.issue_name is not None and not isinstance(self.issue_name, str):
            self.issue_name = str(self.issue_name)

        if self.issue_date is not None and not isinstance(self.issue_date, XSDDate):
            self.issue_date = XSDDate(self.issue_date)

        if self.alliance_category is not None and not isinstance(self.alliance_category, str):
            self.alliance_category = str(self.alliance_category)

        if self.has_mod_reference_type is None:
            self.has_mod_reference_type = []
        if not isinstance(self.has_mod_reference_type, list):
            self.has_mod_reference_type = [self.has_mod_reference_type]
        self.has_mod_reference_type = [v if isinstance(v, str) else str(v) for v in self.has_mod_reference_type]

        if self.has_author is None:
            self.has_author = []
        if not isinstance(self.has_author, list):
            self.has_author = [self.has_author]
        self.has_author = [v if isinstance(v, AgentId) else AgentId(v) for v in self.has_author]

        if self.has_tag is None:
            self.has_tag = []
        if not isinstance(self.has_tag, list):
            self.has_tag = [self.has_tag]
        self.has_tag = [v if isinstance(v, str) else str(v) for v in self.has_tag]

        if self.has_mesh_term is None:
            self.has_mesh_term = []
        if not isinstance(self.has_mesh_term, list):
            self.has_mesh_term = [self.has_mesh_term]
        self.has_mesh_term = [v if isinstance(v, MeshTermId) else MeshTermId(v) for v in self.has_mesh_term]

        if self.has_cross_reference is None:
            self.has_cross_reference = []
        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference]
        self.has_cross_reference = [v if isinstance(v, str) else str(v) for v in self.has_cross_reference]

        if self.has_publisher is None:
            self.has_publisher = []
        if not isinstance(self.has_publisher, list):
            self.has_publisher = [self.has_publisher]
        self.has_publisher = [v if isinstance(v, AgentId) else AgentId(v) for v in self.has_publisher]

        if self.resource_abbreviation is not None and not isinstance(self.resource_abbreviation, str):
            self.resource_abbreviation = str(self.resource_abbreviation)

        if self.date_published is not None and not isinstance(self.date_published, str):
            self.date_published = str(self.date_published)

        if self.arrived_in_PubMed is not None and not isinstance(self.arrived_in_PubMed, str):
            self.arrived_in_PubMed = str(self.arrived_in_PubMed)

        if self.last_modified is not None and not isinstance(self.last_modified, str):
            self.last_modified = str(self.last_modified)

        if self.issue_date is not None and not isinstance(self.issue_date, str):
            self.issue_date = str(self.issue_date)

        if self.alliance_category is not None and not isinstance(self.alliance_category, str):
            self.alliance_category = str(self.alliance_category)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.resource_abbreviation is not None and not isinstance(self.resource_abbreviation, str):
            self.resource_abbreviation = str(self.resource_abbreviation)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Agent
    class_class_curie: ClassVar[str] = "Alliance:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_schemas/linkml/reference.yaml/Agent")

    id: Union[str, AgentId] = None
    name: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=URIRef)

slots.date_published = Slot(uri=DEFAULT_.date_published, name="date_published", curie=DEFAULT_.curie('date_published'),
                   model_uri=DEFAULT_.date_published, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.has_mod_reference_type = Slot(uri=DEFAULT_.has_mod_reference_type, name="has_mod_reference_type", curie=DEFAULT_.curie('has_mod_reference_type'),
                   model_uri=DEFAULT_.has_mod_reference_type, domain=None, range=Optional[Union[str, List[str]]])

slots.has_tag = Slot(uri=DEFAULT_.has_tag, name="has_tag", curie=DEFAULT_.curie('has_tag'),
                   model_uri=DEFAULT_.has_tag, domain=None, range=Optional[Union[str, List[str]]])

slots.arrived_in_pubmed = Slot(uri=DEFAULT_.arrived_in_pubmed, name="arrived_in_pubmed", curie=DEFAULT_.curie('arrived_in_pubmed'),
                   model_uri=DEFAULT_.arrived_in_pubmed, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.has_cross_reference = Slot(uri=DEFAULT_.has_cross_reference, name="has_cross_reference", curie=DEFAULT_.curie('has_cross_reference'),
                   model_uri=DEFAULT_.has_cross_reference, domain=Reference, range=Optional[Union[str, List[str]]])

slots.resource_abbreviation = Slot(uri=DEFAULT_.resource_abbreviation, name="resource_abbreviation", curie=DEFAULT_.curie('resource_abbreviation'),
                   model_uri=DEFAULT_.resource_abbreviation, domain=Reference, range=Optional[str])

slots.issue_date = Slot(uri=DEFAULT_.issue_date, name="issue_date", curie=DEFAULT_.curie('issue_date'),
                   model_uri=DEFAULT_.issue_date, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.last_modified = Slot(uri=DEFAULT_.last_modified, name="last_modified", curie=DEFAULT_.curie('last_modified'),
                   model_uri=DEFAULT_.last_modified, domain=Reference, range=Optional[Union[str, XSDDate]])

slots.title = Slot(uri=DEFAULT_.title, name="title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.title, domain=Reference, range=Optional[str])

slots.volume = Slot(uri=DEFAULT_.volume, name="volume", curie=DEFAULT_.curie('volume'),
                   model_uri=DEFAULT_.volume, domain=Reference, range=Optional[str])

slots.pages = Slot(uri=DEFAULT_.pages, name="pages", curie=DEFAULT_.curie('pages'),
                   model_uri=DEFAULT_.pages, domain=Reference, range=Optional[str])

slots.abstract = Slot(uri=DEFAULT_.abstract, name="abstract", curie=DEFAULT_.curie('abstract'),
                   model_uri=DEFAULT_.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri=DEFAULT_.citation, name="citation", curie=DEFAULT_.curie('citation'),
                   model_uri=DEFAULT_.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri=DEFAULT_.issue_name, name="issue_name", curie=DEFAULT_.curie('issue_name'),
                   model_uri=DEFAULT_.issue_name, domain=Reference, range=Optional[str])

slots.alliance_category = Slot(uri=DEFAULT_.alliance_category, name="alliance_category", curie=DEFAULT_.curie('alliance_category'),
                   model_uri=DEFAULT_.alliance_category, domain=Reference, range=Optional[str])

slots.has_mesh_term = Slot(uri=DEFAULT_.has_mesh_term, name="has_mesh_term", curie=DEFAULT_.curie('has_mesh_term'),
                   model_uri=DEFAULT_.has_mesh_term, domain=Reference, range=Optional[Union[Union[str, MeshTermId], List[Union[str, MeshTermId]]]])

slots.has_keyword = Slot(uri=DEFAULT_.has_keyword, name="has_keyword", curie=DEFAULT_.curie('has_keyword'),
                   model_uri=DEFAULT_.has_keyword, domain=Reference, range=Optional[Union[str, List[str]]])

slots.has_author = Slot(uri=DEFAULT_.has_author, name="has_author", curie=DEFAULT_.curie('has_author'),
                   model_uri=DEFAULT_.has_author, domain=Reference, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_publisher = Slot(uri=DEFAULT_.has_publisher, name="has_publisher", curie=DEFAULT_.curie('has_publisher'),
                   model_uri=DEFAULT_.has_publisher, domain=Reference, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=Optional[str])

slots.date_published = Slot(uri=DEFAULT_.date_published, name="date published", curie=DEFAULT_.curie('date_published'),
                   model_uri=DEFAULT_.date_published, domain=None, range=Optional[str])

slots.arrived_in_PubMed = Slot(uri=DEFAULT_.arrived_in_PubMed, name="arrived in PubMed", curie=DEFAULT_.curie('arrived_in_PubMed'),
                   model_uri=DEFAULT_.arrived_in_PubMed, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=DEFAULT_.last_modified, name="last modified", curie=DEFAULT_.curie('last_modified'),
                   model_uri=DEFAULT_.last_modified, domain=None, range=Optional[str])

slots.issue_date = Slot(uri=DEFAULT_.issue_date, name="issue date", curie=DEFAULT_.curie('issue_date'),
                   model_uri=DEFAULT_.issue_date, domain=None, range=Optional[str])

slots.alliance_category = Slot(uri=DEFAULT_.alliance_category, name="alliance category", curie=DEFAULT_.curie('alliance_category'),
                   model_uri=DEFAULT_.alliance_category, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DEFAULT_.publisher, name="publisher", curie=DEFAULT_.curie('publisher'),
                   model_uri=DEFAULT_.publisher, domain=None, range=Optional[str])

slots.resource_abbreviation = Slot(uri=DEFAULT_.resource_abbreviation, name="resource abbreviation", curie=DEFAULT_.curie('resource_abbreviation'),
                   model_uri=DEFAULT_.resource_abbreviation, domain=None, range=Optional[str])

slots.reference_id = Slot(uri=DEFAULT_.id, name="reference_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.reference_id, domain=Reference, range=Union[str, ReferenceId])

slots.reference_title = Slot(uri=DEFAULT_.title, name="reference_title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.reference_title, domain=Reference, range=Optional[str])

slots.reference_date_published = Slot(uri=DEFAULT_.date_published, name="reference_date published", curie=DEFAULT_.curie('date_published'),
                   model_uri=DEFAULT_.reference_date_published, domain=Reference, range=Optional[str])

slots.reference_arrived_in_PubMed = Slot(uri=DEFAULT_.arrived_in_PubMed, name="reference_arrived in PubMed", curie=DEFAULT_.curie('arrived_in_PubMed'),
                   model_uri=DEFAULT_.reference_arrived_in_PubMed, domain=Reference, range=Optional[str])

slots.reference_last_modified = Slot(uri=DEFAULT_.last_modified, name="reference_last modified", curie=DEFAULT_.curie('last_modified'),
                   model_uri=DEFAULT_.reference_last_modified, domain=Reference, range=Optional[str])

slots.reference_volume = Slot(uri=DEFAULT_.volume, name="reference_volume", curie=DEFAULT_.curie('volume'),
                   model_uri=DEFAULT_.reference_volume, domain=Reference, range=Optional[str])

slots.reference_pages = Slot(uri=DEFAULT_.pages, name="reference_pages", curie=DEFAULT_.curie('pages'),
                   model_uri=DEFAULT_.reference_pages, domain=Reference, range=Optional[str])

slots.reference_citation = Slot(uri=DEFAULT_.citation, name="reference_citation", curie=DEFAULT_.curie('citation'),
                   model_uri=DEFAULT_.reference_citation, domain=Reference, range=Optional[str])

slots.reference_abstract = Slot(uri=DEFAULT_.abstract, name="reference_abstract", curie=DEFAULT_.curie('abstract'),
                   model_uri=DEFAULT_.reference_abstract, domain=Reference, range=Optional[str])

slots.reference_issue_date = Slot(uri=DEFAULT_.issue_date, name="reference_issue date", curie=DEFAULT_.curie('issue_date'),
                   model_uri=DEFAULT_.reference_issue_date, domain=Reference, range=Optional[str])

slots.reference_alliance_category = Slot(uri=DEFAULT_.alliance_category, name="reference_alliance category", curie=DEFAULT_.curie('alliance_category'),
                   model_uri=DEFAULT_.reference_alliance_category, domain=Reference, range=Optional[str])

slots.reference_publisher = Slot(uri=DEFAULT_.publisher, name="reference_publisher", curie=DEFAULT_.curie('publisher'),
                   model_uri=DEFAULT_.reference_publisher, domain=Reference, range=Optional[str])

slots.reference_resource_abbreviation = Slot(uri=DEFAULT_.resource_abbreviation, name="reference_resource abbreviation", curie=DEFAULT_.curie('resource_abbreviation'),
                   model_uri=DEFAULT_.reference_resource_abbreviation, domain=Reference, range=Optional[str])

slots.agent_id = Slot(uri=DEFAULT_.id, name="agent_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.agent_id, domain=Agent, range=Union[str, AgentId])

slots.agent_name = Slot(uri=DEFAULT_.name, name="agent_name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.agent_name, domain=Agent, range=Optional[str])
