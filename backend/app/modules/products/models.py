from sqlalchemy import Column, String, Boolean, Text, Numeric, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, ItemType, CostComponentType


class Product(UUIDBase, TimestampMixin):
    __tablename__ = "products"
    category = Column(SAEnum(Category), nullable=False)
    item_type = Column(SAEnum(ItemType), nullable=False)
    code = Column(String(50), unique=True, nullable=False, index=True)
    name_en = Column(String(255), nullable=False)
    name_ar = Column(String(255), nullable=True)
    description_en = Column(Text, nullable=True)
    description_ar = Column(Text, nullable=True)
    unit_of_measure = Column(String(20), nullable=False, default="pcs")
    photo_url = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)


class ProductVariant(UUIDBase, TimestampMixin):
    __tablename__ = "product_variants"
    product_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    variant_code = Column(String(50), unique=True, nullable=False, index=True)
    variant_name_en = Column(String(255), nullable=False)
    variant_name_ar = Column(String(255), nullable=True)
    specs = Column(JSONB, nullable=True, default=list)
    default_cost_foreign = Column(Numeric(12, 4), nullable=True)
    default_cost_currency = Column(String(3), nullable=True)
    selling_price_egp = Column(Numeric(12, 4), nullable=True)
    selling_price_usd = Column(Numeric(12, 4), nullable=True)
    selling_price_eur = Column(Numeric(12, 4), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)


class BOMLine(UUIDBase, TimestampMixin):
    __tablename__ = "bom_lines"
    final_product_variant_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    raw_material_variant_id = Column(UUID(as_uuid=True), nullable=False)
    quantity_required = Column(Numeric(14, 4), nullable=False)
    notes = Column(Text, nullable=True)


class ProductCostComponent(UUIDBase):
    __tablename__ = "product_cost_components"
    product_variant_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    component_type = Column(SAEnum(CostComponentType), nullable=False)
    amount = Column(Numeric(12, 4), nullable=False)
    cost_currency = Column(String(3), nullable=False, default="EGP")
    notes = Column(Text, nullable=True)
