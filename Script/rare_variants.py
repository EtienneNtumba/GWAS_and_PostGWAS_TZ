import subprocess

# Define input files
vcf_file = "data/genotypes/your_genotype_data.vcf"
phenotype_file = "data/phenotypes/your_phenotype_data.txt"
output_prefix = "results/rare_variant_analysis"

# Run RVTests for Burden and SKAT tests
def run_rare_variant_analysis(vcf_file, phenotype_file, output_prefix):
    try:
        subprocess.run([
            "rvtest", 
            "--inVcf", vcf_file, 
            "--pheno", phenotype_file, 
            "--burden", 
            "--skat", 
            "--out", output_prefix
        ], check=True)
        print(f"Rare variant analysis completed successfully. Results saved in {output_prefix}.")
    except subprocess.CalledProcessError as e:
        print(f"Error in running RVTests: {e}")

# Run the analysis
run_rare_variant_analysis(vcf_file, phenotype_file, output_prefix)

