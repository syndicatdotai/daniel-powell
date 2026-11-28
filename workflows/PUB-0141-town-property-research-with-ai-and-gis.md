# Building a Town-Level Property Research Record with AI and GIS

I’ve been using AI to research properties in a town where I’m interested in purchasing land. The work goes beyond watching listings. I’m looking at parcels, ownership, development history, and the reasons some land has remained underused or stopped moving through development.

The aim is to build a comprehensive working picture of the town, with enough detail to understand which properties deserve a closer look and what questions still need answers.

## Starting with the map

Town GIS maps give the research a place to start. I use AI to help gather and organize parcel information, then connect it with the other material available about the property.

Google Maps provides another way to look at the surrounding area. QGIS brings higher-resolution aerial imagery and other geospatial information into the same research process. Comparing those views helps me examine the relationship between a parcel and the land around it.

A map can raise useful questions. An apparent access route, cleared area, or partly developed tract can become the starting point for a records search. The visual observation goes into the working record alongside the question it creates.

That connection matters. A property may look straightforward in one view, while its recorded history explains why it has been difficult to develop.

## Building a national imagery source inventory

I also used AI-assisted automation to research publicly accessible, high-quality aerial imagery across all 50 states. The resulting inventory records a direct source for each state, the available resolution, acquisition dates, coverage, and limitations. Where a high-resolution statewide source was unavailable, the record identifies a regional source or a lower-resolution fallback. It gives subsequent property research a starting point without repeating the entire source search.

That research feeds into the local land investigation. I can bring the appropriate imagery into QGIS and compare it with parcel boundaries, terrain, mapped wetlands, soils, and geology. The photographs show visible conditions, while lidar-derived elevation and the environmental and geological layers add context about slopes, drainage, possible ledge, and other features worth investigating before a site visit. Regional geology supplies context for questions about rock; site investigation establishes conditions such as depth to ledge. Connecticut makes these complementary layers available through its environmental mapping services. [CT ECO map and image services](https://maps.cteco.uconn.edu/map-services/)

## Comparing seasons and collection years

The inventory also records when the imagery was captured. Leaf-off imagery can reveal more of the ground beneath deciduous trees, while summer imagery shows vegetation under different conditions. Looking across collection years can help identify clearing, access changes, or construction activity. The available dates and seasonal views vary by location and source.

These are examples of the regional sources documented in the research:

| Area | Detail and seasonal coverage | Historical comparison and capture frequency |
|---|---|---|
| Connecticut | The 2023 statewide spring collection has 3-inch pixels, about 7.6 cm. Summer 2023 NAIP imagery provides a second seasonal view at 30 cm. | CT ECO also lists spring collections from 2016 and 2019. These provide snapshots separated by years; available seasonal layers and dates should be checked for the parcel. [CT imagery datasets](https://maps.cteco.uconn.edu/data/imagery/ct_imagery/) |
| Massachusetts, including Boston | The 2025 statewide spring, leaf-off imagery has 15 cm pixels. Cape Cod has a separate 7.5 cm product. | Spring collections from 2019, 2021, 2023, and 2025 provide recent comparisons at roughly two-year intervals. [2025 imagery](https://www.mass.gov/info-details/massgis-data-2025-aerial-imagery) and [imagery archive](https://www.mass.gov/info-details/massgis-data-layers) |
| New York | The source inventory records 6–12-inch orthoimagery, varying by area and collection. The state also lists partial summer coverage for some counties in 2025. | The state program aims for a four- to five-year statewide refresh cycle. Counties have multiple historical captures, with some areas photographed more frequently. [New York orthoimagery program](https://gis.ny.gov/orthoimagery) |
| Rhode Island | Public 3-inch photo collections include spring 2024, winter 2024–2025, and spring 2025. The spring 2025 capture ran from April into May. | These offer several closely spaced comparisons. The detailed photo products can mix foliage conditions and have variable horizontal accuracy because they are not traditionally orthorectified. [Spring 2024](https://rigis-edc.opendata.arcgis.com/datasets/2024-spring-rhode-island-digital-aerial-photographs/about), [winter 2024–2025](https://rigis-edc.opendata.arcgis.com/datasets/2024-2025-winter-rhode-island-digital-aerial-photographs/about), and [spring 2025 release](https://groups.google.com/a/uri.edu/g/rigis-group/c/_vgcY67yd8Q) |

Pixel size describes image detail. The capture date, positioning, and surrounding data determine what that detail can support. The source inventory keeps access and reuse terms with those technical details. MassGIS, for example, publishes its 2025 imagery with no use restrictions and requests acknowledgment for derived products. [MassGIS use terms](https://www.mass.gov/info-details/massgis-data-2025-aerial-imagery)

## Turning a map observation into a research question

The useful part is connecting an observation to something that can be investigated. For example, an older image might show clearing and a rough access route, while a later image shows little visible progress. That gives me a reason to look for the application, approval history, and subsequent records associated with that tract.

The photographs establish what is visible at the capture dates. The written records help explain what was proposed and what decisions followed. If a court case or ownership change appears in the same period, the next question is whether the documents actually connect it to the interrupted work. Several events occurring near each other in time can suggest a line of inquiry, but the connection still needs support.

The environmental layers help frame the physical questions. A possible access route may cross mapped wetland soils or steep terrain. A larger tract may contain only a limited area that appears practical to investigate for a particular use. Those observations help decide where to spend research time and what to examine on a site visit. Each layer has its own scale, age, and purpose, which need to stay attached to the interpretation.

## Following ownership through the records

Part of the research is identifying who owns the property, including the LLCs and individuals associated with it.

An ownership name is a starting point for tracing the parcel’s history. The work involves connecting the assessor information, land records, development applications, and other public documents to the correct property.

Names and descriptions can vary between sources. An older application may refer to a larger tract, while the current map shows several parcels. A company mentioned in a historical record may have transferred the property since then.

Keeping those relationships documented makes it easier to return to the same property without reconstructing the research each time.

## Investigating why development stopped

Some of the most interesting research starts with work that appears to have stalled. A development was proposed, construction began and paused, or a parcel remained underdeveloped while the surrounding area changed.

I use AI to help locate and work through planning records, meeting minutes, court material, and other documents that may explain what happened.

Lawsuits can be part of that history. They can reveal a dispute or a sequence of events that is difficult to understand from the parcel map alone. The research also needs to follow what happened afterward. A historical dispute may have been resolved, ownership may have changed, or a later decision may have altered the situation.

The same care applies to municipal records. Approval of a proposed sale, a completed transfer, a development approval, and the present condition of a property each answer a different question.

The working record preserves those distinctions so an old finding does not quietly become a claim about the property today.

## Building the history across separate records

A property’s history is often spread across documents created for different purposes. An assessor record may describe current ownership, a planning application may describe an earlier development proposal, and meeting minutes may record a decision affecting only part of that proposal.

The research needs to connect those documents to the same land even when the description changes. A parent tract may have been divided, a road may have acquired a name, or the applicant may differ from the recorded owner. That is where following parcel references and the sequence of records becomes useful.

The record also needs to carry the outcome of a finding. A lawsuit appearing in the history raises a question; a later settlement, released lien, transfer, or revised application may change what that question means today. Keeping both entries makes the history more useful than a list of search results.

## Keeping a useful record in Markdown

The information is stored in Markdown. Individual property notes hold the findings and source links, while an index and lead register help me compare the properties and keep track of the next checks.

The records bring together parcel references, ownership findings, development history, relevant proceedings, mapping observations, and unresolved questions. They also distinguish material checked against primary documents from older notes, secondary reporting, and ideas still being investigated.

That creates a lightweight research collection I can read directly and revisit with AI. A new document can be added to the property’s existing history, and a corrected finding can be carried into the next research pass.

This is especially useful when the work happens across separate sessions. The next session can start from the saved record and its open questions.

## Looking beyond the original development proposal

A parcel that could not support its original development plan may still be worth understanding.

The earlier proposal might explain why the property attracted attention, but it also gives the research a question to work through. What prevented that particular plan from moving forward, and what does that mean for a different use?

I’m looking for situations where the history points toward another opportunity worth investigating. That possibility stays attached to the supporting information and the checks it would require.

An underdeveloped parcel or an interrupted project does not by itself establish that land is available for sale or suitable for another purpose. Those questions remain part of the investigation.

## How this connects to open-source intelligence

The same structure has applications in open-source intelligence investigations. Public maps, aerial imagery, business registrations, land records, municipal proceedings, and court documents can be examined together to build a source-backed account of a property or development. A parcel gives the research a geographic anchor, while the documents help trace the organizations, proposals, transactions, and decisions associated with it. That could support property due diligence, a development-history investigation, or research prepared for a private investigator by identifying which connections deserve further examination.

The value comes from preserving how each connection was established. An LLC appearing on an assessor card, an applicant named in meeting minutes, and a party listed in a lawsuit each have a specific relationship to the record. AI can help organize those references and highlight questions across them, while the source documents support the conclusions. Aerial changes can help narrow a timeline, and conflicting records can identify a missing document worth seeking. The resulting Markdown collection gives a reviewer a route from an observation to its sources and unresolved questions.

## What AI contributes to the workflow

AI helps gather information across sources, organize it around individual properties, compare findings, and maintain the written context. The maps provide spatial context, and the public records provide the history behind what appears on the screen.

My construction and drafting experience helps shape the questions. The research process gives those questions a place to accumulate and develop.

The result is a growing town-level property record that connects what the land looks like, who owns it, what has been attempted, and what still needs to be established. It gives me a more informed starting point for deciding which properties and possible uses deserve further attention.

## Related work

- [Using LiDAR Terrain Maps Before the First Site Visit](PUB-0085-lidar-site-research.md) develops the terrain and access side of preliminary property research.
- [Preparing a Site-Planning Exhibit With AI and QGIS](../construction/PUB-0099-preparing-a-site-planning-exhibit-with-ai-and-qgis.md) describes combining historical mapping and project information into a planning document.
- [AI-Assisted Research and a Custom Dashboard for a Private Investigator](../research/PUB-0115-ai-assisted-research-dashboard-for-a-private-investigator.md) describes public-source collection, business-record research, and organizing findings for review.
