[![DOI](https://zenodo.org/badge/917653541.svg)](https://doi.org/10.5281/zenodo.16949040)

# Useful Data Science Resources
Papers and resources that have been particularly useful for health data science research (including stats, epidemiology, coding, etc.).  Of course, Stack Overflow and Stack Exchange are constantly open in one form or another.  The following links are additional references I've found particularly helpful over time.  

## Statistics
### General
* Frank Harrell's author checklist: https://discourse.datamethods.org/t/author-checklist/3407
* Frank Harrell's Biostatistics for Biomedical Research: https://hbiostat.org/bbr

### Probability
* A great visual introduction to probability: https://seeing-theory.brown.edu/

### Regression
* A great visual introduction to regression analysis: https://seeing-theory.brown.edu/regression-analysis/index.html
* Frank Harrell's Regression Modelling Strategies is invaluable: https://hbiostat.org/rmsc/
* An informative explanation showing how most of the common statistical models (e.g., t-test, correlation, chi-square, etc. are actually special cases of linear models (or very close approximations).  Jonas Kristoffer Lindeløv's post walks through the explanations with toy examples and code: https://lindeloev.github.io/tests-as-linear/

### Count data
* An entry-level text for guidance on modelling count data with examples in Stata, R and SAS, <ins>Modeling Count Data</ins> by Joseph M. Hilbe (DOI: https://doi.org/10.1017/CBO9781139236065)
  
### Time-to-event analysis
* A nice summary of frequently used measures of events (Table 3.3 https://archive.cdc.gov/#/details?url=https://www.cdc.gov/csels/dsepd/ss1978/lesson3/section2.html)
  
#### Survival analysis
* A helpful introduction to survival analysis with R code and examples: https://www.emilyzabor.com/tutorials/survival_analysis_in_r_tutorial.html#Part_1:_Introduction_to_Survival_Analysis
* Another tutorial: https://rpubs.com/alecri/258589
* A helpful guide for time-varying covariates with SAS and R code: https://www.jstatsoft.org/article/view/v061c01/v61c01.pdf
* A paper on good practice and pitfalls when presenting survival plots: https://www-sciencedirect-com.ezproxy1.lib.gla.ac.uk/science/article/pii/S014067360208594X?via%3Dihub

#### Multi-state analysis
* A helpful explanation of multi-state models for survival analysis: https://journals.sagepub.com/doi/10.1177/0962280208092301
* Multi-state visualisation: https://cran.r-project.org/web/packages/mstate/vignettes/visuals_demo.html

#### Competing risks
* A general introduction to competing risks: https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.115.017719?rfr_dat=cr_pub++0pubmed&url_ver=Z39.88-2003&rfr_id=ori%3Arid%3Acrossref.org 
* A well-written practical guide for reporting using the Fine-Gray model for competing risks; Fine, of the Fine-Gray model, is an author https://onlinelibrary.wiley.com/doi/10.1002/sim.7501
* A helpful explanation behind the subdistribution (Fine-Grey) and cause-specific survival functions: https://stats.stackexchange.com/questions/587504/subdistribution-cause-specific-survival-functions
* When to use cause-specific HR vs. Fine-Gray model? https://academic.oup.com/aje/article-abstract/170/2/244/111339
* R-specific resources:
  * A helpful R tutorial: https://rpubs.com/kaz_yos/cmprsk2
  * Easy subdistribution R package: https://mskcc-epi-bio.github.io/tidycmprsk/

### Splines 
* Review of spline options, handy for mathematical underpinnings: https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-019-0666-3
* A good comparison of splines vs. fractional polynomials: https://onlinelibrary.wiley.com/doi/full/10.1002/sim.5639
* A starter's guide on non-linear methods: https://bmjmedicine.bmj.com/content/2/1/e000396 

## Epidemiology
The gold standard textbook for epidemiology is <ins>Modern Epidemiology</ins> by Kenneth Rothman (https://www.wolterskluwer.com/en/solutions/ovid/modern-epidemiology-4634). Read <ins>Epidemiology: An Introroduction</ins> (https://global.oup.com/academic/product/epidemiology-9780197751541?cc=gb&lang=en&) by the same author for an overview. 

### Incidence & prevalence
* Prevalent cases in observational studies - https://pmc.ncbi.nlm.nih.gov/articles/PMC2695697/
* Calculating incidence rates and prevalence proportions - https://core.ac.uk/download/pdf/219687452.pdf
* Useful for explanation of incidence rate calculation using look-back periods (see supplementary materials Figure S1): https://www.ahajournals.org/doi/full/10.1161/CIRCULATIONAHA.118.034986#abstract

### Biases and fallacies
* Table 2 fallacy - should we present coefficients/RR/HR for confounders? https://academic.oup.com/aje/article/177/4/292/147738
* Overadjustment bias - should we adjust for everything? https://pmc.ncbi.nlm.nih.gov/articles/PMC2744485/
* Collider bias - how and why conditioning on a common effect (collider) could lead to spurious associations? https://www.bmj.com/content/381/bmj.p1135
* Selection bias - https://link.springer.com/article/10.1007/s40471-020-00241-6

## Electronic patient records
* Scotland-specific resources: https://github.com/jocelynfriday/EPRResources
* Systematic review of the different definitions of major adverse cardiovascular event definitions (MACE): https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-021-01440-5
* Kuan V. and Denaxas S et al. (the team behind the original CALIBER phenotypes)'s GitHub for machine-readable electronic health record phenotypes: https://github.com/HDRUK/chronological-map-phenotypes/tree/master
* Atlas of Longitudinal Datasets to find longitudinal data around the world: https://atlaslongitudinaldatasets.ac.uk/

## Data manipulation
* A helpful book with R code and examples for health data science in R: https://argoshare.is.ed.ac.uk/healthyr_book/
* A general data manipulation and visualisation using the tidyverse packages in R: https://r4ds.hadley.nz/
* A great introduction to doing data science in R based on the <tt>Tidyverse</tt> structure: https://r4ds.hadley.nz/

### General R packages
* Tidy data and data manipulation through <tt>Tidyverse</tt>: https://joss.theoj.org/papers/10.21105/joss.01686
* Creating presentation-ready summary tables through <tt>gtsummary</tt> : https://www.danieldsjoberg.com/gtsummary/
  * Splitting one variable (row) by another categorical variable (e.g., reporting haemoglobin levels by sex): https://forum.posit.co/t/summarizing-a-continuous-variables-by-two-categorical-variables-with-the-gtsummary-package/81937
* Visualising survival analysis and producing Kaplan-Meier curves and cumulative incidence analysis <tt>ggsurvfit</tt>: https://www.danieldsjoberg.com/ggsurvfit/
* When dealing with larger datasets, consider using using <tt>data.table</tt>: https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html
* Cheatsheets for R: https://www.usu.edu/math/amlc/files/r-studio-reference-sheets-compilation.pdf

## Data visualisation
* A great way to figure out how best to visualise your data with coded examples: https://www.data-to-viz.com/
* Interactive and easy data visualisation resource: https://app.flourish.studio/
* Tool for generating scientific images and illustrations: https://www.biorender.com/
* Edward Tufte is a master of data visualisation, called the "Leonardo da Vinci of data," by the <i>The New York Times</i>: https://www.edwardtufte.com/books/
* A colour blindness simulator for checking how illustrations and figures appear under different kinds of colour blindness: https://www.color-blindness.com/coblis-color-blindness-simulator/
* An alternative to an overcrowded Venn diagram: https://upset.app/

## General computational admin
* The Homebrew is the easy way to install packages on macOS (or Linux): https://brew.sh/

## Science communication
* A great article published in JAMA giving practical insights into how to communicate medical numbers to help guide decisions and improve communication of statistics: https://jamanetwork.com/journals/jama/fullarticle/2839303?utm_source=email&utm_campaign=content-shareicons&utm_content=article_engagement&utm_medium=social&utm_term=103125
  
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/jocelynfriday/UsefulDataSceinceResources">Useful Data Science Resources</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/jocelynfriday">Jocelyn M Friday</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
