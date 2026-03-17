from sqlalchemy import Column, String, Integer, Numeric, Text, Boolean, DateTime, Date, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from app.shared.base_model import UUIDBase, TimestampMixin
from app.shared.enums import Category, OfferStatus, PaymentType, OfferLineType, LineSource

class Offer(UUIDBase, TimestampMixin):
    __tablename__ = "offers"
    offer_number = Column(String(30), nullable=False, index=True)
    version = Column(Integer, nullable=False, default=1)
    parent_offer_id = Column(UUID(as_uuid=True), nullable=True)
    branch_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category = Column(SAEnum(Category), nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    lead_id = Column(UUID(as_uuid=True), nullable=True)
    supplier_pi_id = Column(UUID(as_uuid=True), nullable=True)
    status = Column(SAEnum(OfferStatus), nullable=False, default=OfferStatus.DRAFT)
    sell_currency = Column(String(3), nullable=False, default="EGP")
    fx_rate_used = Column(Numeric(12, 6), nullable=True)
    warranty_duration = Column(String(100), nullable=True)
    delivery_time = Column(String(100), nullable=True)
    subtotal = Column(Numeric(14, 2), nullable=False, default=0)
    vat_rate = Column(Numeric(5, 2), nullable=False, default=14)
    vat_amount = Column(Numeric(14, 2), nullable=False, default=0)
    total = Column(Numeric(14, 2), nullable=False, default=0)
    payment_type = Column(SAEnum(PaymentType), nullable=False, default=PaymentType.SINGLE)
    deposit_pct = Column(Numeric(5, 2), nullable=True)
    final_pct = Column(Numeric(5, 2), nullable=True)
    tc_content_en = Column(Text, nullable=True)
    tc_content_ar = Column(Text, nullable=True)
    notes_en = Column(Text, nullable=True)
    notes_ar = Column(Text, nullable=True)
    internal_notes = Column(Text, nullable=True)
    valid_until = Column(Date, nullable=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=False)

class OfferLine(UUIDBase):
    __tablename__ = "offer_lines"
    offer_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    line_type = Column(SAEnum(OfferLineType), nullable=False, default=OfferLineType.PRODUCT)
    product_variant_id = Column(UUID(as_uuid=True), nullable=True)
    pi_line_id = Column(UUID(as_uuid=True), nullable=True)
    description_en = Column(Text, nullable=False)
    description_ar = Column(Text, nullable=True)
    quantity = Column(Numeric(14, 4), nullable=False)
    unit_of_measure = Column(String(20), nullable=True)
    unit_cost_foreign = Column(Numeric(12, 4), nullable=True)
    unit_cost_local = Column(Numeric(12, 4), nullable=True)
    markup_pct = Column(Numeric(5, 2), nullable=True)
    unit_price = Column(Numeric(12, 4), nullable=False)
    line_total = Column(Numeric(14, 2), nullable=False)
    source = Column(SAEnum(LineSource), nullable=True)
    sort_order = Column(Integer, nullable=False, default=0)
