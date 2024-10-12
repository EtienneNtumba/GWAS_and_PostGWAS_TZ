# **GWAS and Post-GWAS Analysis for Malaria Resistance in Tanzanian Population**

### **Authors**:  
**Etienne Ntumba Kabongo**

---

## **Introduction**

Malaria remains a significant public health issue in Tanzania and other regions in Sub-Saharan Africa. Understanding the genetic factors influencing malaria susceptibility is crucial for developing effective treatments and public health strategies. This project focuses on conducting a Genome-Wide Association Study (GWAS) using Tanzanian population data to identify genetic variants associated with malaria resistance. The study integrates traditional GWAS methods with advanced AI-driven approaches, enhancing the detection of complex interactions, epistasis, and rare variants.

---

## **Methodology**

### **a. Data Collection and Preparation**

- **Genotype Data**: Blood samples were collected from malaria patients and controls from various regions of Tanzania. Genotyping was performed using SNP arrays, ensuring broad genomic coverage for population-wide genetic variation.
  
- **Phenotype Data**: The phenotype of interest was malaria susceptibility or resistance. Covariates such as age, gender, and environmental factors were recorded for inclusion in the analysis.
  
- **Quality Control**: Genotype data were filtered using **PLINK** to remove SNPs with low genotyping quality, minor allele frequency (MAF) < 0.01, and deviations from Hardy-Weinberg Equilibrium (HWE). This ensured the accuracy of downstream analysis.

---

### **b. GWAS Analysis**

- **Tools**: **PLINK** and **EMMAX** were employed to perform single-marker association testing, identifying SNPs associated with malaria susceptibility. EMMAX accounted for population stratification by incorporating a linear mixed model.

- **Population Stratification**: **Principal Component Analysis (PCA)** was performed to correct for population structure. This ensured that associations detected were not confounded by underlying genetic differences across sub-populations.

- **Meta-Analysis**: Regional datasets were integrated using **METAL** to increase statistical power, combining samples from different geographic regions within Tanzania.

---

### **c. AI-Enhanced Analysis**

- **Feature Selection**: Machine learning models, including **Random Forest** and **LASSO Regression**, were applied to prioritize SNPs based on their importance scores. These techniques are robust in detecting non-linear relationships and interaction effects that might be missed by traditional GWAS methods.

- **Deep Learning for Epistasis Detection**: A **Convolutional Neural Network (CNN)** was used to model higher-order interactions (epistasis) between genetic variants. CNNs can capture complex genetic architectures, revealing hidden relationships between SNPs that significantly influence malaria susceptibility.

- **Polygenic Risk Score (PRS)**: PRS was calculated using traditional methods with **PRSice**, and further refined by integrating **Gradient Boosting Machines (GBM)** and **Support Vector Machines (SVM)**. These AI-driven models provided more accurate malaria risk predictions by incorporating both genetic variants and environmental covariates.

---

### **d. Rare Variant Analysis**

- **AI-Based Detection**: Rare variants, which are often challenging to detect due to their small effect sizes, were analyzed using **deep learning-based autoencoders**. This AI-driven approach clustered rare variants and detected associations with malaria resistance that traditional GWAS often fails to identify.

---

## **Results**

- **Significant SNPs**: The GWAS identified several SNPs in genes related to immune response, particularly in the **HBB** and **ATP2B4** genes. These variants have been previously associated with malaria resistance in African populations.

- **AI-Based Insights**: Machine learning models detected non-linear interactions between SNPs located in different genomic regions. These interactions demonstrated that combinations of variants in immune-related genes provided stronger associations with malaria resistance than individual SNPs alone.

- **Polygenic Risk Scores (PRS)**: AI-enhanced PRS models showed improved predictive power for malaria resistance, though challenges remained in fully accounting for gene-environment interactions.

- **Rare Variants**: Deep learning identified rare variants located in regulatory regions of key genes. These variants were not detected by traditional GWAS, emphasizing the importance of regulatory variation in malaria resistance.

---

## **Biological Interpretation**

- **Functional Annotation**: Using tools like **FUMA** and **Enrichr**, significant SNPs were mapped to pathways involved in immune response and red blood cell function. This reinforced the genetic basis for malaria resistance in the Tanzanian population.

- **AI-Based Pathway Analysis**: AI models, particularly **neural networks** and **random forests**, refined the pathway analysis by integrating multiple omics layers (e.g., transcriptomics). These layers uncovered hidden relationships between genes and biological pathways that traditional methods missed, leading to more comprehensive biological interpretations.

---

## **Challenges and Limitations**

- **Population Structure**: The high genetic diversity in the Tanzanian population posed a challenge for population stratification correction. **AI-based clustering** techniques helped group individuals more effectively based on genetic similarity, reducing confounding effects.

- **Low Predictive Power of PRS**: Although AI models improved PRS prediction, they still struggled to fully capture gene-gene and gene-environment interactions due to the complexity of malaria susceptibility.

- **Interpretation of Rare Variants**: Functional interpretation of AI-identified rare variants remains challenging, as experimental validation is often required to confirm their biological significance in malaria resistance.

---

## **Conclusion and Future Work**

This study identified several novel genetic variants associated with malaria resistance in the Tanzanian population, with AI models enhancing the detection of non-linear interactions and rare variants. In future work, the integration of **epigenomics** and **proteomics** data will further refine the understanding of malaria resistance. Additionally, experimental validation of AI-predicted rare variants is necessary to confirm their biological relevance.

---

## **Conclusion: AI in GWAS**

The integration of AI techniques into the GWAS pipeline significantly improves the detection of complex genetic interactions, rare variants, and non-linear relationships. AI models such as **deep learning**, **random forests**, and **gradient boosting** provide robust tools for feature selection, interaction detection, and polygenic trait prediction. This hybrid approach advances the understanding of the genetic underpinnings of diseases like malaria and opens new avenues for precision medicine.

---

### **Repository Structure**

```plaintext
├── data/
│   ├── genotypes/       # Raw genotype data (VCF/PLINK format)
│   ├── phenotypes/      # Phenotype data (CSV/TSV format)
│   └── results/         # GWAS results and model outputs
├── envs/                # Conda environment configurations
│   ├── plink.yaml
│   └── ml.yaml
├── scripts/             # Python scripts for analysis
│   ├── feature_selection.py
│   ├── machine_learning.py
│   ├── deep_learning.py
└── Snakefile            # Snakemake workflow file for pipeline automation
