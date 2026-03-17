import enum


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    SALES_REP = "SALES_REP"
    WAREHOUSE = "WAREHOUSE"
    ACCOUNTANT = "ACCOUNTANT"


class BranchCode(str, enum.Enum):
    GI = "GI"    # Gamma International — Nasr City
    GIE = "GIE"  # Gamma International Egypt — Obour City
    GEE = "GEE"  # Gamma Egypt for Engineering & Trade


class Category(str, enum.Enum):
    LED_LIGHTS = "LED_LIGHTS"
    HEATER_THERMOCOUPLE = "HEATER_THERMOCOUPLE"
    SOLAR_AC = "SOLAR_AC"
    TRADE = "TRADE"


class Language(str, enum.Enum):
    EN = "EN"
    AR = "AR"


class Theme(str, enum.Enum):
    LIGHT = "LIGHT"
    DARK = "DARK"


class ItemType(str, enum.Enum):
    RAW_MATERIAL = "RAW_MATERIAL"
    FINAL_PRODUCT = "FINAL_PRODUCT"


class SupplierType(str, enum.Enum):
    FOREIGN = "FOREIGN"
    LOCAL = "LOCAL"


class LeadStatus(str, enum.Enum):
    NEW = "NEW"
    SUPPLIER_CONTACTED = "SUPPLIER_CONTACTED"
    OFFER_SENT = "OFFER_SENT"
    WON = "WON"
    LOST = "LOST"


class OfferStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    SENT = "SENT"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"
    SUPERSEDED = "SUPERSEDED"


class PaymentType(str, enum.Enum):
    SINGLE = "SINGLE"
    TWO_STAGE = "TWO_STAGE"


class SalesOrderStatus(str, enum.Enum):
    CONFIRMED = "CONFIRMED"
    AWAITING_STOCK = "AWAITING_STOCK"
    IN_PRODUCTION = "IN_PRODUCTION"
    AWAITING_SHIPMENT = "AWAITING_SHIPMENT"
    READY_TO_DISPATCH = "READY_TO_DISPATCH"
    DISPATCHED = "DISPATCHED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


class LineSource(str, enum.Enum):
    FROM_STOCK = "FROM_STOCK"
    IMPORT_ORDER = "IMPORT_ORDER"
    PRODUCTION = "PRODUCTION"


class ProductionStatus(str, enum.Enum):
    PLANNED = "PLANNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ProductionTrigger(str, enum.Enum):
    SALES_ORDER = "SALES_ORDER"
    STOCK_BUILD = "STOCK_BUILD"


class SupplierPOStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    SENT = "SENT"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"


class PaymentStatus(str, enum.Enum):
    UNPAID = "UNPAID"
    DEPOSIT_PAID = "DEPOSIT_PAID"
    FULLY_PAID = "FULLY_PAID"


class ShipmentStatus(str, enum.Enum):
    AWAITING_DISPATCH = "AWAITING_DISPATCH"
    IN_TRANSIT = "IN_TRANSIT"
    CUSTOMS = "CUSTOMS"
    ARRIVED = "ARRIVED"
    RECEIVED = "RECEIVED"


class StockMovementType(str, enum.Enum):
    GOODS_RECEIPT = "GOODS_RECEIPT"
    PRODUCTION_OUTPUT = "PRODUCTION_OUTPUT"
    SALES_DISPATCH = "SALES_DISPATCH"
    RESERVATION = "RESERVATION"
    RESERVATION_RELEASE = "RESERVATION_RELEASE"
    TRANSFER_OUT = "TRANSFER_OUT"
    TRANSFER_IN = "TRANSFER_IN"
    ADJUSTMENT = "ADJUSTMENT"


class TransferStatus(str, enum.Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    DISPATCHED = "DISPATCHED"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"


class InvoiceStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ISSUED = "ISSUED"
    SENT = "SENT"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    PAID = "PAID"
    OVERDUE = "OVERDUE"
    VOID = "VOID"


class DocumentType(str, enum.Enum):
    OFFER = "OFFER"
    INVOICE = "INVOICE"
    DELIVERY_NOTE = "DELIVERY_NOTE"
    SUPPLIER_PO = "SUPPLIER_PO"


class ClientType(str, enum.Enum):
    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"


class OfferLineType(str, enum.Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"
    CUSTOM = "CUSTOM"


class CostComponentType(str, enum.Enum):
    LABOUR = "LABOUR"
    FREIGHT = "FREIGHT"
    CUSTOMS = "CUSTOMS"
    OVERHEAD = "OVERHEAD"
