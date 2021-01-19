
# Type: agent


person, group, organization or project that provides a piece of information (i.e. a knowledge association)

URI: [Alliance:Agent](http://alliancegenome.org/Agent)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Agent&#124;affiliation:uriorcurie%20*;address:string%20%3F;id:string;name:string%20%3F])

## Referenced by class


## Attributes


### Own

 * [address](address.md)  <sub>OPT</sub>
    * Description: the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * range: [String](types/String.md)
 * [affiliation](affiliation.md)  <sub>0..*</sub>
    * Description: a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [agent➞id](agent_id.md)  <sub>REQ</sub>
    * Description: Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.
    * range: [String](types/String.md)
 * [agent➞name](agent_name.md)  <sub>OPT</sub>
    * Description: it is recommended that an author's 'name' property be formatted as "surname, firstname initial."
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | group |
| **Exact Mappings:** | | prov:Agent |
|  | | dct:Agent |
|  | | biolink:Agent |
| **Narrow Mappings:** | | UMLSSG:ORGA |
|  | | UMLSSC:T092 |
|  | | UMLSST:orgt |
|  | | UMLSSC:T093 |
|  | | UMLSST:hcro |
|  | | UMLSSC:T094 |
|  | | UMLSST:pros |
|  | | UMLSSC:T095 |
|  | | UMLSST:shro |
|  | | UMLSSC:T096 |
|  | | UMLSST:grup |
|  | | UMLSSC:T097 |
|  | | UMLSST:prog |

