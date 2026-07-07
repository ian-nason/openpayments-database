# openpayments Data Dictionary

Built from the CMS Open Payments June 2026 publication and the frozen archive ZIPs (PY2013-2018). Authoritative column semantics: the CMS Open Payments Methodology & Data Dictionary, https://www.cms.gov/OpenPayments/Downloads/OpenPaymentsDataDictionary.pdf

Per-era source-column mappings (including which columns exist only pre-2016 or only 2021+) are in crosswalk_openpayments.csv in the build repo.

## general_payments

General (non-research) payments and transfers of value to covered recipients, PY2013-2025. 148,797,140 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `applicable_manufacturer_or_applicable_gpo_making_payment_country` | VARCHAR | 0.0% | Argentina |
| `applicable_manufacturer_or_applicable_gpo_making_payment_id` | VARCHAR | 0.0% | 100000000053 |
| `applicable_manufacturer_or_applicable_gpo_making_payment_name` | VARCHAR | 0.0% | .decimal |
| `applicable_manufacturer_or_applicable_gpo_making_payment_state` | VARCHAR | 0.4% | AK |
| `associated_device_or_medical_supply_pdi_1` | VARCHAR | 59.2% | '00370858000041 |
| `associated_device_or_medical_supply_pdi_2` | VARCHAR | 65.2% | 0 |
| `associated_device_or_medical_supply_pdi_3` | VARCHAR | 65.7% | '00370858000041 |
| `associated_device_or_medical_supply_pdi_4` | VARCHAR | 65.8% | 00035664009229 |
| `associated_device_or_medical_supply_pdi_5` | VARCHAR | 65.9% | 00040565122496 |
| `associated_drug_or_biological_ndc_1` | VARCHAR | 41.3% | 00000-000-00 |
| `associated_drug_or_biological_ndc_2` | VARCHAR | 87.3% | 00000-314-27 |
| `associated_drug_or_biological_ndc_3` | VARCHAR | 96.6% | 00000-314-27 |
| `associated_drug_or_biological_ndc_4` | VARCHAR | 98.9% | 00000-314-27 |
| `associated_drug_or_biological_ndc_5` | VARCHAR | 99.6% | 00000-314-27 |
| `change_type` | VARCHAR | 0.0% | ADD |
| `charity_indicator` | VARCHAR | 58.4% | No |
| `city_of_travel` | VARCHAR | 95.6% | #REF! |
| `contextual_information` | VARCHAR | 91.4% | "1/21/2023 $100.00 Discuss SB
Gaylord Rockies Stu meal with Dr. Prakash Gyawali  |
| `country_of_travel` | VARCHAR | 95.6% | Afghanistan |
| `covered_or_noncovered_indicator_1` | VARCHAR | 22.6% | Covered |
| `covered_or_noncovered_indicator_2` | VARCHAR | 85.0% | Covered |
| `covered_or_noncovered_indicator_3` | VARCHAR | 95.3% | Covered |
| `covered_or_noncovered_indicator_4` | VARCHAR | 98.2% | Covered |
| `covered_or_noncovered_indicator_5` | VARCHAR | 99.1% | Covered |
| `covered_recipient_first_name` | VARCHAR | 0.4% | 'DAVID |
| `covered_recipient_last_name` | VARCHAR | 0.4% | 'WORRELL |
| `covered_recipient_license_state_code1` | VARCHAR | 0.4% | AK |
| `covered_recipient_license_state_code2` | VARCHAR | 97.6% | AK |
| `covered_recipient_license_state_code3` | VARCHAR | 99.4% | AK |
| `covered_recipient_license_state_code4` | VARCHAR | 99.8% | AK |
| `covered_recipient_license_state_code5` | VARCHAR | 99.9% | AK |
| `covered_recipient_middle_name` | VARCHAR | 43.7% | "TRAVIS" |
| `covered_recipient_name_suffix` | VARCHAR | 98.1% | #N/A |
| `covered_recipient_npi` | VARCHAR | 10.8% | 042697983 |
| `covered_recipient_primary_type_1` | VARCHAR | 0.4% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_2` | VARCHAR | 100.0% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_3` | VARCHAR | 100.0% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_4` | VARCHAR | 100.0% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_5` | VARCHAR | 100.0% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_6` | VARCHAR | 100.0% | Anesthesiologist Assistant |
| `covered_recipient_profile_id` | VARCHAR | 0.4% | 1 |
| `covered_recipient_specialty_1` | VARCHAR | 0.4% | Agencies/Case Management |
| `covered_recipient_specialty_2` | VARCHAR | 100.0% | Allopathic & Osteopathic Physicians/Internal Medicine/Interventional Cardiology |
| `covered_recipient_specialty_3` | VARCHAR | 100.0% | Physician Assistants & Advanced Practice Nursing Providers/Nurse Practitioner/Ad |
| `covered_recipient_specialty_4` | VARCHAR | 100.0% | Physician Assistants & Advanced Practice Nursing Providers/Nurse Practitioner/Ad |
| `covered_recipient_specialty_5` | VARCHAR | 100.0% |  |
| `covered_recipient_specialty_6` | VARCHAR | 100.0% |  |
| `covered_recipient_type` | VARCHAR | 0.0% | Covered Recipient Non-Physician Practitioner |
| `date_of_payment` | DATE | 0.0% | 0002-11-30 |
| `delay_in_publication_indicator` | VARCHAR | 0.0% | No |
| `dispute_status_for_publication` | VARCHAR | 0.0% | No |
| `form_of_payment_or_transfer_of_value` | VARCHAR | 0.0% | Any other ownership interest |
| `indicate_drug_or_biological_or_device_or_medical_supply_1` | VARCHAR | 24.2% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_2` | VARCHAR | 85.3% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_3` | VARCHAR | 95.5% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_4` | VARCHAR | 98.3% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_5` | VARCHAR | 99.1% | Biological |
| `name_of_associated_covered_device_or_medical_supply1` | VARCHAR | 96.7% | "Endodontic Dentistry" |
| `name_of_associated_covered_device_or_medical_supply2` | VARCHAR | 99.8% | .8mm Point FG |
| `name_of_associated_covered_device_or_medical_supply3` | VARCHAR | 99.9% | 01-102054S/POUCHED RACK |
| `name_of_associated_covered_device_or_medical_supply4` | VARCHAR | 100.0% | 25mm Xplore Canal Navigation Kit |
| `name_of_associated_covered_device_or_medical_supply5` | VARCHAR | 100.0% | 25/.06 25mm Typhoon Infinite Flex NiTi Files |
| `name_of_associated_covered_drug_or_biological1` | VARCHAR | 86.2% | (810) Chenodal |
| `name_of_associated_covered_drug_or_biological2` | VARCHAR | 96.1% | 18F Sodium Fluoride |
| `name_of_associated_covered_drug_or_biological3` | VARCHAR | 98.8% | 25 .08 21mm Instigator, Orafice Opener |
| `name_of_associated_covered_drug_or_biological4` | VARCHAR | 99.8% | 25mm Xplore Canal Navigation Kit |
| `name_of_associated_covered_drug_or_biological5` | VARCHAR | 99.9% | 3.2 Mixing Tip with Integrated Needle Blue 25 Pack |
| `name_of_drug_or_biological_or_device_or_medical_supply_1` | VARCHAR | 24.4% | "ACTICOAT 4"" X 4""" |
| `name_of_drug_or_biological_or_device_or_medical_supply_2` | VARCHAR | 85.3% | "ACTICOAT 4"" X 4""" |
| `name_of_drug_or_biological_or_device_or_medical_supply_3` | VARCHAR | 95.5% | "ACTICOAT 4"" X 4""" |
| `name_of_drug_or_biological_or_device_or_medical_supply_4` | VARCHAR | 98.3% | "ACTICOAT 4"" X 4""" |
| `name_of_drug_or_biological_or_device_or_medical_supply_5` | VARCHAR | 99.1% | "ACTICOAT 4"" X 4""" |
| `name_of_third_party_entity_receiving_payment_or_transfer_of_value` | VARCHAR | 99.1% | #12  BRAVO ROBINSON |
| `nature_of_payment_or_transfer_of_value` | VARCHAR | 0.0% | Acquisitions |
| `ndc_of_associated_covered_drug_or_biological1` | VARCHAR | 88.2% | 0000034214 |
| `ndc_of_associated_covered_drug_or_biological2` | VARCHAR | 96.5% | 0000034214 |
| `ndc_of_associated_covered_drug_or_biological3` | VARCHAR | 98.9% | 0000034214 |
| `ndc_of_associated_covered_drug_or_biological4` | VARCHAR | 99.8% | 0000034214 |
| `ndc_of_associated_covered_drug_or_biological5` | VARCHAR | 99.9% | 00018-600-04 |
| `number_of_payments_included_in_total_amount` | INTEGER | 0.0% | 0 |
| `payment_publication_date` | DATE | 0.0% | 2021-01-22 |
| `physician_ownership_indicator` | VARCHAR | 6.8% | No |
| `product_category_or_therapeutic_area_1` | VARCHAR | 24.3% | #N/A |
| `product_category_or_therapeutic_area_2` | VARCHAR | 85.3% | 1 |
| `product_category_or_therapeutic_area_3` | VARCHAR | 95.5% | 00850012532620 |
| `product_category_or_therapeutic_area_4` | VARCHAR | 98.3% | 1 |
| `product_category_or_therapeutic_area_5` | VARCHAR | 99.2% | 2 |
| `program_year` | INTEGER | 0.0% | 2013 |
| `recipient_city` | VARCHAR | 0.0% | , ALBUQUERQUE |
| `recipient_country` | VARCHAR | 0.0% | Afghanistan |
| `recipient_postal_code` | VARCHAR | 100.0% | 0 |
| `recipient_primary_business_street_address_line1` | VARCHAR | 0.0% | 	297 Kinderkamack Rd |
| `recipient_primary_business_street_address_line2` | VARCHAR | 71.5% | ! |
| `recipient_province` | VARCHAR | 100.0% | -- |
| `recipient_state` | VARCHAR | 0.0% | 0R |
| `recipient_zip_code` | VARCHAR | 0.0% | - |
| `record_id` | VARCHAR | 0.0% | 100000000 |
| `related_product_indicator` | VARCHAR | 0.0% | Combination |
| `state_of_travel` | VARCHAR | 95.8% | -- SELECT -- |
| `submitting_applicable_manufacturer_or_applicable_gpo_name` | VARCHAR | 0.0% | .decimal |
| `teaching_hospital_ccn` | VARCHAR | 99.6% | 010001 |
| `teaching_hospital_id` | VARCHAR | 99.6% | 1 |
| `teaching_hospital_name` | VARCHAR | 99.6% | ABBOTT NORTHWESTERN HOSPITAL |
| `third_party_equals_covered_recipient_indicator` | VARCHAR | 98.9% | No |
| `third_party_payment_recipient_indicator` | VARCHAR | 0.0% | Entity |
| `total_amount_of_payment_usdollars` | DECIMAL(14,2) | 0.0% | 0.00 |
| `source_file` | VARCHAR | 0.0% | OP_DTL_GNRL_PGYR2013_P01222021.csv |

## research_payments

Research payments (wide form, up to 5 principal investigators per record), PY2013-2025. 10,995,016 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `applicable_manufacturer_or_applicable_gpo_making_payment_country` | VARCHAR | 0.0% | Australia |
| `applicable_manufacturer_or_applicable_gpo_making_payment_id` | VARCHAR | 0.0% | 100000000053 |
| `applicable_manufacturer_or_applicable_gpo_making_payment_name` | VARCHAR | 0.0% | .decimal |
| `applicable_manufacturer_or_applicable_gpo_making_payment_state` | VARCHAR | 12.8% | AL |
| `associated_device_or_medical_supply_pdi_1` | VARCHAR | 60.1% | 00020221662009 |
| `associated_device_or_medical_supply_pdi_2` | VARCHAR | 62.7% | 00081317001034 |
| `associated_device_or_medical_supply_pdi_3` | VARCHAR | 62.8% | 00081317008330 |
| `associated_device_or_medical_supply_pdi_4` | VARCHAR | 62.8% | 00081317001034 |
| `associated_device_or_medical_supply_pdi_5` | VARCHAR | 62.8% | 00607915110147 |
| `associated_drug_or_biological_ndc_1` | VARCHAR | 69.2% | 00000-314-27 |
| `associated_drug_or_biological_ndc_2` | VARCHAR | 99.1% | 00018-607-76 |
| `associated_drug_or_biological_ndc_3` | VARCHAR | 99.7% | 0002-4115-30 |
| `associated_drug_or_biological_ndc_4` | VARCHAR | 99.8% | 0002-4420-30 |
| `associated_drug_or_biological_ndc_5` | VARCHAR | 99.9% | 0004-0800-85 |
| `change_type` | VARCHAR | 0.0% | ADD |
| `clinicaltrials_gov_identifier` | VARCHAR | 74.1% | ABC12345678 |
| `context_of_research` | VARCHAR | 84.1% | "M-Search NGS performance on NDMM patients for plasma cell genomic architecture  |
| `covered_or_noncovered_indicator_1` | VARCHAR | 34.3% | Covered |
| `covered_or_noncovered_indicator_2` | VARCHAR | 97.4% | Covered |
| `covered_or_noncovered_indicator_3` | VARCHAR | 99.1% | Covered |
| `covered_or_noncovered_indicator_4` | VARCHAR | 99.4% | Covered |
| `covered_or_noncovered_indicator_5` | VARCHAR | 99.5% | Covered |
| `covered_recipient_first_name` | VARCHAR | 95.4% | A |
| `covered_recipient_last_name` | VARCHAR | 95.4% | AABERG |
| `covered_recipient_license_state_code1` | VARCHAR | 95.4% | AK |
| `covered_recipient_license_state_code2` | VARCHAR | 99.9% | AK |
| `covered_recipient_license_state_code3` | VARCHAR | 100.0% | AL |
| `covered_recipient_license_state_code4` | VARCHAR | 100.0% | AL |
| `covered_recipient_license_state_code5` | VARCHAR | 100.0% | AL |
| `covered_recipient_middle_name` | VARCHAR | 97.2% | (NMI) |
| `covered_recipient_name_suffix` | VARCHAR | 99.9% | D.O. |
| `covered_recipient_npi` | VARCHAR | 96.2% | 1003013129 |
| `covered_recipient_primary_type_1` | VARCHAR | 95.4% | Anesthesiologist Assistant |
| `covered_recipient_primary_type_2` | VARCHAR | 100.0% |  |
| `covered_recipient_primary_type_3` | VARCHAR | 100.0% |  |
| `covered_recipient_primary_type_4` | VARCHAR | 100.0% |  |
| `covered_recipient_primary_type_5` | VARCHAR | 100.0% |  |
| `covered_recipient_primary_type_6` | VARCHAR | 100.0% |  |
| `covered_recipient_profile_id` | VARCHAR | 95.4% | 1000060 |
| `covered_recipient_specialty_1` | VARCHAR | 95.4% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `covered_recipient_specialty_2` | VARCHAR | 100.0% |  |
| `covered_recipient_specialty_3` | VARCHAR | 100.0% |  |
| `covered_recipient_specialty_4` | VARCHAR | 100.0% |  |
| `covered_recipient_specialty_5` | VARCHAR | 100.0% |  |
| `covered_recipient_specialty_6` | VARCHAR | 100.0% |  |
| `covered_recipient_type` | VARCHAR | 0.0% | Covered Recipient Non-Physician Practitioner |
| `date_of_payment` | DATE | 0.0% | 0002-11-30 |
| `delay_in_publication_indicator` | VARCHAR | 0.0% | No |
| `dispute_status_for_publication` | VARCHAR | 0.0% | No |
| `expenditure_category1` | VARCHAR | 98.1% | Medical Research Writing or Publication |
| `expenditure_category2` | VARCHAR | 100.0% | Medical Research Writing or Publication |
| `expenditure_category3` | VARCHAR | 100.0% | Non-patient Care |
| `expenditure_category4` | VARCHAR | 100.0% | Non-patient Care |
| `expenditure_category5` | VARCHAR | 100.0% | Other |
| `expenditure_category6` | VARCHAR | 100.0% | Other |
| `form_of_payment_or_transfer_of_value` | VARCHAR | 0.0% | Cash or cash equivalent |
| `indicate_drug_or_biological_or_device_or_medical_supply_1` | VARCHAR | 56.3% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_2` | VARCHAR | 98.1% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_3` | VARCHAR | 99.1% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_4` | VARCHAR | 99.4% | Biological |
| `indicate_drug_or_biological_or_device_or_medical_supply_5` | VARCHAR | 99.5% | Biological |
| `name_of_associated_covered_device_or_medical_supply1` | VARCHAR | 98.0% | 1 Data logger, 3 PCT sensitive kits IUO |
| `name_of_associated_covered_device_or_medical_supply2` | VARCHAR | 99.9% | 106041388 |
| `name_of_associated_covered_device_or_medical_supply3` | VARCHAR | 100.0% | 5356 Stool |
| `name_of_associated_covered_device_or_medical_supply4` | VARCHAR | 100.0% | 3M Scotchbond Unviersal Intro kit |
| `name_of_associated_covered_device_or_medical_supply5` | VARCHAR | 100.0% | Asserachrom B2GP1 IgG and IgM Kits |
| `name_of_associated_covered_drug_or_biological1` | VARCHAR | 90.2% | (810) Chenodal |
| `name_of_associated_covered_drug_or_biological2` | VARCHAR | 99.8% | 0051-8462-33 |
| `name_of_associated_covered_drug_or_biological3` | VARCHAR | 100.0% | ALDURAZYME |
| `name_of_associated_covered_drug_or_biological4` | VARCHAR | 100.0% | ADVAIR DISKUS |
| `name_of_associated_covered_drug_or_biological5` | VARCHAR | 100.0% | DEPOT |
| `name_of_drug_or_biological_or_device_or_medical_supply_1` | VARCHAR | 57.0% | (0082) Healthcare Innovation |
| `name_of_drug_or_biological_or_device_or_medical_supply_2` | VARCHAR | 98.2% | 0.185% Riboflavin Ophthalmic Solution (ROS 0185) |
| `name_of_drug_or_biological_or_device_or_medical_supply_3` | VARCHAR | 99.2% | 1382 ESH TOUCH TUBE RACKS |
| `name_of_drug_or_biological_or_device_or_medical_supply_4` | VARCHAR | 99.4% | 2 |
| `name_of_drug_or_biological_or_device_or_medical_supply_5` | VARCHAR | 99.6% | 4-K Telescopes |
| `name_of_study` | VARCHAR | 0.8% | """Daily Adaptive Stereotactic Body Radiation Therapy for Prostate Cancer with U |
| `ndc_of_associated_covered_drug_or_biological1` | VARCHAR | 92.8% | 0000031427 |
| `ndc_of_associated_covered_drug_or_biological2` | VARCHAR | 99.9% | 00018-607-76 |
| `ndc_of_associated_covered_drug_or_biological3` | VARCHAR | 100.0% | 0002-4115-30 |
| `ndc_of_associated_covered_drug_or_biological4` | VARCHAR | 100.0% | 0002-4112-30 |
| `ndc_of_associated_covered_drug_or_biological5` | VARCHAR | 100.0% | 0074-3346-03 |
| `noncovered_recipient_entity_name` | VARCHAR | 18.2% | "BRIGHAM AND WOMEN'S PHYSICIANS ORGANIZATION" |
| `payment_publication_date` | DATE | 0.0% | 2021-01-22 |
| `preclinical_research_indicator` | VARCHAR | 0.0% | No |
| `principal_investigator_1_business_street_address_line1` | VARCHAR | 5.2% | "100 White Spruce Blvd |
| `principal_investigator_1_business_street_address_line2` | VARCHAR | 64.7% | # |
| `principal_investigator_1_city` | VARCHAR | 5.2% | #N/A |
| `principal_investigator_1_country` | VARCHAR | 5.2% | Afghanistan |
| `principal_investigator_1_covered_recipient_type` | VARCHAR | 23.5% | Covered Recipient Non-Physician Practitioner |
| `principal_investigator_1_first_name` | VARCHAR | 5.2% | A |
| `principal_investigator_1_last_name` | VARCHAR | 5.2% | AABERG |
| `principal_investigator_1_license_state_code1` | VARCHAR | 5.2% | AK |
| `principal_investigator_1_license_state_code2` | VARCHAR | 96.0% | AK |
| `principal_investigator_1_license_state_code3` | VARCHAR | 99.2% | AK |
| `principal_investigator_1_license_state_code4` | VARCHAR | 99.8% | AK |
| `principal_investigator_1_license_state_code5` | VARCHAR | 100.0% | AK |
| `principal_investigator_1_middle_name` | VARCHAR | 47.8% | (NAI) |
| `principal_investigator_1_name_suffix` | VARCHAR | 98.3% | 0 |
| `principal_investigator_1_npi` | VARCHAR | 15.5% | 1003000639 |
| `principal_investigator_1_postal_code` | VARCHAR | 99.2% | 00653 |
| `principal_investigator_1_primary_type_1` | VARCHAR | 5.2% | Certified Nurse-Midwife |
| `principal_investigator_1_primary_type_2` | VARCHAR | 100.0% |  |
| `principal_investigator_1_primary_type_3` | VARCHAR | 100.0% |  |
| `principal_investigator_1_primary_type_4` | VARCHAR | 100.0% |  |
| `principal_investigator_1_primary_type_5` | VARCHAR | 100.0% |  |
| `principal_investigator_1_primary_type_6` | VARCHAR | 100.0% |  |
| `principal_investigator_1_profile_id` | VARCHAR | 5.2% | 1000036 |
| `principal_investigator_1_province` | VARCHAR | 99.8% | 02601 |
| `principal_investigator_1_specialty_1` | VARCHAR | 5.2% | Agencies/Public Health or Welfare |
| `principal_investigator_1_specialty_2` | VARCHAR | 100.0% | Physician Assistants & Advanced Practice Nursing Providers/Physician Assistant |
| `principal_investigator_1_specialty_3` | VARCHAR | 100.0% |  |
| `principal_investigator_1_specialty_4` | VARCHAR | 100.0% |  |
| `principal_investigator_1_specialty_5` | VARCHAR | 100.0% |  |
| `principal_investigator_1_specialty_6` | VARCHAR | 100.0% |  |
| `principal_investigator_1_state` | VARCHAR | 5.2% | AE |
| `principal_investigator_1_zip_code` | VARCHAR | 5.2% | 00000-2114 |
| `principal_investigator_2_business_street_address_line1` | VARCHAR | 99.0% | 1 ATWELL RD |
| `principal_investigator_2_business_street_address_line2` | VARCHAR | 99.9% | # 141 |
| `principal_investigator_2_city` | VARCHAR | 99.0% | ABINGTON |
| `principal_investigator_2_country` | VARCHAR | 99.0% | United States |
| `principal_investigator_2_covered_recipient_type` | VARCHAR | 99.2% | Covered Recipient Non-Physician Practitioner |
| `principal_investigator_2_first_name` | VARCHAR | 99.0% | A |
| `principal_investigator_2_last_name` | VARCHAR | 99.0% | AAZAMI |
| `principal_investigator_2_license_state_code1` | VARCHAR | 99.0% | AK |
| `principal_investigator_2_license_state_code2` | VARCHAR | 100.0% | AL |
| `principal_investigator_2_license_state_code3` | VARCHAR | 100.0% | AZ |
| `principal_investigator_2_license_state_code4` | VARCHAR | 100.0% | AL |
| `principal_investigator_2_license_state_code5` | VARCHAR | 100.0% | AZ |
| `principal_investigator_2_middle_name` | VARCHAR | 99.3% | A |
| `principal_investigator_2_name_suffix` | VARCHAR | 100.0% | Dr. |
| `principal_investigator_2_npi` | VARCHAR | 99.1% | 1003015207 |
| `principal_investigator_2_postal_code` | VARCHAR | 100.0% | 00653 |
| `principal_investigator_2_primary_type_1` | VARCHAR | 99.0% | Doctor of Dentistry |
| `principal_investigator_2_primary_type_2` | VARCHAR | 100.0% |  |
| `principal_investigator_2_primary_type_3` | VARCHAR | 100.0% |  |
| `principal_investigator_2_primary_type_4` | VARCHAR | 100.0% |  |
| `principal_investigator_2_primary_type_5` | VARCHAR | 100.0% |  |
| `principal_investigator_2_primary_type_6` | VARCHAR | 100.0% |  |
| `principal_investigator_2_profile_id` | VARCHAR | 99.0% | 1000075 |
| `principal_investigator_2_province` | VARCHAR | 100.0% | PR |
| `principal_investigator_2_specialty_1` | VARCHAR | 99.0% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `principal_investigator_2_specialty_2` | VARCHAR | 100.0% |  |
| `principal_investigator_2_specialty_3` | VARCHAR | 100.0% |  |
| `principal_investigator_2_specialty_4` | VARCHAR | 100.0% |  |
| `principal_investigator_2_specialty_5` | VARCHAR | 100.0% |  |
| `principal_investigator_2_specialty_6` | VARCHAR | 100.0% |  |
| `principal_investigator_2_state` | VARCHAR | 99.0% | AK |
| `principal_investigator_2_zip_code` | VARCHAR | 99.0% | 00682-1560 |
| `principal_investigator_3_business_street_address_line1` | VARCHAR | 99.3% | 1 EDMUNDSON PL |
| `principal_investigator_3_business_street_address_line2` | VARCHAR | 100.0% | # TCB1380 |
| `principal_investigator_3_city` | VARCHAR | 99.3% | ADDISON |
| `principal_investigator_3_country` | VARCHAR | 99.3% | United States |
| `principal_investigator_3_covered_recipient_type` | VARCHAR | 99.4% | Covered Recipient Non-Physician Practitioner |
| `principal_investigator_3_first_name` | VARCHAR | 99.3% | AAMIR |
| `principal_investigator_3_last_name` | VARCHAR | 99.3% | AARON |
| `principal_investigator_3_license_state_code1` | VARCHAR | 99.3% | AL |
| `principal_investigator_3_license_state_code2` | VARCHAR | 100.0% | AL |
| `principal_investigator_3_license_state_code3` | VARCHAR | 100.0% | AZ |
| `principal_investigator_3_license_state_code4` | VARCHAR | 100.0% | CA |
| `principal_investigator_3_license_state_code5` | VARCHAR | 100.0% | MO |
| `principal_investigator_3_middle_name` | VARCHAR | 99.5% | A |
| `principal_investigator_3_name_suffix` | VARCHAR | 100.0% | D.O. |
| `principal_investigator_3_npi` | VARCHAR | 99.3% | 1003070327 |
| `principal_investigator_3_postal_code` | VARCHAR | 100.0% |  |
| `principal_investigator_3_primary_type_1` | VARCHAR | 99.3% | Doctor of Dentistry |
| `principal_investigator_3_primary_type_2` | VARCHAR | 100.0% |  |
| `principal_investigator_3_primary_type_3` | VARCHAR | 100.0% |  |
| `principal_investigator_3_primary_type_4` | VARCHAR | 100.0% |  |
| `principal_investigator_3_primary_type_5` | VARCHAR | 100.0% |  |
| `principal_investigator_3_primary_type_6` | VARCHAR | 100.0% |  |
| `principal_investigator_3_profile_id` | VARCHAR | 99.3% | 1001001 |
| `principal_investigator_3_province` | VARCHAR | 100.0% |  |
| `principal_investigator_3_specialty_1` | VARCHAR | 99.3% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `principal_investigator_3_specialty_2` | VARCHAR | 100.0% |  |
| `principal_investigator_3_specialty_3` | VARCHAR | 100.0% |  |
| `principal_investigator_3_specialty_4` | VARCHAR | 100.0% |  |
| `principal_investigator_3_specialty_5` | VARCHAR | 100.0% |  |
| `principal_investigator_3_specialty_6` | VARCHAR | 100.0% |  |
| `principal_investigator_3_state` | VARCHAR | 99.3% | AL |
| `principal_investigator_3_zip_code` | VARCHAR | 99.3% | 00917 |
| `principal_investigator_4_business_street_address_line1` | VARCHAR | 99.4% | 1 Bowdoin Sq |
| `principal_investigator_4_business_street_address_line2` | VARCHAR | 100.0% | #102 |
| `principal_investigator_4_city` | VARCHAR | 99.4% | ADDISON |
| `principal_investigator_4_country` | VARCHAR | 99.4% | United States |
| `principal_investigator_4_covered_recipient_type` | VARCHAR | 99.4% | Covered Recipient Physician |
| `principal_investigator_4_first_name` | VARCHAR | 99.4% | AAMIR |
| `principal_investigator_4_last_name` | VARCHAR | 99.4% | ABBAS |
| `principal_investigator_4_license_state_code1` | VARCHAR | 99.4% | AL |
| `principal_investigator_4_license_state_code2` | VARCHAR | 100.0% | AL |
| `principal_investigator_4_license_state_code3` | VARCHAR | 100.0% | AZ |
| `principal_investigator_4_license_state_code4` | VARCHAR | 100.0% | MO |
| `principal_investigator_4_license_state_code5` | VARCHAR | 100.0% | FL |
| `principal_investigator_4_middle_name` | VARCHAR | 99.5% | A |
| `principal_investigator_4_name_suffix` | VARCHAR | 100.0% | II |
| `principal_investigator_4_npi` | VARCHAR | 99.4% | 1003070327 |
| `principal_investigator_4_postal_code` | VARCHAR | 100.0% |  |
| `principal_investigator_4_primary_type_1` | VARCHAR | 99.4% | Doctor of Dentistry |
| `principal_investigator_4_primary_type_2` | VARCHAR | 100.0% |  |
| `principal_investigator_4_primary_type_3` | VARCHAR | 100.0% |  |
| `principal_investigator_4_primary_type_4` | VARCHAR | 100.0% |  |
| `principal_investigator_4_primary_type_5` | VARCHAR | 100.0% |  |
| `principal_investigator_4_primary_type_6` | VARCHAR | 100.0% |  |
| `principal_investigator_4_profile_id` | VARCHAR | 99.4% | 1001001 |
| `principal_investigator_4_province` | VARCHAR | 100.0% | US |
| `principal_investigator_4_specialty_1` | VARCHAR | 99.4% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `principal_investigator_4_specialty_2` | VARCHAR | 100.0% |  |
| `principal_investigator_4_specialty_3` | VARCHAR | 100.0% |  |
| `principal_investigator_4_specialty_4` | VARCHAR | 100.0% |  |
| `principal_investigator_4_specialty_5` | VARCHAR | 100.0% |  |
| `principal_investigator_4_specialty_6` | VARCHAR | 100.0% |  |
| `principal_investigator_4_state` | VARCHAR | 99.4% | AL |
| `principal_investigator_4_zip_code` | VARCHAR | 99.4% | 01107 |
| `principal_investigator_5_business_street_address_line1` | VARCHAR | 99.4% | 1 CHILDRENS PLZ |
| `principal_investigator_5_business_street_address_line2` | VARCHAR | 100.0% | #410 |
| `principal_investigator_5_city` | VARCHAR | 99.4% | ALBUQUERQUE |
| `principal_investigator_5_country` | VARCHAR | 99.4% | United States |
| `principal_investigator_5_covered_recipient_type` | VARCHAR | 99.4% | Covered Recipient Physician |
| `principal_investigator_5_first_name` | VARCHAR | 99.4% | AAMIR |
| `principal_investigator_5_last_name` | VARCHAR | 99.4% | ABADIN |
| `principal_investigator_5_license_state_code1` | VARCHAR | 99.4% | AK |
| `principal_investigator_5_license_state_code2` | VARCHAR | 100.0% | AZ |
| `principal_investigator_5_license_state_code3` | VARCHAR | 100.0% | AZ |
| `principal_investigator_5_license_state_code4` | VARCHAR | 100.0% | CA |
| `principal_investigator_5_license_state_code5` | VARCHAR | 100.0% | AZ |
| `principal_investigator_5_middle_name` | VARCHAR | 99.5% | A |
| `principal_investigator_5_name_suffix` | VARCHAR | 100.0% | II |
| `principal_investigator_5_npi` | VARCHAR | 99.4% | 1003856568 |
| `principal_investigator_5_postal_code` | VARCHAR | 100.0% |  |
| `principal_investigator_5_primary_type_1` | VARCHAR | 99.4% | Doctor of Optometry |
| `principal_investigator_5_primary_type_2` | VARCHAR | 100.0% |  |
| `principal_investigator_5_primary_type_3` | VARCHAR | 100.0% |  |
| `principal_investigator_5_primary_type_4` | VARCHAR | 100.0% |  |
| `principal_investigator_5_primary_type_5` | VARCHAR | 100.0% |  |
| `principal_investigator_5_primary_type_6` | VARCHAR | 100.0% |  |
| `principal_investigator_5_profile_id` | VARCHAR | 99.4% | 1010712 |
| `principal_investigator_5_province` | VARCHAR | 100.0% |  |
| `principal_investigator_5_specialty_1` | VARCHAR | 99.4% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `principal_investigator_5_specialty_2` | VARCHAR | 100.0% |  |
| `principal_investigator_5_specialty_3` | VARCHAR | 100.0% |  |
| `principal_investigator_5_specialty_4` | VARCHAR | 100.0% |  |
| `principal_investigator_5_specialty_5` | VARCHAR | 100.0% |  |
| `principal_investigator_5_specialty_6` | VARCHAR | 100.0% |  |
| `principal_investigator_5_state` | VARCHAR | 99.4% | AL |
| `principal_investigator_5_zip_code` | VARCHAR | 99.4% | 00927 |
| `product_category_or_therapeutic_area_1` | VARCHAR | 58.3% | 014 Radial Catheter |
| `product_category_or_therapeutic_area_2` | VARCHAR | 98.2% | AB-0003 |
| `product_category_or_therapeutic_area_3` | VARCHAR | 99.2% | 30 pack Flocked Swabs: RFIT-SUB-0439 |
| `product_category_or_therapeutic_area_4` | VARCHAR | 99.4% | 30 pack Flocked Swabs: RFIT-SUB-0439 |
| `product_category_or_therapeutic_area_5` | VARCHAR | 99.6% | APPLIANCE, FIXATION, SPINAL INTERLAMINAL; ORTHOSIS, CERVICAL PEDICLE SCREW SPINA |
| `program_year` | INTEGER | 0.0% | 2013 |
| `recipient_city` | VARCHAR | 0.1% | "LEE'S SUMMIT" |
| `recipient_country` | VARCHAR | 0.1% | Afghanistan |
| `recipient_postal_code` | VARCHAR | 99.9% | 00001 |
| `recipient_primary_business_street_address_line1` | VARCHAR | 0.1% | """3000 Bayview Drive Fort Lauderdale, FL 33006""" |
| `recipient_primary_business_street_address_line2` | VARCHAR | 77.2% | "C-212 BOX 356340" |
| `recipient_province` | VARCHAR | 100.0% | 006 |
| `recipient_state` | VARCHAR | 0.1% | AK |
| `recipient_zip_code` | VARCHAR | 0.1% | 00000-2114 |
| `record_id` | VARCHAR | 0.0% | 1000082011 |
| `related_product_indicator` | VARCHAR | 0.0% | Combination |
| `research_information_link` | VARCHAR | 97.4% | WWW.GEISTLICH-CH.COM |
| `submitting_applicable_manufacturer_or_applicable_gpo_name` | VARCHAR | 0.0% | .decimal |
| `teaching_hospital_ccn` | VARCHAR | 86.4% | 010001 |
| `teaching_hospital_id` | VARCHAR | 86.4% | 1 |
| `teaching_hospital_name` | VARCHAR | 86.4% | ABBOTT NORTHWESTERN HOSPITAL |
| `total_amount_of_payment_usdollars` | DECIMAL(14,2) | 0.0% | 0.00 |
| `source_file` | VARCHAR | 0.0% | OP_DTL_RSRCH_PGYR2013_P01222021.csv |

## research_payment_investigators

Long form of research-payment principal investigators: one row per (record, PI slot). 10,745,869 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `record_id` | VARCHAR | 0.0% | 1000082011 |
| `program_year` | INTEGER | 0.0% | 2013 |
| `pi_position` | INTEGER | 0.0% | 1 |
| `pi_profile_id` | VARCHAR | 0.0% | 1000036 |
| `pi_npi` | VARCHAR | 10.7% | 1003000639 |
| `pi_first_name` | VARCHAR | 0.0% | A |
| `pi_middle_name` | VARCHAR | 44.3% | (NAI) |
| `pi_last_name` | VARCHAR | 0.0% | AABERG |
| `pi_name_suffix` | VARCHAR | 98.2% | 0 |
| `pi_city` | VARCHAR | 0.0% | #N/A |
| `pi_state` | VARCHAR | 0.0% | AE |
| `pi_country` | VARCHAR | 0.0% | Afghanistan |
| `pi_primary_type_1` | VARCHAR | 0.0% | Certified Nurse-Midwife |
| `pi_specialty_1` | VARCHAR | 0.0% | Agencies/Public Health or Welfare |

## ownership_payments

Physician ownership and investment interests, PY2013-2025. 53,915 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `applicable_manufacturer_or_applicable_gpo_making_payment_country` | VARCHAR | 0.0% | Australia |
| `applicable_manufacturer_or_applicable_gpo_making_payment_id` | VARCHAR | 0.0% | 100000000075 |
| `applicable_manufacturer_or_applicable_gpo_making_payment_name` | VARCHAR | 0.0% | 3NT Medical |
| `applicable_manufacturer_or_applicable_gpo_making_payment_state` | VARCHAR | 0.7% | AK |
| `change_type` | VARCHAR | 0.0% | CHANGED |
| `dispute_status_for_publication` | VARCHAR | 0.0% | No |
| `interest_held_by_physician_or_an_immediate_family_member` | VARCHAR | 0.0% | Immediate family member |
| `payment_publication_date` | DATE | 0.0% | 2021-01-22 |
| `physician_first_name` | VARCHAR | 0.0% | A |
| `physician_last_name` | VARCHAR | 0.0% | AABERG |
| `physician_middle_name` | VARCHAR | 64.8% | A |
| `physician_name_suffix` | VARCHAR | 87.7% | 02129 |
| `physician_npi` | VARCHAR | 19.9% | 1003001165 |
| `physician_primary_type` | VARCHAR | 0.0% | Chiropractor |
| `physician_profile_id` | VARCHAR | 0.0% | 100005 |
| `physician_specialty` | VARCHAR | 1.2% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `program_year` | INTEGER | 0.0% | 2013 |
| `recipient_city` | VARCHAR | 0.0% | 1300 CENTERVIEW DR |
| `recipient_country` | VARCHAR | 0.0% | Brazil |
| `recipient_postal_code` | VARCHAR | 100.0% | 008210 |
| `recipient_primary_business_street_address_line1` | VARCHAR | 0.0% | "900 NW 17th St |
| `recipient_primary_business_street_address_line2` | VARCHAR | 59.9% | # 1030 |
| `recipient_province` | VARCHAR | 100.0% | American Samoa |
| `recipient_state` | VARCHAR | 0.0% | AK |
| `recipient_zip_code` | VARCHAR | 0.0% | 00907 |
| `record_id` | VARCHAR | 0.0% | 1001507833 |
| `submitting_applicable_manufacturer_or_applicable_gpo_name` | VARCHAR | 0.0% | 3NT Medical |
| `terms_of_interest` | VARCHAR | 0.0% | "Dollar Amount Invested" is total value of stock at close of market on 12/31/14. |
| `total_amount_invested_usdollars` | DECIMAL(14,2) | 0.0% | 0.00 |
| `value_of_interest` | VARCHAR | 0.0% | 0.00 |
| `source_file` | VARCHAR | 0.0% | OP_DTL_OWNRSHP_PGYR2013_P01222021.csv |

## covered_recipients

Covered Recipient Profile Supplement: one row per physician/NPP profile with NPI. 1,697,025 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `covered_recipient_profile_type` | VARCHAR | 0.0% | Covered Recipient Non-Physician Practitioner |
| `covered_recipient_profile_id` | VARCHAR | 0.0% | 1 |
| `associated_covered_recipient_profile_id_1` | VARCHAR | 99.5% | 1002323 |
| `associated_covered_recipient_profile_id_2` | VARCHAR | 100.0% | 1008683 |
| `covered_recipient_npi` | VARCHAR | 0.9% | 1003000126 |
| `covered_recipient_profile_first_name` | VARCHAR | 0.0% | A |
| `covered_recipient_profile_middle_name` | VARCHAR | 35.6% | A |
| `covered_recipient_profile_last_name` | VARCHAR | 0.0% | A |
| `covered_recipient_profile_suffix` | VARCHAR | 99.6% | I |
| `covered_recipient_profile_alternate_first_name` | VARCHAR | 53.1% | A |
| `covered_recipient_profile_alternate_middle_name` | VARCHAR | 68.0% | A |
| `covered_recipient_profile_alternate_last_name` | VARCHAR | 53.1% | A |
| `covered_recipient_profile_alternate_suffix` | VARCHAR | 98.3% | I |
| `covered_recipient_profile_address_line_1` | VARCHAR | 0.0% | # 1 PASTERNAK ST |
| `covered_recipient_profile_address_line_2` | VARCHAR | 77.0% | ! |
| `covered_recipient_profile_city` | VARCHAR | 0.0% | 008-B213 |
| `covered_recipient_profile_state` | VARCHAR | 0.0% | AA |
| `covered_recipient_profile_zipcode` | VARCHAR | 0.0% | 0 |
| `covered_recipient_profile_country_name` | VARCHAR | 0.0% | ARGENTINA |
| `covered_recipient_profile_province_name` | VARCHAR | 100.0% | 00000 |
| `covered_recipient_profile_primary_specialty` | VARCHAR | 4.0% | Allopathic & Osteopathic Physicians/Allergy & Immunology |
| `covered_recipient_profile_ops_taxonomy_1` | VARCHAR | 0.0% | 111N00000X |
| `covered_recipient_profile_ops_taxonomy_2` | VARCHAR | 78.4% | 111N00000X |
| `covered_recipient_profile_ops_taxonomy_3` | VARCHAR | 96.2% | 111N00000X |
| `covered_recipient_profile_ops_taxonomy_4` | VARCHAR | 99.3% | 111N00000X |
| `covered_recipient_profile_ops_taxonomy_5` | VARCHAR | 99.8% | 111N00000X |
| `covered_recipient_profile_ops_taxonomy_6` | VARCHAR | 99.9% | 111NR0200X |
| `covered_recipient_profile_license_state_code_1` | VARCHAR | 0.0% | AK |
| `covered_recipient_profile_license_state_code_2` | VARCHAR | 59.2% | AK |
| `covered_recipient_profile_license_state_code_3` | VARCHAR | 83.6% | AK |
| `covered_recipient_profile_license_state_code_4` | VARCHAR | 93.0% | AK |
| `covered_recipient_profile_license_state_code_5` | VARCHAR | 96.6% | AK |

## deleted_records

Record IDs deleted between publications (PY2016+; earlier years never had these files). 162,030 rows.

| Column | Type | Null % | Example |
|--------|------|--------|---------|
| `change_type` | VARCHAR | 0.0% | DELETED |
| `program_year` | INTEGER | 0.0% | 2016 |
| `payment_type` | VARCHAR | 0.0% | General |
| `record_id` | VARCHAR | 0.0% | 1006169905 |
| `source_file` | VARCHAR | 0.0% | OP_REMOVED_DELETED_PGYR2016_P01182024.csv |
