# Generated by Django 4.0.4 on 2022-12-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockuploader', '0020_remove_stock_user_profilestock_symbol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundamentalAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=300)),
                ('revenue_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('net_income_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('operating_cash_flow_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('free_cash_flow_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('cash_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('book_value_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('tangible_book_value_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('shareholders_equity_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('interest_debt_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('market_cap', models.FloatField(blank=True, default=0, null=True)),
                ('enterprise_value', models.FloatField(blank=True, default=0, null=True)),
                ('price_to_earnings_ratio', models.FloatField(blank=True, default=0, null=True)),
                ('psales_ratio', models.FloatField(blank=True, default=0, null=True)),
                ('price_to_operating_cashflow', models.FloatField(blank=True, default=0, null=True)),
                ('price_to_cashflow', models.FloatField(blank=True, default=0, null=True)),
                ('price_to_book_ratio', models.FloatField(blank=True, default=0, null=True)),
                ('enterprise_value_to_sales', models.FloatField(blank=True, default=0, null=True)),
                ('enterprise_value_to_ebitda', models.FloatField(blank=True, default=0, null=True)),
                ('ev_to_operating_cash_flow', models.FloatField(blank=True, default=0, null=True)),
                ('ev_to_free_cash_flow', models.FloatField(blank=True, default=0, null=True)),
                ('earnings_yield', models.FloatField(blank=True, default=0, null=True)),
                ('free_cash_flow_yield', models.FloatField(blank=True, default=0, null=True)),
                ('debt_to_equity', models.FloatField(blank=True, default=0, null=True)),
                ('debt_to_assets', models.FloatField(blank=True, default=0, null=True)),
                ('current_ratio', models.FloatField(blank=True, default=0, null=True)),
                ('interest_coverage', models.FloatField(blank=True, default=0, null=True)),
                ('income_quality', models.FloatField(blank=True, default=0, null=True)),
                ('dividend_yield', models.FloatField(blank=True, default=0, null=True)),
                ('dividend_yield_percent', models.FloatField(blank=True, default=0, null=True)),
                ('payout_ratio', models.FloatField(blank=True, default=0, null=True)),
                ('sales_and_genral_admin_to_revenue', models.FloatField(blank=True, default=0, null=True)),
                ('research_and_development_to_revenue', models.FloatField(blank=True, default=0, null=True)),
                ('intangibles_to_total_assets', models.FloatField(blank=True, default=0, null=True)),
                ('capex_to_operating_cash_flow', models.FloatField(blank=True, default=0, null=True)),
                ('capex_to_revenue', models.FloatField(blank=True, default=0, null=True)),
                ('capex_to_depreciation', models.FloatField(blank=True, default=0, null=True)),
                ('stock_based_copensation_to_revenue', models.FloatField(blank=True, default=0, null=True)),
                ('graham_number', models.FloatField(blank=True, default=0, null=True)),
                ('return_on_invested_capital', models.FloatField(blank=True, default=0, null=True)),
                ('return_on_tangible_assets', models.FloatField(blank=True, default=0, null=True)),
                ('net_graham_number', models.FloatField(blank=True, default=0, null=True)),
                ('working_capital', models.FloatField(blank=True, default=0, null=True)),
                ('tangible_asset_value', models.FloatField(blank=True, default=0, null=True)),
                ('net_current_asset_value', models.FloatField(blank=True, default=0, null=True)),
                ('invested_capital', models.FloatField(blank=True, default=0, null=True)),
                ('days_sales_outstanding', models.FloatField(blank=True, default=0, null=True)),
                ('days_payables_outstanding', models.FloatField(blank=True, default=0, null=True)),
                ('days_inventory_on_hand', models.FloatField(blank=True, default=0, null=True)),
                ('recievables_turnover', models.FloatField(blank=True, default=0, null=True)),
                ('payables_turnover', models.FloatField(blank=True, default=0, null=True)),
                ('inventory_turnover', models.FloatField(blank=True, default=0, null=True)),
                ('return_on_equity', models.FloatField(blank=True, default=0, null=True)),
                ('capex_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('dividend_per_share', models.FloatField(blank=True, default=0, null=True)),
                ('debt_to_market_cap', models.FloatField(blank=True, default=0, null=True)),
                ('stock', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockuploader.stock')),
            ],
        ),
    ]
