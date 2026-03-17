import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import all models so Alembic can detect them
from app.core.database import Base
from app.modules.auth.models import User
from app.modules.branches.models import Branch, BranchBankAccount, TCTemplate
from app.modules.clients.models import Client
from app.modules.suppliers.models import Supplier
from app.modules.exchange_rates.models import ExchangeRate
from app.modules.leads.models import Lead
from app.modules.supplier_pis.models import SupplierPI, SupplierPILine
from app.modules.products.models import Product, ProductVariant, BOMLine, ProductCostComponent
from app.modules.offers.models import Offer, OfferLine
from app.modules.sales_orders.models import SalesOrder, SalesOrderLine
from app.modules.production.models import ProductionRun, ProductionRunLine, ProductionMaterialConsumption
from app.modules.supplier_pos.models import SupplierPO, SupplierPOLine
from app.modules.shipments.models import Shipment
from app.modules.inventory.models import StockLevel, StockMovement, BranchStockTransfer, BranchStockTransferLine
from app.modules.invoices.models import Invoice
from app.modules.delivery_notes.models import DeliveryNote

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True,
                      dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = configuration["sqlalchemy.url"]
    connectable = async_engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool
    )
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
