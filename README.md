# Useful Data Science Resources
Papers and resources that I've found to be particularly useful for health data science research (including stats, epidemiology, coding, etc.).  Of course, StackOverflow and StackExchange are constantly open in one form or fashion.  The following links are additional references I've found particularly helpful over time.  

## Statistics
### General
* Frank Harrell's author checklist: https://discourse.datamethods.org/t/author-checklist/3407

### Regression
* Frank Harrell's Regression Modeling Strategies is invaluable: https://hbiostat.org/rmsc/
#### Time-to-event analysis

##### Survival Analysis
* A useful introduction to survival analysis with R code and examples: https://www.emilyzabor.com/tutorials/survival_analysis_in_r_tutorial.html#Part_1:_Introduction_to_Survival_Analysis

##### Multistate analysis
* Multi-state visualisation: https://cran.r-project.org/web/packages/mstate/vignettes/visuals_demo.html

##### Competing Risks
* A well-written practical guide for reporting using the Fine-Grey model for competing risks; Fine of Fine and Gray is an author https://onlinelibrary.wiley.com/doi/10.1002/sim.7501
* A helpful explanation behind the subdistribution (Fine-Grey) and cause-specific survival functions: https://stats.stackexchange.com/questions/587504/subdistribution-cause-specific-survival-functions
* R specific resources:
  * A useful R tutorial: https://rpubs.com/kaz_yos/cmprsk2
  * Easy subdistribution R package: https://mskcc-epi-bio.github.io/tidycmprsk/


### Splines 
* Review of spline options, handy for mathematical underpinnings: https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-019-0666-3

## Epidemiology

### Incidence & Prevalence
* Prevalent cases in observational studies -  https://pmc.ncbi.nlm.nih.gov/articles/PMC2695697/
* Calculating incidence rates and prevalence proportions - https://core.ac.uk/download/pdf/219687452.pdf
* Useful for explanation of incidence rate calculation using look-back periods (see supplementary materials Figure S1): https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.118.034986#abstract

## Electronic patient records
* Scotland-specific resources: https://github.com/jocelynfriday/EPRResources
* Systematic review of the different definitions of major adverse cardiovascular event definitions (MACE): https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-021-01440-5
* Kuan V. and Denaxas S et al. (the team behind the original CALIBER phenotypes)'s GitHub for machine-readable electronic health record phenotypes: https://github.com/HDRUK/chronological-map-phenotypes/tree/master

## Data manipulation
* A helpful book with R code and examples for health data science in R: https://argoshare.is.ed.ac.uk/healthyr_book/

### Data visualisation
* A great way to figure out how best to visualise your data with coded examples: https://www.data-to-viz.com/

## General computational admin
* The Homebrew is the easy way to install packages on macOS (or Linux): https://brew.sh/
