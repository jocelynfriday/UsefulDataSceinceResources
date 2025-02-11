# Useful Data Science Resources
Papers and resources that I've found to be particularly useful for health data science research (including stats, epidemiology, coding, etc.).  Of course, StackOverflow and StackExchange are constantly open in one form or fashion.  The following links are additional references I've found particularly helpful over time.  

## Statistics
### General
* Frank Harrell's author checklist: https://discourse.datamethods.org/t/author-checklist/3407

### Regression
* Frank Harrell's Regression Modeling Strategies is invaluable: https://hbiostat.org/rmsc/

#### Count data
* An entry-level text for guidance on modelling count data: (DOI: https://doi.org/10.1017/CBO9781139236065)
  
#### Time-to-event analysis
* A nice summary of frequently used measures of events (Table 3.3 https://archive.cdc.gov/#/details?url=https://www.cdc.gov/csels/dsepd/ss1978/lesson3/section2.html)
  
##### Survival Analysis
* A helpful introduction to survival analysis with R code and examples: https://www.emilyzabor.com/tutorials/survival_analysis_in_r_tutorial.html#Part_1:_Introduction_to_Survival_Analysis
* Another tutorial: https://rpubs.com/alecri/258589
* A helpful guide for time-varying covariates with SAS and R code: https://www.jstatsoft.org/article/view/v061c01/v61c01.pdf

##### Multistate analysis
* A helpful explanation of multi-state models for survival analysis: https://journals.sagepub.com/doi/10.1177/0962280208092301
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

### General R packages
* Tidy data and data manipulation through <tt>Tidyverse</tt>: https://joss.theoj.org/papers/10.21105/joss.01686
* Creating presentation-ready summary tables through <tt>gtsummary</tt> : https://www.danieldsjoberg.com/gtsummary/
* When dealing with larger datasets, consider using using <tt>data.table</tt>: https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html
* Cheatsheets for R: https://www.usu.edu/math/amlc/files/r-studio-reference-sheets-compilation.pdf

### Data visualisation
* A great way to figure out how best to visualise your data with coded examples: https://www.data-to-viz.com/
* Interactive and easy data visualisation resource: https://app.flourish.studio/

## General computational admin
* The Homebrew is the easy way to install packages on macOS (or Linux): https://brew.sh/

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/jocelynfriday/UsefulDataSceinceResources">Useful Data Science Resources</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/jocelynfriday">Jocelyn M Friday</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
