"use client";
import { Menu, Bell } from "lucide-react";
import { ThemeToggle } from "@/components/navigation/theme-toggle";
import { LanguageToggle } from "@/components/navigation/language-toggle";

interface TopBarProps { onMenuClick: () => void; }

export function TopBar({ onMenuClick }: TopBarProps) {
  return (
    <header className="sticky top-0 z-20 bg-white dark:bg-gray-900
                       border-b border-gray-200 dark:border-gray-800
                       flex items-center gap-3 px-4 h-14 shrink-0">
      {/* Mobile: hamburger */}
      <button
        onClick={onMenuClick}
        className="lg:hidden p-2 -ml-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800"
        aria-label="Open menu"
      >
        <Menu size={20} />
      </button>

      {/* Mobile: brand */}
      <div className="lg:hidden flex items-center gap-2 flex-1">
        <div className="w-6 h-6 rounded bg-gamma-gold flex items-center justify-center">
          <span className="text-gamma-dark font-black text-xs">GI</span>
        </div>
        <span className="font-semibold text-sm text-gamma-dark dark:text-white">
          Gamma ERP
        </span>
      </div>

      <div className="hidden lg:block flex-1" />

      {/* Right side */}
      <div className="flex items-center gap-1">
        <div className="hidden lg:flex items-center gap-1">
          <ThemeToggle />
          <LanguageToggle />
        </div>
        <button className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 relative">
          <Bell size={18} />
        </button>
      </div>
    </header>
  );
}
