/*
    ANALYTICS MODEL: fct_sales_summary
    PURPOSE: Aggregating cleaned sales data to provide high-level business insights.
    GRAIN: Product per Region
*/

{{ config(materialized='table') }}

with sales_data as (
    -- Reference the cleaned staging model
    select * from {{ ref('stg_sales') }}
)

select
    product_name,
    region,
    -- 1. Volume Metrics
    count(*) as total_orders,
    sum(units_sold) as total_units_sold,
    sum(returns) as total_returns,
    
    -- 2. Financial Performance
    round(sum(revenue), 2) as total_revenue,
    round(sum(net_profit), 2) as total_profit,
    
    -- 3. Business KPIs (Key Performance Indicators)
    -- Average Order Value (AOV)
    round(sum(revenue) / count(*), 2) as avg_order_value,
    
    -- Return Rate Percentage
    round(
        case 
            when sum(units_sold) > 0 then (sum(returns) * 1.0 / sum(units_sold)) * 100 
            else 0 
        end, 2
    ) as return_rate_pct,

    -- Profit Margin Percentage
    round(
        case 
            when sum(revenue) > 0 then (sum(net_profit) / sum(revenue)) * 100 
            else 0 
        end, 2
    ) as profit_margin_pct

from sales_data
group by 1, 2
order by total_profit desc
