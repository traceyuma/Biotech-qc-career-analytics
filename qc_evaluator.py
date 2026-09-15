"""
Biotech Quality Control (QC) Analyst Career Roadmap & Skill Evaluation Script
-----------------------------------------------------------------------------
This script processes evaluation metrics, salary benchmarks, and target tools 
for a Quality Control Analyst (Biotech) candidate, presenting structured 
readiness insights and skill roadmaps.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SkillCategory:
    name: str
    present: List[str]
    missing: List[str]


@dataclass
class SalaryData:
    entry: int
    intermediate: int
    advanced: int
    expert: int
    five_year_growth: str


class BiotechQCEvaluator:
    def __init__(self, candidate_name: str, readiness_score: float):
        self.candidate_name = candidate_name
        self.readiness_score = readiness_score

    def get_skill_breakdown(self) -> Dict[str, SkillCategory]:
        """Returns hard skills, soft skills, and required software tools."""
        return {
            "Hard Skills": SkillCategory(
                name="Hard Skills Baseline",
                present=[
                    "Data Analysis",
                    "Documentation",
                    "Documentation Management Systems",
                    "Environmental Monitoring",
                    "Laboratory Techniques (PCR, ELISA, Chromatography)",
                    "Microbiological Techniques",
                ],
                missing=[
                    "Instrument Calibration",
                    "Quality Assurance",
                    "Regulatory Compliance",
                    "Sterility Testing",
                ],
            ),
            "Soft Skills": SkillCategory(
                name="Soft Skills Baseline",
                present=[
                    "Adaptability",
                    "Attention to Detail",
                    "Attention to Safety",
                    "Communication",
                    "Critical Thinking",
                    "Organizational Skills",
                    "Problem Solving",
                    "Teamwork",
                    "Time Management",
                ],
                missing=["Technical Proficiency"],
            ),
            "Software & Tools": SkillCategory(
                name="Software & Tooling Stack",
                present=[
                    "Document Management Systems (SharePoint, Documentum)",
                    "Microsoft Excel",
                    "Spectroscopy Analysis Tools",
                ],
                missing=[
                    "Biomodule Analysis Software",
                    "Chromatography Data Systems (CDS)",
                    "Data Visualization Software",
                    "Electronic Lab Notebooks (ELNs)",
                    "Laboratory Information Management Systems (LIMS)",
                    "Quality Management Systems (QMS - SAP QM)",
                    "Statistical Analysis Software (Minitab)",
                ],
            ),
        }

    def get_certifications(self) -> Dict[str, List[str]]:
        """Returns required certifications breakdown."""
        return {
            "Required Certifications": [
                "Certified Biotechnology Professional (CBP)",
                "Certified Pharmaceutical GMP Professional (CPGP)",
                "Certified Quality Auditor (CQA)",
                "Certified Quality Engineer (CQE)",
                "Certified Quality Technician (CQT)",
            ]
        }

    def get_global_salaries(self) -> Dict[str, SalaryData]:
        """Returns annual regional compensation benchmarks (USD)."""
        return {
            "Africa": SalaryData(8000, 15000, 25000, 35000, "+27%"),
            "North America": SalaryData(50000, 70000, 90000, 110000, "+22%"),
            "Europe": SalaryData(45000, 60000, 75000, 90000, "+12%"),
            "Asia": SalaryData(10000, 20000, 30000, 40000, "+25%"),
            "Australia": SalaryData(60000, 80000, 100000, 120000, "N/A"),
        }

    def get_risk_mitigation_strategies(self) -> List[str]:
        """Returns actionable strategies for overcoming biotech industry challenges."""
        return [
            "Continuous learning in biotech QC and evolving analytical methods.",
            "Cross-functional collaboration with R&D, manufacturing, and regulatory teams.",
            "Implementing compliance management systems (FDA, GMP, audit controls).",
            "Establishing FMEA and HACCP protocols for contamination risk mitigation.",
            "Utilizing data-driven decision making and statistical process optimization.",
        ]

    def display_report(self) -> None:
        """Prints formatted readiness summary to console."""
        print("=" * 70)
        print(f"  BIOTECH QC ANALYST CAREER EVALUATION REPORT")
        print(f"  Candidate: {self.candidate_name}")
        print(f"  2026 Job Readiness Score: {self.readiness_score}%")
        print("=" * 70 + "\n")

        # 1. Skills & Tools Breakdown
        print("1. SKILL & TOOLING COMPOSITION")
        print("-" * 40)
        for category, data in self.get_skill_breakdown().items():
            print(f"\n[{category}]")
            print(f"  ✓ Present ({len(data.present)}):")
            for item in data.present:
                print(f"     - {item}")
            print(f"  ✗ Missing ({len(data.missing)}):")
            for item in data.missing:
                print(f"     - {item}")

        # 2. Target Certifications
        print("\n" + "=" * 70)
        print("2. RECOMMENDED PROFESSIONAL CERTIFICATIONS")
        print("-" * 40)
        for cert in self.get_certifications()["Required Certifications"]:
            print(f"  - [ ] {cert}")

        # 3. Global Salary Benchmarks
        print("\n" + "=" * 70)
        print("3. GLOBAL SALARY BENCHMARKS (USD)")
        print("-" * 40)
        print(
            f"{'Region':<15} | {'Entry':<10} | {'Intermed.':<10} | {'Advanced':<10} | {'5-Yr Growth'}"
        )
        print("-" * 65)
        for region, sal in self.get_global_salaries().items():
            print(
                f"{region:<15} | ${sal.entry:<9,} | ${sal.intermediate:<9,} | ${sal.advanced:<9,} | {sal.five_year_growth}"
            )

        # 4. Strategic Actions
        print("\n" + "=" * 70)
        print("4. STRATEGIC MITIGATION & GROWTH STEPS")
        print("-" * 40)
        for idx, strategy in enumerate(
            self.get_risk_mitigation_strategies(), 1
        ):
            print(f"  {idx}. {strategy}")
        print("=" * 70 + "\n")


if __name__ == "__main__":
    # Initialize evaluator with report values
    evaluator = BiotechQCEvaluator(
        candidate_name="Tracey Ayuma Isanya", readiness_score=32.0
    )
    evaluator.display_report()
  
