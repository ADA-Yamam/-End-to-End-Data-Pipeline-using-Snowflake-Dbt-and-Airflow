{% macro clean_string(column_name) %}
    trim(upper({{ column_name }}))
{% endmacro %}

{% macro format_money(column_name) %}
    round(cast({{ column_name }} as numeric(16,2)), 2)
{% endmacro %}

{% macro safe_divide_pct(numerator, denominator) %}
    round(
        case 
            when {{ denominator }} > 0 then ({{ numerator }} * 1.0 / {{ denominator }}) * 100 
            else 0 
        end, 2
    )
{% endmacro %}
