"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";
import { BOTTOM_NAV_ITEMS } from "@/lib/nav-config";

export function BottomNav() {
  const pathname = usePathname();
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-30 bg-white dark:bg-gray-900
                    border-t border-gray-200 dark:border-gray-800
                    flex items-stretch safe-area-inset-bottom">
      {BOTTOM_NAV_ITEMS.map((item) => {
        const active = pathname.startsWith(item.href);
        return (
          <Link
            key={item.href}
            href={item.href}
            className={cn(
              "flex-1 flex flex-col items-center justify-center gap-0.5 py-2 text-xs font-medium transition-colors min-w-0",
              active
                ? "text-gamma-blue dark:text-gamma-gold"
                : "text-gray-500 dark:text-gray-400"
            )}
          >
            <item.icon size={20} className="shrink-0" />
            <span className="truncate w-full text-center px-1">{item.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}
