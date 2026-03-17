from sqlalchemy import Column, Numeric, Text, Date, DateTime, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, ProductionStatus, ProductionTrigger

class ProductionRun(UUIDBase, TimestampMixin):
    __tablename__ = "production_runs"
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    trigger_type = Column(SAEnum(ProductionTrigger), nullable=False)
    sales_order_id = Column(UUID(as_uuid=True), nullable=True)
    status = Column(SAEnum(ProductionStatus), nullable=False, default=ProductionStatus.PLANNED)
    planned_start_date = Column(Date, nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)

class ProductionRunLine(UUIDBase):
    __tablename__ = "production_run_lines"
    run_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    product_variant_id = Column(UUID(as_uuid=True), nullable=False)
    quantity_planned = Column(Numeric(14, 4), nullable=False)
    quantity_produced = Column(Numeric(14, 4), nullable=True)

class ProductionMaterialConsumption(UUIDBase):
    __tablename__ = "production_material_consumption"
    run_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    raw_material_variant_id = Column(UUID(as_uuid=True), nullable=False)
    quantity_planned = Column(Numeric(14, 4), nullable=False)
    quantity_actual = Column(Numeric(14, 4), nullable=True)
