# MISP by BitHorn

**bh-misp (MISP by BitHorn)** includes integrations and developments made by the BitHorn group for the [MISP](https://www.misp-project.org/) platform. The project originated from the BitHorn members' need to experiment with, document, and integrate the MISP platform within enterprise and SOC environments. It is closely linked to [eg0n](https://github.com/b1th0rn/eg0n), which serves as the public web interface.

References:

* [eg0n](https://github.com/b1th0rn/eg0n)
* [MISP](https://www.misp-project.org/)
* [Telegram](https://t.me/+YsBHtJkvgNFmOGQ0)
* [Discord](https://discord.gg/Ys5AAbsyyH)
* [Support the project](https://www.patreon.com/roccosicilia)
* [Threat Intelligence automation series](https://www.patreon.com/posts/128063674)
* [MISP instance by BitHorn](https://misp.bithorn.org/)

## MISP

[MISP (Malware Information Sharing Platform)](https://www.misp-project.org/) is an open-source solution designed for the collection, storage, distribution, and sharing of cybersecurity indicators and threat intelligence, particularly in the context of incident response and malware analysis. MISP is tailored for incident responders, security analysts, ICT specialists, and malware reverse engineers, enabling them to carry out their daily operations more effectively and share structured information efficiently.

Initially launched in 2011 to provide structured management of Indicators of Compromise (IoCs), MISP has since evolved and is now used by [national CERTs and NATO](https://www.misp-project.org/who/), which contributed to the platform's name recognition. Today, MISP is also employed by organizations such as the [ACN](https://www.acn.gov.it/portale/w/cybersecurity-governance-fundamentals-la-valutazione-del-contesto-cyber-di-un-organizzazione) and other entities requiring structured IoC handling.

The [European Payments Council (EPC)](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2021-04/EPC098-21%20Request%20for%20Proposal%20EPC%20MISP%20instance%20service%20provider.pdf) has also adopted MISP to share timely information aimed at preventing and detecting fraudulent payment transactions. For further information, refer to the [CIPA note](https://www.cipa.it/attivita/iniziative/iniziative.pdf).

MISP supports threat intelligence operations through:

* Robust management of Indicators of Compromise (IoCs)
* A flexible and accurate [taxonomy system](https://www.misp-project.org/datamodels/#misp-taxonomies) based on tagging, enabling detailed data classification ([GitHub](https://github.com/MISP/misp-taxonomies/))
* Native support for a variety of [threat feeds](https://www.misp-project.org/feeds/)
* Extendability via [third-party tools and integrations](https://www.misp-project.org/tools/)
* Adoption of [open standards and data models](https://www.misp-project.org/datamodels/)

## BitHorn's MISP instance (WIP)

The BitHorn community is committed to promoting the adoption of MISP as a threat intelligence tool. Current regulatory trends emphasize collaboration among organizations for the structured sharing of IoCs. To support this, BitHorn provides a publicly accessible [MISP instance](https://misp.bithorn.org/) available to analysts. The instance supports multiple organizations and allows analysts to test and implement structured IoC management using MISP.

### Honeypots (WIP)

The BitHorn community aims to automate IoC ingestion processes as much as possible. A key initiative involves integrating honeypot systems with MISP, enabling automatic submission of malicious activity detected by the honeypots to the [MISP instance](https://misp.bithorn.org/).

Honeypots are expected to log malicious activities using the [Elastic Common Schema (ECS)](https://www.elastic.co/docs/reference/ecs). The logs will be processed and ingested into MISP via a dedicated batch process.

### Email Analysis (WIP)

To support the ingestion of IoCs from as many sources as possible, a batch process is under development for analyzing emails flagged as malicious. A designated email inbox will be configured to receive malicious emails as attachments. The batch will analyze these attachments and automatically insert the resulting IoCs into the [MISP instance](https://misp.bithorn.org/).

### Privacy

Since IoCs may include personal data, careful consideration must be given to the impact of sharing such data with the BitHorn community and other connected MISP instances.

## eg0n (WIP)

The native MISP interface is not optimized for public access. The BitHorn community aims to make collected IoCs publicly accessible. [eg0n](https://github.com/b1th0rn/eg0n) is the platform responsible for extracting IoCs from MISP, validating their quality and relevance, and publishing them as publicly accessible threat feeds.
