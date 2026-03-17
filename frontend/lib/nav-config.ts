import {
  LayoutDashboard, Users, FileText, ShoppingCart,
  Receipt, Package, Factory, Truck, BarChart2,
  Settings, Boxes, Globe, ClipboardList
} from "lucide-react";

export const NAV_ITEMS = [
  { href: "/dashboard",   label: "Dashboard",   icon: LayoutDashboard },
  { href: "/leads",       label: "Leads",        icon: ClipboardList },
  { href: "/offers",      label: "Offers",       icon: FileText },
  { href: "/orders",      label: "Orders",       icon: ShoppingCart },
  { href: "/invoices",    label: "Invoices",     icon: Receipt },
  { href: "/inventory",   label: "Inventory",    icon: Package },
  { href: "/production",  label: "Production",   icon: Factory },
  { href: "/suppliers",   label: "Suppliers",    icon: Globe },
  { href: "/shipments",   label: "Shipments",    icon: Truck },
  { href: "/products",    label: "Products",     icon: Boxes },
  { href: "/clients",     label: "Clients",      icon: Users },
  { href: "/reports",     label: "Reports",      icon: BarChart2 },
  { href: "/settings",    label: "Settings",     icon: Settings },
];

// 5 items for mobile bottom bar (most-used)
export const BOTTOM_NAV_ITEMS = [
  { href: "/dashboard",  label: "Home",      icon: LayoutDashboard },
  { href: "/leads",      label: "Leads",     icon: ClipboardList },
  { href: "/offers",     label: "Offers",    icon: FileText },
  { href: "/orders",     label: "Orders",    icon: ShoppingCart },
  { href: "/invoices",   label: "Invoices",  icon: Receipt },
];

export const CATEGORY_COLORS: Record<string, string> = {
  LED_LIGHTS:          "bg-amber-100  text-amber-800  dark:bg-amber-900/30  dark:text-amber-400",
  HEATER_THERMOCOUPLE: "bg-red-100    text-red-800    dark:bg-red-900/30    dark:text-red-400",
  SOLAR_AC:            "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400",
  TRADE:               "bg-purple-100 text-purple-800 dark:bg-purple-900/30 dark:text-purple-400",
};
