/*
    STAGING MODEL: stg_sales
    PURPOSE: Clean and standardize raw sales data from Snowflake.ٍٍ
    REVISIONS:
    - Standardized text casing for PRODUCT and REGION.
    - Included missing metrics: UNITS_SOLD, RETURNS.
    - Filtered out invalid records (Returns > Units Sold).
    - Rounded financial values to 2 decimal places for accuracy.
*/

with raw_data as (
    -- Direct reference to the raw source table in Snowflake
    select * from MY_ANALYSIS_DB.RAW_DATA.RAW_SALESS
)

select
    -- 1. Date and Time Standardization
    cast(DATE as date) as sales_date,
    
    -- 2. Text Normalization (Trimming and Uppercasing)
    trim(upper(PRODUCT)) as product_name,
    trim(upper(REGION)) as region,
    
    -- 3. Volume Metrics
    cast(UNITS_SOLD as integer) as units_sold,
    cast(RETURNS as integer) as returns,
    
    -- 4. Financial Metrics (Using numeric for precision)
    round(cast(REVENUE as numeric(16,2)), 2) as revenue,
    round(cast(MARKETING_SPEND as numeric(16,2)), 2) as marketing_spend,
    
    -- 5. Calculated Fields
    round(cast(REVENUE - MARKETING_SPEND as numeric(16,2)), 2) as net_profit

from raw_data
where 
    -- Business Logic Filter: Returns cannot exceed units sold
    RETURNS <= UNITS_SOLD 
    -- Data Quality Filter: Ensure it has a valid date
    and DATE is not null
