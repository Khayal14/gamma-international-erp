"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";
import { NAV_ITEMS, CATEGORY_COLORS } from "@/lib/nav-config";
import { ThemeToggle } from "@/components/navigation/theme-toggle";
import { LanguageToggle } from "@/components/navigation/language-toggle";

interface SidebarProps { onClose?: () => void; }

export function Sidebar({ onClose }: SidebarProps) {
  const pathname = usePathname();

  return (
    <div className="flex flex-col h-full bg-gamma-dark text-white">
      {/* Brand */}
      <div className="flex items-center justify-between px-4 py-4 border-b border-white/10">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gamma-gold flex items-center justify-center shrink-0">
            <span className="text-gamma-dark font-black text-sm">GI</span>
          </div>
          <div className="leading-tight">
            <p className="font-bold text-sm">Gamma International</p>
            <p className="text-xs text-white/50">ERP System</p>
          </div>
        </div>
        {onClose && (
          <button onClick={onClose} className="p-1 rounded hover:bg-white/10">
            <X size={18} />
          </button>
        )}
      </div>

      {/* Nav Items */}
      <nav className="flex-1 overflow-y-auto py-4 px-2 space-y-0.5">
        {NAV_ITEMS.map((item) => {
          const active = pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
              href={item.href}
              onClick={onClose}
              className={cn(
                "flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors",
                active
                  ? "bg-gamma-blue text-white"
                  : "text-white/70 hover:bg-white/10 hover:text-white"
              )}
            >
              <item.icon size={18} className="shrink-0" />
              <span>{item.label}</span>
              {item.badge && (
                <span className="ml-auto bg-gamma-gold text-gamma-dark text-xs font-bold px-1.5 py-0.5 rounded-full">
                  {item.badge}
                </span>
              )}
            </Link>
          );
        })}
      </nav>

      {/* Bottom Controls */}
      <div className="px-4 py-3 border-t border-white/10 flex items-center gap-2">
        <ThemeToggle />
        <LanguageToggle />
      </div>
    </div>
  );
}
