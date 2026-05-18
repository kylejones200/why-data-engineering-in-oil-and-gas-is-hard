# Why Data Engineering in Oil and Gas is Hard

Published: 2025-06-27
Medium: [https://medium.com/@kyle-t-jones/why-data-engineering-in-oil-and-gas-is-hard-c22478fd5e67](https://medium.com/@kyle-t-jones/why-data-engineering-in-oil-and-gas-is-hard-c22478fd5e67)

## Business context

Data engineering in oil and gas is difficult because core operational systems were never built to speak the same language. Each domain --- drilling, completions, production, land, maintenance --- adopted its own tools, its own schemas, and its own logic. The problems are not abstract. They show up in specific ways that make even basic analysis unreliable until they are addressed.

Start with identity. There is no universal well ID. A single horizontal well might be recorded in a drilling database as `OK-031N-066W-1423H`, while the SCADA historian logs it as `0310661423H`, and the SAP maintenance system calls it `WELL-1423`. In completions spreadsheets, it might show up as `1423-H`, and in production records, as `Well_1423_1L`. None of these names match directly. API numbers help, but even they can be formatted differently---with or without dashes, with extra digits, or truncated to county-level identifiers. Without a curated mapping table or fuzzy join logic, it becomes impossible to correlate events across domains. You may think you're analyzing a single well, when in fact the data reflects two or three.

Time introduces another layer of inconsistency. Consider the spud date. The drilling contractor may log the date they first moved the rig onto location. The operator's report might list the day the bit hit surface. In WITSML files, the same well could show a `spudDate` tied to the start of intermediate casing. Regulatory filings, often submitted weeks later, may use the permit date instead. A completion engineer looking at fiber data might interpret "start of well" as the beginning of stage pumping. In one North Dakota dataset, the spud date differed by as much as 19 days depending on the source. This breaks longitudinal modeling---especially when trying to align production with drilling and completions activity.

## About

Place the code for this article in this repository.
The original article export is saved as `article.md`.

## Files

Add your `.ipynb`, `.py`, `.yaml`, `.js`, `.ts`, or other project files here.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).