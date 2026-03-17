"""initial schema

Revision ID: 001_initial_schema
Revises:
Create Date: 2026-03-17 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define all enum types with create_type=False so op.create_table won't try
# to CREATE TYPE again (we call .create() explicitly at the top of upgrade()).
userrole_t = postgresql.ENUM('ADMIN', 'SALES_REP', 'WAREHOUSE', 'ACCOUNTANT',
                              name='userrole', create_type=False)
branchcode_t = postgresql.ENUM('GI', 'GIE', 'GEE',
                                name='branchcode', create_type=False)
language_t = postgresql.ENUM('EN', 'AR',
                              name='language', create_type=False)
theme_t = postgresql.ENUM('LIGHT', 'DARK',
                           name='theme', create_type=False)
category_t = postgresql.ENUM('LED_LIGHTS', 'HEATER_THERMOCOUPLE', 'SOLAR_AC', 'TRADE',
                              name='category', create_type=False)
clienttype_t = postgresql.ENUM('INDIVIDUAL', 'BUSINESS',
                                name='clienttype', create_type=False)
suppliertype_t = postgresql.ENUM('FOREIGN', 'LOCAL',
                                  name='suppliertype', create_type=False)
leadstatus_t = postgresql.ENUM('NEW', 'SUPPLIER_CONTACTED', 'OFFER_SENT', 'WON', 'LOST',
                                name='leadstatus', create_type=False)
itemtype_t = postgresql.ENUM('RAW_MATERIAL', 'FINAL_PRODUCT',
                              name='itemtype', create_type=False)
costcomponenttype_t = postgresql.ENUM('LABOUR', 'FREIGHT', 'CUSTOMS', 'OVERHEAD',
                                       name='costcomponenttype', create_type=False)
offerstatus_t = postgresql.ENUM('DRAFT', 'SENT', 'ACCEPTED', 'REJECTED', 'EXPIRED', 'SUPERSEDED',
                                 name='offerstatus', create_type=False)
paymenttype_t = postgresql.ENUM('SINGLE', 'TWO_STAGE',
                                 name='paymenttype', create_type=False)
offerlinetype_t = postgresql.ENUM('PRODUCT', 'SERVICE', 'CUSTOM',
                                   name='offerlinetype', create_type=False)
linesource_t = postgresql.ENUM('FROM_STOCK', 'IMPORT_ORDER', 'PRODUCTION',
                                name='linesource', create_type=False)
salesorderstatus_t = postgresql.ENUM(
    'CONFIRMED', 'AWAITING_STOCK', 'IN_PRODUCTION', 'AWAITING_SHIPMENT',
    'READY_TO_DISPATCH', 'DISPATCHED', 'DELIVERED', 'CANCELLED',
    name='salesorderstatus', create_type=False)
productionstatus_t = postgresql.ENUM('PLANNED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED',
                                      name='productionstatus', create_type=False)
productiontrigger_t = postgresql.ENUM('SALES_ORDER', 'STOCK_BUILD',
                                       name='productiontrigger', create_type=False)
supplierpostatus_t = postgresql.ENUM('DRAFT', 'SENT', 'CONFIRMED', 'SHIPPED', 'RECEIVED', 'CANCELLED',
                                      name='supplierpostatus', create_type=False)
paymentstatus_t = postgresql.ENUM('UNPAID', 'DEPOSIT_PAID', 'FULLY_PAID',
                                   name='paymentstatus', create_type=False)
shipmentstatus_t = postgresql.ENUM('AWAITING_DISPATCH', 'IN_TRANSIT', 'CUSTOMS', 'ARRIVED', 'RECEIVED',
                                    name='shipmentstatus', create_type=False)
stockmovementtype_t = postgresql.ENUM(
    'GOODS_RECEIPT', 'PRODUCTION_OUTPUT', 'SALES_DISPATCH',
    'RESERVATION', 'RESERVATION_RELEASE', 'TRANSFER_OUT', 'TRANSFER_IN', 'ADJUSTMENT',
    name='stockmovementtype', create_type=False)
transferstatus_t = postgresql.ENUM('REQUESTED', 'APPROVED', 'DISPATCHED', 'RECEIVED', 'CANCELLED',
                                    name='transferstatus', create_type=False)
invoicestatus_t = postgresql.ENUM('DRAFT', 'ISSUED', 'SENT', 'PARTIALLY_PAID', 'PAID', 'OVERDUE', 'VOID',
                                   name='invoicestatus', create_type=False)
documenttype_t = postgresql.ENUM('OFFER', 'INVOICE', 'DELIVERY_NOTE', 'SUPPLIER_PO',
                                  name='documenttype', create_type=False)


def upgrade() -> None:
    bind = op.get_bind()

    # Create all enum types explicitly (checkfirst=True is safe for reruns)
    for enum in [
        postgresql.ENUM('ADMIN', 'SALES_REP', 'WAREHOUSE', 'ACCOUNTANT', name='userrole'),
        postgresql.ENUM('GI', 'GIE', 'GEE', name='branchcode'),
        postgresql.ENUM('EN', 'AR', name='language'),
        postgresql.ENUM('LIGHT', 'DARK', name='theme'),
        postgresql.ENUM('LED_LIGHTS', 'HEATER_THERMOCOUPLE', 'SOLAR_AC', 'TRADE', name='category'),
        postgresql.ENUM('INDIVIDUAL', 'BUSINESS', name='clienttype'),
        postgresql.ENUM('FOREIGN', 'LOCAL', name='suppliertype'),
        postgresql.ENUM('NEW', 'SUPPLIER_CONTACTED', 'OFFER_SENT', 'WON', 'LOST', name='leadstatus'),
        postgresql.ENUM('RAW_MATERIAL', 'FINAL_PRODUCT', name='itemtype'),
        postgresql.ENUM('LABOUR', 'FREIGHT', 'CUSTOMS', 'OVERHEAD', name='costcomponenttype'),
        postgresql.ENUM('DRAFT', 'SENT', 'ACCEPTED', 'REJECTED', 'EXPIRED', 'SUPERSEDED', name='offerstatus'),
        postgresql.ENUM('SINGLE', 'TWO_STAGE', name='paymenttype'),
        postgresql.ENUM('PRODUCT', 'SERVICE', 'CUSTOM', name='offerlinetype'),
        postgresql.ENUM('FROM_STOCK', 'IMPORT_ORDER', 'PRODUCTION', name='linesource'),
        postgresql.ENUM('CONFIRMED', 'AWAITING_STOCK', 'IN_PRODUCTION', 'AWAITING_SHIPMENT',
                        'READY_TO_DISPATCH', 'DISPATCHED', 'DELIVERED', 'CANCELLED', name='salesorderstatus'),
        postgresql.ENUM('PLANNED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', name='productionstatus'),
        postgresql.ENUM('SALES_ORDER', 'STOCK_BUILD', name='productiontrigger'),
        postgresql.ENUM('DRAFT', 'SENT', 'CONFIRMED', 'SHIPPED', 'RECEIVED', 'CANCELLED', name='supplierpostatus'),
        postgresql.ENUM('UNPAID', 'DEPOSIT_PAID', 'FULLY_PAID', name='paymentstatus'),
        postgresql.ENUM('AWAITING_DISPATCH', 'IN_TRANSIT', 'CUSTOMS', 'ARRIVED', 'RECEIVED', name='shipmentstatus'),
        postgresql.ENUM('GOODS_RECEIPT', 'PRODUCTION_OUTPUT', 'SALES_DISPATCH',
                        'RESERVATION', 'RESERVATION_RELEASE', 'TRANSFER_OUT', 'TRANSFER_IN', 'ADJUSTMENT',
                        name='stockmovementtype'),
        postgresql.ENUM('REQUESTED', 'APPROVED', 'DISPATCHED', 'RECEIVED', 'CANCELLED', name='transferstatus'),
        postgresql.ENUM('DRAFT', 'ISSUED', 'SENT', 'PARTIALLY_PAID', 'PAID', 'OVERDUE', 'VOID', name='invoicestatus'),
        postgresql.ENUM('OFFER', 'INVOICE', 'DELIVERY_NOTE', 'SUPPLIER_PO', name='documenttype'),
    ]:
        enum.create(bind, checkfirst=True)

    # --- Tables ---

    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('role', userrole_t, nullable=False),
        sa.Column('branch_ids', postgresql.ARRAY(postgresql.UUID(as_uuid=True)), nullable=False),
        sa.Column('default_language', language_t, nullable=False),
        sa.Column('theme', theme_t, nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('last_login_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_users_email', 'users', ['email'])

    op.create_table(
        'branches',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('code', branchcode_t, nullable=False),
        sa.Column('legal_name_en', sa.String(255), nullable=False),
        sa.Column('legal_name_ar', sa.String(255), nullable=False),
        sa.Column('address_en', sa.String(), nullable=True),
        sa.Column('address_ar', sa.String(), nullable=True),
        sa.Column('phone', sa.String(30), nullable=True),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('logo_url', sa.String(), nullable=True),
        sa.Column('vat_number', sa.String(50), nullable=True),
        sa.Column('default_vat_rate', sa.Numeric(5, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_branches_code', 'branches', ['code'], unique=True)

    op.create_table(
        'branch_bank_accounts',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('bank_name', sa.String(255), nullable=False),
        sa.Column('account_name', sa.String(255), nullable=False),
        sa.Column('account_number', sa.String(100), nullable=False),
        sa.Column('iban', sa.String(50), nullable=True),
        sa.Column('swift', sa.String(20), nullable=True),
        sa.Column('currency', sa.String(3), nullable=False),
        sa.Column('is_default', sa.Boolean(), nullable=False),
    )
    op.create_index('ix_branch_bank_accounts_branch_id', 'branch_bank_accounts', ['branch_id'])

    op.create_table(
        'tc_templates',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('document_type', documenttype_t, nullable=False),
        sa.Column('language', language_t, nullable=False),
        sa.Column('content_en', sa.String(), nullable=True),
        sa.Column('content_ar', sa.String(), nullable=True),
        sa.Column('is_default', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        'clients',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('name_en', sa.String(255), nullable=False),
        sa.Column('name_ar', sa.String(255), nullable=True),
        sa.Column('client_type', clienttype_t, nullable=False),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('phone', sa.String(30), nullable=True),
        sa.Column('country', sa.String(100), nullable=True),
        sa.Column('billing_address', postgresql.JSONB(), nullable=True),
        sa.Column('vat_registered', sa.Boolean(), nullable=False),
        sa.Column('vat_number', sa.String(50), nullable=True),
        sa.Column('preferred_currency', sa.String(3), nullable=False),
        sa.Column('payment_terms_days', sa.Numeric(), nullable=False),
        sa.Column('credit_limit', sa.Numeric(14, 2), nullable=True),
        sa.Column('assigned_sales_rep', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_clients_branch_id', 'clients', ['branch_id'])

    op.create_table(
        'suppliers',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('country', sa.String(100), nullable=True),
        sa.Column('supplier_type', suppliertype_t, nullable=False),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('phone', sa.String(30), nullable=True),
        sa.Column('preferred_currency', sa.String(3), nullable=False),
        sa.Column('payment_terms', sa.Text(), nullable=True),
        sa.Column('lead_time_days', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        'exchange_rates',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('from_currency', sa.String(3), nullable=False),
        sa.Column('to_currency', sa.String(3), nullable=False),
        sa.Column('rate', sa.Numeric(12, 6), nullable=False),
        sa.Column('effective_date', sa.Date(), nullable=False),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_exchange_rates_effective_date', 'exchange_rates', ['effective_date'])

    op.create_table(
        'leads',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('prospect_name', sa.String(255), nullable=True),
        sa.Column('prospect_contact', sa.Text(), nullable=True),
        sa.Column('product_description', sa.Text(), nullable=True),
        sa.Column('estimated_quantity', sa.Numeric(14, 4), nullable=True),
        sa.Column('status', leadstatus_t, nullable=False),
        sa.Column('source', sa.String(100), nullable=True),
        sa.Column('assigned_to', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_leads_branch_id', 'leads', ['branch_id'])

    op.create_table(
        'products',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('item_type', itemtype_t, nullable=False),
        sa.Column('code', sa.String(50), nullable=False),
        sa.Column('name_en', sa.String(255), nullable=False),
        sa.Column('name_ar', sa.String(255), nullable=True),
        sa.Column('description_en', sa.Text(), nullable=True),
        sa.Column('description_ar', sa.Text(), nullable=True),
        sa.Column('unit_of_measure', sa.String(20), nullable=False),
        sa.Column('photo_url', sa.Text(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_products_code', 'products', ['code'], unique=True)

    op.create_table(
        'product_variants',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('product_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('variant_code', sa.String(50), nullable=False),
        sa.Column('variant_name_en', sa.String(255), nullable=False),
        sa.Column('variant_name_ar', sa.String(255), nullable=True),
        sa.Column('specs', postgresql.JSONB(), nullable=True),
        sa.Column('default_cost_foreign', sa.Numeric(12, 4), nullable=True),
        sa.Column('default_cost_currency', sa.String(3), nullable=True),
        sa.Column('selling_price_egp', sa.Numeric(12, 4), nullable=True),
        sa.Column('selling_price_usd', sa.Numeric(12, 4), nullable=True),
        sa.Column('selling_price_eur', sa.Numeric(12, 4), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_product_variants_product_id', 'product_variants', ['product_id'])
    op.create_index('ix_product_variants_variant_code', 'product_variants', ['variant_code'], unique=True)

    op.create_table(
        'bom_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('final_product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('raw_material_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quantity_required', sa.Numeric(14, 4), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_bom_lines_final_product_variant_id', 'bom_lines', ['final_product_variant_id'])

    op.create_table(
        'product_cost_components',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('component_type', costcomponenttype_t, nullable=False),
        sa.Column('amount', sa.Numeric(12, 4), nullable=False),
        sa.Column('cost_currency', sa.String(3), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
    )
    op.create_index('ix_product_cost_components_product_variant_id', 'product_cost_components', ['product_variant_id'])

    op.create_table(
        'supplier_pis',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('pi_number', sa.String(50), nullable=True),
        sa.Column('supplier_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('lead_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('currency', sa.String(3), nullable=False),
        sa.Column('fx_rate_snapshot', sa.Numeric(12, 6), nullable=True),
        sa.Column('subtotal_foreign', sa.Numeric(14, 4), nullable=False),
        sa.Column('shipping_cost_foreign', sa.Numeric(14, 4), nullable=True),
        sa.Column('valid_until', sa.Date(), nullable=True),
        sa.Column('received_date', sa.Date(), nullable=True),
        sa.Column('attachment_url', sa.Text(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_supplier_pis_supplier_id', 'supplier_pis', ['supplier_id'])
    op.create_index('ix_supplier_pis_branch_id', 'supplier_pis', ['branch_id'])

    op.create_table(
        'supplier_pi_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('pi_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('quantity', sa.Numeric(14, 4), nullable=False),
        sa.Column('unit_price_foreign', sa.Numeric(12, 4), nullable=False),
        sa.Column('line_total_foreign', sa.Numeric(14, 4), nullable=False),
        sa.Column('sort_order', sa.Integer(), nullable=False),
    )
    op.create_index('ix_supplier_pi_lines_pi_id', 'supplier_pi_lines', ['pi_id'])

    op.create_table(
        'offers',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('offer_number', sa.String(30), nullable=False),
        sa.Column('version', sa.Integer(), nullable=False),
        sa.Column('parent_offer_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('lead_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('supplier_pi_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('status', offerstatus_t, nullable=False),
        sa.Column('sell_currency', sa.String(3), nullable=False),
        sa.Column('fx_rate_used', sa.Numeric(12, 6), nullable=True),
        sa.Column('warranty_duration', sa.String(100), nullable=True),
        sa.Column('delivery_time', sa.String(100), nullable=True),
        sa.Column('subtotal', sa.Numeric(14, 2), nullable=False),
        sa.Column('vat_rate', sa.Numeric(5, 2), nullable=False),
        sa.Column('vat_amount', sa.Numeric(14, 2), nullable=False),
        sa.Column('total', sa.Numeric(14, 2), nullable=False),
        sa.Column('payment_type', paymenttype_t, nullable=False),
        sa.Column('deposit_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('final_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('tc_content_en', sa.Text(), nullable=True),
        sa.Column('tc_content_ar', sa.Text(), nullable=True),
        sa.Column('notes_en', sa.Text(), nullable=True),
        sa.Column('notes_ar', sa.Text(), nullable=True),
        sa.Column('internal_notes', sa.Text(), nullable=True),
        sa.Column('valid_until', sa.Date(), nullable=True),
        sa.Column('sent_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_offers_offer_number', 'offers', ['offer_number'])
    op.create_index('ix_offers_branch_id', 'offers', ['branch_id'])

    op.create_table(
        'offer_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('offer_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('line_type', offerlinetype_t, nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('pi_line_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('description_ar', sa.Text(), nullable=True),
        sa.Column('quantity', sa.Numeric(14, 4), nullable=False),
        sa.Column('unit_of_measure', sa.String(20), nullable=True),
        sa.Column('unit_cost_foreign', sa.Numeric(12, 4), nullable=True),
        sa.Column('unit_cost_local', sa.Numeric(12, 4), nullable=True),
        sa.Column('markup_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('unit_price', sa.Numeric(12, 4), nullable=False),
        sa.Column('line_total', sa.Numeric(14, 2), nullable=False),
        sa.Column('source', linesource_t, nullable=True),
        sa.Column('sort_order', sa.Integer(), nullable=False),
    )
    op.create_index('ix_offer_lines_offer_id', 'offer_lines', ['offer_id'])

    op.create_table(
        'sales_orders',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('order_number', sa.String(30), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('offer_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('client_po_reference', sa.String(100), nullable=True),
        sa.Column('status', salesorderstatus_t, nullable=False),
        sa.Column('sell_currency', sa.String(3), nullable=False),
        sa.Column('fx_rate_used', sa.Numeric(12, 6), nullable=True),
        sa.Column('subtotal', sa.Numeric(14, 2), nullable=False),
        sa.Column('vat_rate', sa.Numeric(5, 2), nullable=False),
        sa.Column('vat_amount', sa.Numeric(14, 2), nullable=False),
        sa.Column('total', sa.Numeric(14, 2), nullable=False),
        sa.Column('payment_type', paymenttype_t, nullable=False),
        sa.Column('deposit_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('deposit_paid_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('final_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('final_paid_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('delivery_address', postgresql.JSONB(), nullable=True),
        sa.Column('requested_delivery_date', sa.Date(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_sales_orders_order_number', 'sales_orders', ['order_number'])
    op.create_index('ix_sales_orders_branch_id', 'sales_orders', ['branch_id'])

    op.create_table(
        'sales_order_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('description_en', sa.Text(), nullable=False),
        sa.Column('description_ar', sa.Text(), nullable=True),
        sa.Column('quantity', sa.Numeric(14, 4), nullable=False),
        sa.Column('unit_price', sa.Numeric(12, 4), nullable=False),
        sa.Column('line_total', sa.Numeric(14, 2), nullable=False),
        sa.Column('source', sa.String(20), nullable=True),
    )
    op.create_index('ix_sales_order_lines_order_id', 'sales_order_lines', ['order_id'])

    op.create_table(
        'production_runs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('trigger_type', productiontrigger_t, nullable=False),
        sa.Column('sales_order_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('status', productionstatus_t, nullable=False),
        sa.Column('planned_start_date', sa.Date(), nullable=True),
        sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_production_runs_branch_id', 'production_runs', ['branch_id'])

    op.create_table(
        'production_run_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('run_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quantity_planned', sa.Numeric(14, 4), nullable=False),
        sa.Column('quantity_produced', sa.Numeric(14, 4), nullable=True),
    )
    op.create_index('ix_production_run_lines_run_id', 'production_run_lines', ['run_id'])

    op.create_table(
        'production_material_consumption',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('run_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('raw_material_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quantity_planned', sa.Numeric(14, 4), nullable=False),
        sa.Column('quantity_actual', sa.Numeric(14, 4), nullable=True),
    )
    op.create_index('ix_production_material_consumption_run_id', 'production_material_consumption', ['run_id'])

    op.create_table(
        'supplier_purchase_orders',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('po_number', sa.String(30), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('supplier_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('sales_order_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('supplier_pi_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('status', supplierpostatus_t, nullable=False),
        sa.Column('currency', sa.String(3), nullable=False),
        sa.Column('fx_rate_at_order', sa.Numeric(12, 6), nullable=True),
        sa.Column('subtotal_foreign', sa.Numeric(14, 4), nullable=False),
        sa.Column('shipping_cost_foreign', sa.Numeric(14, 4), nullable=True),
        sa.Column('total_foreign', sa.Numeric(14, 4), nullable=False),
        sa.Column('payment_type', paymenttype_t, nullable=False),
        sa.Column('deposit_pct', sa.Numeric(5, 2), nullable=True),
        sa.Column('payment_status', paymentstatus_t, nullable=False),
        sa.Column('delivery_destination', sa.Text(), nullable=True),
        sa.Column('expected_lead_time', sa.String(100), nullable=True),
        sa.Column('order_date', sa.Date(), nullable=True),
        sa.Column('expected_arrival_date', sa.Date(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_supplier_purchase_orders_po_number', 'supplier_purchase_orders', ['po_number'])
    op.create_index('ix_supplier_purchase_orders_branch_id', 'supplier_purchase_orders', ['branch_id'])

    op.create_table(
        'supplier_po_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('po_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('quantity', sa.Numeric(14, 4), nullable=False),
        sa.Column('unit_price_foreign', sa.Numeric(12, 4), nullable=False),
        sa.Column('line_total_foreign', sa.Numeric(14, 4), nullable=False),
    )
    op.create_index('ix_supplier_po_lines_po_id', 'supplier_po_lines', ['po_id'])

    op.create_table(
        'shipments',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('supplier_po_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('tracking_reference', sa.String(100), nullable=True),
        sa.Column('shipping_method', sa.String(50), nullable=True),
        sa.Column('status', shipmentstatus_t, nullable=False),
        sa.Column('origin_country', sa.String(100), nullable=True),
        sa.Column('estimated_arrival_date', sa.Date(), nullable=True),
        sa.Column('actual_arrival_date', sa.Date(), nullable=True),
        sa.Column('customs_cleared_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('received_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_shipments_supplier_po_id', 'shipments', ['supplier_po_id'])
    op.create_index('ix_shipments_branch_id', 'shipments', ['branch_id'])

    op.create_table(
        'stock_levels',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quantity_on_hand', sa.Numeric(14, 4), nullable=False),
        sa.Column('quantity_reserved', sa.Numeric(14, 4), nullable=False),
        sa.Column('quantity_available', sa.Numeric(14, 4), nullable=False),
        sa.Column('last_updated_at', sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index('ix_stock_levels_branch_id', 'stock_levels', ['branch_id'])
    op.create_index('ix_stock_levels_product_variant_id', 'stock_levels', ['product_variant_id'])

    op.create_table(
        'stock_movements',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('movement_type', stockmovementtype_t, nullable=False),
        sa.Column('quantity', sa.Numeric(14, 4), nullable=False),
        sa.Column('reference_type', sa.String(50), nullable=True),
        sa.Column('reference_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_stock_movements_branch_id', 'stock_movements', ['branch_id'])
    op.create_index('ix_stock_movements_product_variant_id', 'stock_movements', ['product_variant_id'])

    op.create_table(
        'branch_stock_transfers',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('from_branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('to_branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', transferstatus_t, nullable=False),
        sa.Column('requested_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('approved_by', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        'branch_stock_transfer_lines',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('transfer_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('product_variant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quantity_requested', sa.Numeric(14, 4), nullable=False),
        sa.Column('quantity_approved', sa.Numeric(14, 4), nullable=True),
        sa.Column('quantity_received', sa.Numeric(14, 4), nullable=True),
    )
    op.create_index('ix_branch_stock_transfer_lines_transfer_id', 'branch_stock_transfer_lines', ['transfer_id'])

    op.create_table(
        'invoices',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('invoice_number', sa.String(30), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category', category_t, nullable=False),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('sales_order_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', invoicestatus_t, nullable=False),
        sa.Column('sell_currency', sa.String(3), nullable=False),
        sa.Column('fx_rate_used', sa.Numeric(12, 6), nullable=True),
        sa.Column('subtotal', sa.Numeric(14, 2), nullable=False),
        sa.Column('vat_rate', sa.Numeric(5, 2), nullable=False),
        sa.Column('vat_amount', sa.Numeric(14, 2), nullable=False),
        sa.Column('total', sa.Numeric(14, 2), nullable=False),
        sa.Column('payment_type', paymenttype_t, nullable=False),
        sa.Column('deposit_amount', sa.Numeric(14, 2), nullable=True),
        sa.Column('deposit_paid_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('final_amount', sa.Numeric(14, 2), nullable=True),
        sa.Column('final_paid_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('issue_date', sa.Date(), nullable=False),
        sa.Column('due_date', sa.Date(), nullable=False),
        sa.Column('bank_account_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('tc_content_en', sa.Text(), nullable=True),
        sa.Column('tc_content_ar', sa.Text(), nullable=True),
        sa.Column('notes_en', sa.Text(), nullable=True),
        sa.Column('notes_ar', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_invoices_invoice_number', 'invoices', ['invoice_number'])
    op.create_index('ix_invoices_branch_id', 'invoices', ['branch_id'])

    op.create_table(
        'delivery_notes',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('delivery_number', sa.String(30), nullable=False),
        sa.Column('branch_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('sales_order_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('invoice_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('delivery_address', postgresql.JSONB(), nullable=True),
        sa.Column('dispatched_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('received_by', sa.String(255), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_by', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index('ix_delivery_notes_delivery_number', 'delivery_notes', ['delivery_number'])


def downgrade() -> None:
    bind = op.get_bind()

    # Drop tables in reverse dependency order
    for table in [
        'delivery_notes', 'invoices', 'branch_stock_transfer_lines',
        'branch_stock_transfers', 'stock_movements', 'stock_levels',
        'shipments', 'supplier_po_lines', 'supplier_purchase_orders',
        'production_material_consumption', 'production_run_lines', 'production_runs',
        'sales_order_lines', 'sales_orders', 'offer_lines', 'offers',
        'supplier_pi_lines', 'supplier_pis', 'product_cost_components',
        'bom_lines', 'product_variants', 'products', 'leads',
        'exchange_rates', 'suppliers', 'clients', 'tc_templates',
        'branch_bank_accounts', 'branches', 'users',
    ]:
        op.drop_table(table)

    # Drop enum types
    for enum_name in [
        'documenttype', 'invoicestatus', 'transferstatus', 'stockmovementtype',
        'shipmentstatus', 'paymentstatus', 'supplierpostatus', 'productiontrigger',
        'productionstatus', 'salesorderstatus', 'linesource', 'offerlinetype',
        'paymenttype', 'offerstatus', 'costcomponenttype', 'itemtype',
        'leadstatus', 'suppliertype', 'clienttype', 'category',
        'theme', 'language', 'branchcode', 'userrole',
    ]:
        postgresql.ENUM(name=enum_name, create_type=False).drop(bind, checkfirst=True)
