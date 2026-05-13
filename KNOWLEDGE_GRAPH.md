# Codex for Legal Practice Area Map

This map shows the public practice-area structure of `codex-for-legal`: 13 Codex legal plugins grouped by use case, with a short summary of what each plugin is for.

```mermaid
graph LR
  root["Codex for Legal"]

  subgraph transactional["Transactional / Business"]
    commercial["commercial-legal"]
    corporate["corporate-legal"]
    ip["ip-legal"]
  end

  subgraph advisory["Advisory / Governance"]
    privacy["privacy-legal"]
    product["product-legal"]
    employment["employment-legal"]
    regulatory["regulatory-legal"]
    ai["ai-governance-legal"]
  end

  subgraph disputes["Disputes / Research"]
    litigation["litigation-legal"]
    cocounsel["cocounsel-legal"]
  end

  subgraph education["Education / Clinic / Ops"]
    student["law-student"]
    clinic["legal-clinic"]
    builder["legal-builder-hub"]
  end

  commercial --> commercialSkills["Contract review, NDA, SaaS MSA, renewals"]
  corporate --> corporateSkills["M&A diligence, board minutes, entity compliance"]
  ip --> ipSkills["Clearance, FTO, OSS, takedowns, IP portfolio"]

  privacy --> privacySkills["PIA, DPA, DSAR, privacy gap analysis"]
  product --> productSkills["Launch review, marketing claims, feature risk"]
  employment --> employmentSkills["Hiring, termination, investigations, wage-hour"]
  regulatory --> regulatorySkills["Regulatory feeds, policy diff, comments, gaps"]
  ai --> aiSkills["AI inventory, AIA, vendor AI review"]

  litigation --> litigationSkills["Chronologies, claim charts, holds, subpoenas, briefs"]
  cocounsel --> cocounselSkills["Westlaw / Practical Law deep research"]

  student --> studentSkills["Case briefs, IRAC, outlines, bar prep"]
  clinic --> clinicSkills["Client intake, clinic memos, deadlines, handoffs"]
  builder --> builderSkills["Skill discovery, QA, registry, install workflow"]

  root --> transactional
  root --> advisory
  root --> disputes
  root --> education
```
