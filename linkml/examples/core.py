# Auto generated from core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-17 15:30
# Schema: Alliance-Schema-Prototype-Core-Types
#
# id: https://github.com/alliance-genome/agr_schemas/linkml
# description: Alliance Schema Prototype with LinkML
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
FB = CurieNamespace('FB', 'http://example.org/UNKNOWN/FB/')
GSID = CurieNamespace('GSID', 'http://example.org/UNKNOWN/GSID/')
MGI = CurieNamespace('MGI', 'http://example.org/UNKNOWN/MGI/')
ORCID = CurieNamespace('ORCID', 'http://example.org/UNKNOWN/ORCID/')
RGD = CurieNamespace('RGD', 'http://example.org/UNKNOWN/RGD/')
RESEARCHID = CurieNamespace('ResearchID', 'http://example.org/UNKNOWN/ResearchID/')
SGD = CurieNamespace('SGD', 'http://example.org/UNKNOWN/SGD/')
SCOPUSID = CurieNamespace('ScopusID', 'http://example.org/UNKNOWN/ScopusID/')
WB = CurieNamespace('WB', 'http://example.org/UNKNOWN/WB/')
ZFIN = CurieNamespace('ZFIN', 'http://example.org/UNKNOWN/ZFIN/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
ISBN = CurieNamespace('isbn', 'http://example.org/UNKNOWN/isbn/')
ISNI = CurieNamespace('isni', 'http://example.org/UNKNOWN/isni/')
DEFAULT_ = ALLIANCE


# Types

# Class references



@dataclass
class InformationContentEntity(YAMLRoot):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity
    class_class_curie: ClassVar[str] = "Alliance:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity

    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

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
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Agent

    id: str = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.affiliation is None:
            self.affiliation = []
        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation]
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.node_property = Slot(uri=ALLIANCE.node_property, name="node property", curie=ALLIANCE.curie('node_property'),
                   model_uri=ALLIANCE.node_property, domain=None, range=Optional[str])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.affiliation = Slot(uri=ALLIANCE.affiliation, name="affiliation", curie=ALLIANCE.curie('affiliation'),
                   model_uri=ALLIANCE.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=ALLIANCE.address, name="address", curie=ALLIANCE.curie('address'),
                   model_uri=ALLIANCE.address, domain=None, range=Optional[str])

slots.creation_date = Slot(uri=ALLIANCE.creation_date, name="creation date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=ALLIANCE.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=str)

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.information_content_entity_creation_date = Slot(uri=ALLIANCE.creation_date, name="information content entity_creation date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=ALLIANCE.information_content_entity_creation_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.agent_id = Slot(uri=ALLIANCE.id, name="agent_id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.agent_id, domain=Agent, range=str)

slots.agent_name = Slot(uri=ALLIANCE.name, name="agent_name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.agent_name, domain=Agent, range=Optional[str])
